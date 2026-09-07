# Contributing to Writing Studio

Writing Studio improves through evidence-backed corrections, not accumulating style preferences.

## Before proposing a change

Describe:

1. the observed failure;
2. the accepted or demonstrably better result;
3. the supported scope and known confounds;
4. the smallest candidate decision rule;
5. one realistic regression case;
6. one adjacent case where over-application would be harmful.

Do not include private drafts, report IDs, student or participant names, interview quotations, local paths, or identifying metadata. Use anonymised summaries or synthetic fixtures.

## Pull-request expectations

- Keep `SKILL.md` concise and route conditional detail into `references/`.
- Preserve facts, evidence boundaries, quotations, citations, claim strength, and user edit authority.
- Add or update a case in `references/evaluation.md` for behavioural changes.
- Test changed scripts and include the command and result.
- Avoid universal word bans, detector guarantees, evasion tactics, and rules derived from a single uncontrolled score movement.
- Explain whether the lesson is candidate, scoped, or promoted.

## Commit style

Prefer focused commits such as:

```text
feat: add a scoped report-comparison rule
test: protect expression-only edit authority
docs: clarify Mode B input requirements
fix: preserve mixed quotation islands during mapping
```

## Release check

Before release:

1. validate `SKILL.md` frontmatter and all local links;
2. run `scripts/turnitin_passage_map.py --help` and any relevant smoke test;
3. review representative and adjacent evaluation cases;
4. scan the repository for private paths, reports, drafts, generated caches, and credentials;
5. confirm that the packaged and installed copies match the reviewed source.

