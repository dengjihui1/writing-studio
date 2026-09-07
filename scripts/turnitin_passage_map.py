"""Map coloured passages in a Turnitin-style PDF report to Markdown paragraphs.

This helper extracts evidence for editorial comparison. It does not predict a
detector score and should not be used to optimise prose against a detector.
Visually confirm representative mappings because report layouts can change.

Example:
    python turnitin_passage_map.py \
      --case v1 56 report-v1.pdf essay-v1.docx \
      --case v2 40 report-v2.pdf essay-v2.md \
      --output passage-map.md
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable

import pdfplumber
from docx import Document


TOKEN_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z0-9]+)?")
DEFAULT_BLUE = (0.3203125, 0.77734375, 0.85546875)


@dataclass(frozen=True)
class Case:
    label: str
    score: str
    report: Path
    source: Path


def tokens(text: str) -> list[str]:
    cleaned = text.replace("**", "").replace("*", "")
    return [token.lower() for token in TOKEN_RE.findall(cleaned)]


def location_sort_key(location: str) -> tuple[str, int]:
    match = re.search(r"(\d+)$", location)
    if match is None:
        return (location, -1)
    return (location[: match.start()].strip(), int(match.group(1)))


def body_paragraphs(path: Path) -> list[tuple[str, str]]:
    if path.suffix.lower() == ".docx":
        paragraphs: list[tuple[str, str]] = []
        in_body = False
        for index, paragraph in enumerate(Document(path).paragraphs):
            text = " ".join(paragraph.text.split())
            if paragraph.style.name.startswith("Heading"):
                heading = text.lower()
                if heading == "references":
                    break
                if heading == "1.0 introduction":
                    in_body = True
                continue
            if in_body and text:
                paragraphs.append((f"DOCX P{index}", text))
        return paragraphs

    blocks = [
        block.strip()
        for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8"))
        if block.strip()
    ]
    paragraphs: list[tuple[str, str]] = []
    in_body = False
    for block in blocks:
        if block.startswith("## "):
            heading = block[3:].strip().lower()
            if heading == "references":
                break
            in_body = True
            continue
        if in_body and not block.startswith("# "):
            text = " ".join(line.strip() for line in block.splitlines())
            paragraphs.append((f"P{len(paragraphs) + 1:02d}", text))
    return paragraphs


def colour_matches(value: object, target: tuple[float, float, float], tolerance: float) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == 3
        and sum(abs(float(value[index]) - target[index]) for index in range(3)) <= tolerance
    )


def report_tokens(
    path: Path,
    target: tuple[float, float, float],
    tolerance: float,
    header_cutoff: float,
    footer_cutoff: float,
) -> list[tuple[str, bool]]:
    result: list[tuple[str, bool]] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            rectangles = [
                rect
                for rect in page.rects
                if colour_matches(rect.get("non_stroking_color"), target, tolerance)
            ]
            # Turnitin sometimes places words from the same paragraph in a
            # non-geometric content-stream order, especially around quotations
            # and page breaks. Text-flow order is more faithful to the visible
            # reading sequence used for editorial mapping.
            for word in page.extract_words(use_text_flow=True, keep_blank_chars=False):
                if word["top"] < header_cutoff or word["bottom"] > footer_cutoff:
                    continue
                centre = (word["x0"] + word["x1"]) / 2
                highlighted = any(
                    word["bottom"] > rect["top"]
                    and word["top"] < rect["bottom"]
                    and centre >= rect["x0"] - 1
                    and centre <= rect["x1"] + 1
                    for rect in rectangles
                )
                result.extend((token, highlighted) for token in tokens(word["text"]))
    return result


def find_exact(haystack: list[str], needle: list[str], start: int = 0) -> int:
    if not needle:
        return -1
    first = needle[0]
    final_start = len(haystack) - len(needle)
    for index in range(start, final_start + 1):
        if haystack[index] == first and haystack[index : index + len(needle)] == needle:
            return index
    return -1


def find_tolerant(
    haystack: list[str], needle: list[str], start: int = 0, max_noise: int = 30
) -> list[int]:
    """Locate a paragraph while tolerating report headers or page-break noise.

    Require an exact eight-token opening anchor, then allow only a small number
    of intervening report tokens. Returned positions correspond to source tokens,
    so colour ratios are not inflated by the skipped report material.
    """
    if len(needle) < 8:
        return []
    anchor = needle[:8]
    search_at = start
    while True:
        match = find_exact(haystack, anchor, search_at)
        if match < 0:
            return []
        positions = list(range(match, match + len(anchor)))
        cursor = positions[-1] + 1
        noise = 0
        failed = False
        for token in needle[len(anchor) :]:
            while cursor < len(haystack) and haystack[cursor] != token:
                cursor += 1
                noise += 1
                if noise > max_noise:
                    failed = True
                    break
            if failed or cursor >= len(haystack):
                failed = True
                break
            positions.append(cursor)
            cursor += 1
        if not failed:
            return positions
        search_at = match + 1


def analyse_case(
    case: Case,
    target: tuple[float, float, float],
    tolerance: float,
    header_cutoff: float,
    footer_cutoff: float,
) -> tuple[list[dict[str, object]], list[int]]:
    stream = report_tokens(
        case.report, target, tolerance, header_cutoff, footer_cutoff
    )
    report_words = [word for word, _ in stream]
    report_flags = [flag for _, flag in stream]
    cursor = 0
    rows: list[dict[str, object]] = []
    missing: list[int] = []

    for number, (location, paragraph) in enumerate(body_paragraphs(case.source), start=1):
        paragraph_words = tokens(paragraph)
        match = find_exact(report_words, paragraph_words, cursor)
        if match < 0:
            match = find_exact(report_words, paragraph_words, 0)
        positions: list[int]
        if match >= 0:
            positions = list(range(match, match + len(paragraph_words)))
        else:
            positions = find_tolerant(report_words, paragraph_words, cursor)
            if not positions:
                positions = find_tolerant(report_words, paragraph_words, 0)
        if not positions:
            missing.append(number)
            continue
        flags = [report_flags[position] for position in positions]
        ratio = sum(flags) / len(flags) if flags else 0.0
        rows.append(
            {
                "paragraph": number,
                "location": location,
                "words": len(paragraph_words),
                "highlighted_words": sum(flags),
                "highlighted_ratio": ratio,
                "lead": " ".join(paragraph_words[:16]),
            }
        )
        cursor = positions[-1] + 1
    return rows, missing


def render_markdown(
    cases: Iterable[Case],
    analyses: Iterable[tuple[list[dict[str, object]], list[int]]],
    minimum_ratio: float,
) -> str:
    case_list = list(cases)
    analysis_list = list(analyses)
    output = [
        "# Detector passage map",
        "",
        "> Editorial evidence only. Visually confirm representative matches before drawing conclusions.",
        "",
    ]
    for case, (rows, missing) in zip(case_list, analysis_list):
        mapped_words = sum(int(row["words"]) for row in rows)
        highlighted_words = sum(int(row["highlighted_words"]) for row in rows)
        mapped_ratio = highlighted_words / mapped_words if mapped_words else 0.0
        visible = [row for row in rows if row["highlighted_ratio"] >= minimum_ratio]
        output.extend(
            [
                f"## {case.label}",
                "",
                f"Reported score: {case.score}",
                "",
                f"Mapped body tokens: {mapped_words}",
                "",
                f"Highlighted tokens among mapped text: {highlighted_words} ({mapped_ratio:.1%})",
                "",
                f"Paragraphs at or above the comparison threshold: {len(visible)}",
                "",
                f"Unmapped paragraphs: {', '.join(map(str, missing)) if missing else 'none'}",
                "",
                "| Paragraph | Source location | Words | Highlighted | Lead |",
                "|---:|---|---:|---:|---|",
            ]
        )
        for row in visible:
            output.append(
                f"| P{row['paragraph']:02d} | {row['location']} | {row['words']} | "
                f"{row['highlighted_ratio']:.1%} | {row['lead']} |"
            )
        if not visible:
            output.append("| - | - | - | - | No paragraphs above threshold |")
        output.append("")

    if len(case_list) > 1:
        output.extend(
            [
                "## Observed location transitions",
                "",
                "> Location-level comparison only. Unmapped or structurally relocated text remains unmeasured, and visual segmentation still requires review.",
                "",
            ]
        )
        for index in range(len(case_list) - 1):
            left_case = case_list[index]
            right_case = case_list[index + 1]
            left_rows = analysis_list[index][0]
            right_rows = analysis_list[index + 1][0]
            left = {str(row["location"]): row for row in left_rows}
            right = {str(row["location"]): row for row in right_rows}
            common = sorted(set(left) & set(right), key=location_sort_key)
            transitions: dict[str, list[str]] = {
                "exited": [],
                "persisted": [],
                "entered": [],
                "unhighlighted": [],
            }
            for location in common:
                was_highlighted = float(left[location]["highlighted_ratio"]) >= minimum_ratio
                is_highlighted = float(right[location]["highlighted_ratio"]) >= minimum_ratio
                if was_highlighted and not is_highlighted:
                    state = "exited"
                elif was_highlighted and is_highlighted:
                    state = "persisted"
                elif not was_highlighted and is_highlighted:
                    state = "entered"
                else:
                    state = "unhighlighted"
                transitions[state].append(location)

            unmeasured = sorted(set(left) ^ set(right), key=location_sort_key)
            output.extend(
                [
                    f"### {left_case.label} -> {right_case.label}",
                    "",
                    f"- Exited: {len(transitions['exited'])} ({', '.join(transitions['exited']) or 'none'})",
                    f"- Persisted: {len(transitions['persisted'])} ({', '.join(transitions['persisted']) or 'none'})",
                    f"- Entered: {len(transitions['entered'])} ({', '.join(transitions['entered']) or 'none'})",
                    f"- Unhighlighted in both: {len(transitions['unhighlighted'])}",
                    f"- Unmeasured in one case: {len(unmeasured)} ({', '.join(unmeasured) or 'none'})",
                    "",
                ]
            )
    return "\n".join(output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        action="append",
        nargs=4,
        metavar=("LABEL", "SCORE", "REPORT_PDF", "SOURCE_MD"),
        required=True,
        help="Add a report/source pair. Repeat to compare versions.",
    )
    parser.add_argument("--output", type=Path, help="Write Markdown instead of stdout.")
    parser.add_argument(
        "--blue", nargs=3, type=float, default=DEFAULT_BLUE, metavar=("R", "G", "B")
    )
    parser.add_argument("--tolerance", type=float, default=0.03)
    parser.add_argument("--minimum-ratio", type=float, default=0.03)
    parser.add_argument("--header-cutoff", type=float, default=65.0)
    parser.add_argument("--footer-cutoff", type=float, default=730.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cases = [
        Case(label, score, Path(report), Path(source))
        for label, score, report, source in args.case
    ]
    for case in cases:
        if not case.report.is_file():
            raise FileNotFoundError(case.report)
        if not case.source.is_file():
            raise FileNotFoundError(case.source)

    target = tuple(args.blue)
    analyses = [
        analyse_case(
            case,
            target,
            args.tolerance,
            args.header_cutoff,
            args.footer_cutoff,
        )
        for case in cases
    ]
    content = render_markdown(cases, analyses, args.minimum_ratio)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content + "\n", encoding="utf-8")
    else:
        print(content)


if __name__ == "__main__":
    main()
