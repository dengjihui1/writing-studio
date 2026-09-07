# Intake and routing

## Choose the execution mode first

Execution mode answers what evidence the workflow can learn from. Edit depth answers how much it may change. Keep those decisions separate.

| Available material and request | Route | Required behaviour |
|---|---|---|
| Notes, source material, or no existing prose | **Mode A — Direct writing / single-draft** | Plan and draft normally from the evidence boundary |
| One current draft, with no detector report | **Mode A** | Diagnose and revise directly; do not request a report or older version |
| One current draft plus one AI-writing report | **Mode A with report-assisted inspection** | Use highlights as noisy local signals; do not claim before-and-after learning |
| Two drafts but only one report, or two reports without their corresponding drafts | **Mode A plus limited comparison** | Describe only observable differences; do not attribute score movement to specific edits |
| Before draft + before AI report + after draft + after AI report | **Mode B — Comparative report learning** | Check comparability, map passage states, identify recurring correlated changes, and transfer supported lessons |
| A complete measured pair, but the user asks only to improve the skill or summarize learning | **Mode B, learn-only** | Freeze the artifact; extract reusable lessons without another document edit |

Mode B's minimum reliable comparison set is:

1. the before draft;
2. its AI-writing report;
3. the after draft;
4. its AI-writing report.

The current version to revise may be the after draft or a later supplied draft. A similarity report is optional and must remain a separate integrity review. If a required component is absent, continue with the safe work supported by the available material instead of blocking ordinary revision; label any comparison as limited.

## Minimum writing contract

Infer these fields from the request and supplied material. Ask only for a field whose absence blocks a materially correct result.

| Field | Default when absent |
|---|---|
| Operation | Draft if no prose exists; first-pass humanization if the user asks for naturalization or removal of AI-like/formulaic writing; otherwise substantive polish if prose exists |
| Audience | An informed general reader appropriate to the topic |
| Purpose | Explain or persuade, inferred from the requested genre |
| Medium | Plain text or Markdown |
| Language | Match the user's requested output; otherwise match the source |
| Length | Proportional to the material and medium |
| Evidence boundary | User-supplied material only unless research is requested or clearly required |
| Voice | Clear, natural, restrained, and genre-appropriate |
| Edit depth | Substantive edit that preserves facts and intent |
| Content budget | Preserve required claims, evidence, qualifications, protected text, and proportionate development; do not compress by default |
| Detector evidence | Optional and never required; when supplied, treat scores and highlights as noisy revision signals, not proof or a target |

## Mode-specific defaults

### Mode A — Direct writing / single-draft

- Complete the writing or revision in the first pass at the strongest edit depth allowed by the user's authority.
- Diagnose structure, paragraph ancestry, evidence use, abstraction, cadence, and closure from the text itself.
- Do not delay a substantive reconstruction to wait for a future detector result.
- Deliver the finished text or requested artifact first, with a short change summary only when useful.

### Mode B — Comparative report learning

- Validate that each report belongs to its stated draft and note material format, length, or detector-setting differences.
- Compare passage states and internal controls before forming a revision hypothesis.
- Distinguish layout, surface, structural, and epistemic interventions; do not credit a score change to one feature without controls.
- Default to **learn-and-revise** when the user asks to continue polishing, **learn-only** when the user says the document is finished, and **diagnose-only** when the user requests analysis rather than editing.
- Deliver a compact comparison diagnosis before or alongside the revised artifact so the next intervention is auditable.

## Operation routing

- **Plan:** Return the reader promise, evidence inventory, outline, and key risks. Do not draft full prose unless useful as a small sample.
- **Draft:** Build the argument and structure before producing prose.
- **Rewrite:** Reconstruct weak structure or expression while preserving the underlying claims and ownership.
- **First-pass humanization:** Work from the sole current draft. Diagnose structure, paragraph ancestry, evidence use, abstraction, cadence, and closure; use deep reconstruction immediately when the draft is highly templated or the stakes are high. Do not ask for a detector report, older version, or writing sample unless the user independently wants voice matching or report analysis.
- **Expression-only polish:** Preserve the argument, evidence coverage, conclusion, protected text, and approximate length. Improve wording, sentence movement, citation integration, and local paragraph flow without silently deleting development.
- **Polish:** Improve clarity, flow, tone, concision, and mechanics without changing substantive meaning.
- **Translate:** Preserve meaning and evidentiary strength, then naturalize for target-language genre conventions.
- **Critique:** Diagnose first. Do not silently rewrite the whole piece unless asked.
- **Report-guided rewrite (Mode B):** Compare reports and versions, identify persistent passage patterns, then choose surface, structural, or epistemic intervention proportionally.

## Edit-depth contract

- **Expression-only:** Language and local flow only; keep the content budget stable.
- **Light:** Grammar, punctuation, awkward phrasing, and local clarity only.
- **Substantive:** Reorder sentences or paragraphs, remove repetition, strengthen transitions, and tighten claims without changing the thesis.
- **Full rewrite:** Rebuild structure and prose from the source material; preserve the source boundary and list major assumptions. Use on the first pass when the sole draft is heavily templated, prompt-shaped, structurally interchangeable, or high-stakes, as well as when later report evidence shows persistent highlighted clusters.

## Useful questions when truly needed

Prefer one compact question containing only the unresolved decision. Common blockers are:

- mutually incompatible audiences or publication venues;
- a strict word limit that is not provided;
- a requested factual or personal claim with no supporting material;
- unclear permission to research beyond supplied sources;
- an edit that may substantially change the author's position.

Do not ask the user to choose among writing frameworks. Select the framework that fits the contract.
