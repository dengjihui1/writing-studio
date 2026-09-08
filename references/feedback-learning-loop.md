# Feedback-to-regression learning loop

Use this reference when maintaining Writing Studio from accepted user corrections, measured before-and-after revisions, or repeated workflow failures. It governs skill evolution, not ordinary writing output.

## Purpose

A successful revision is evidence, not automatically a rule. Convert real feedback into a reproducible, scoped learning record before changing default behaviour. This prevents the skill from overfitting one document, detector version, genre, language, or user preference.

The loop is:

`observed result -> precommitted candidate rule -> development case -> adjacent-case check -> holdout confirmation -> promote, narrow, or reject`

## Evidence strength

Not all supporting material carries the same weight:

| Level | Evidence | Permitted conclusion |
|---|---|---|
| diagnostic | a public pattern list, maintainer intuition, or one detector highlight | use as an inspection prompt only |
| candidate | one accepted correction or one comparable measured pair | write a scoped hypothesis and development case |
| repeated candidate | several passages or iterations in the same document | strengthen the local diagnosis, but do not claim independence |
| scoped | repeated editorial benefit across independent suitable documents or synthetic cases, plus an adjacent-case pass | use inside the supported genre, language, section, and authority boundary |
| promoted | representative development cases and untouched holdout cases pass with no material integrity regression | use in the shared default workflow |

GitHub stars, a skill author's self-reported detector result, and a list of alleged AI words are not independent validation. They may suggest a candidate test, but they do not justify a universal rule.

## 1. Capture the correction

Record only what is needed to reproduce the decision:

| Field | Meaning |
|---|---|
| observed failure | what the earlier workflow did poorly |
| accepted result | what the user accepted or what materially improved |
| evidence | draft/report facts, passage deltas, or fidelity checks supporting the observation |
| scope | genre, language, section type, edit authority, and input conditions where the lesson may apply |
| out of scope | cases the evidence does not cover |
| confounds | format, length, segmentation, detector version, or concurrent edits that limit attribution |
| candidate rule | the smallest decision rule that could prevent recurrence |
| regression case | a realistic input and observable expected behaviour |

Before changing instructions, write the candidate rule and its expected observable quality effect. If the rationale is written only after the result is known, label it exploratory and test it prospectively on another case.

For public records, use anonymised summaries or synthetic fixtures. Never publish source drafts, report IDs, names, interview quotations, local paths, or other identifying material without explicit permission.

## 2. Write a decision rule, not a style superstition

A useful candidate rule changes a decision under stated conditions. It does not ban a word, punctuation mark, sentence length, paragraph length, or grammatical form.

Prefer:

> When a comparable pair shows persistent editable passages after surface polishing, rebuild the section's evidence order before another sentence-level pass.

Avoid:

> Never use long sentences, transitions, lists, or balanced clauses.

Keep causal language calibrated. A report movement may be consistent with an intervention without proving that the intervention caused the movement.

## 3. Add the development case first

Before promoting a candidate rule into `SKILL.md` or a default reference workflow:

1. add a realistic case to `evals/core-cases.jsonl` in the `dev` split and, when useful, expand the narrative catalogue in `references/evaluation.md`;
2. define observable process and output expectations;
3. include the fidelity or integrity condition that must remain protected;
4. include at least one adjacent case where over-application would be harmful.

The case should test a decision, not exact generated wording.

Keep a separate `holdout` split for release checks. Do not repeatedly inspect the holdout output and then tune instructions to it; move a newly diagnosed failure into development and reserve another independent case for later confirmation.

## 4. Classify the lesson

Use one of three states:

- **candidate:** supported by one accepted correction or one measured pair; keep local or experimental;
- **scoped:** repeated within a defined genre, language, section type, or input condition; use only inside that boundary;
- **promoted:** supported across representative and adjacent cases with no material fidelity regression; safe for the shared workflow.

One dramatic score change is still one observation. Repeated passes over one document are also dependent observations. Prefer repeated directional evidence across independent suitable cases, stable content budgets, passage-level comparison, and independent quality checks.

## 5. Run adjacent-case and integrity checks

Test whether the candidate rule would:

- alter facts, quotations, citations, numbers, causal direction, certainty, or required coverage;
- override expression-only authority with structural change;
- make academic prose informal or narrative prose artificially academic;
- turn a local English pattern into a universal multilingual rule;
- optimise a detector percentage at the expense of writing quality;
- add process burden to ordinary Mode A requests that do not need it.

If so, narrow or reject the rule. A regression in source fidelity is an automatic failure even when a report percentage moves.

For qualitative comparisons, anonymise outputs as A and B, judge them in both orders, and treat an order reversal as unstable. Control large length differences and calibrate model-assisted judgements against a small human blind review. Detector movement may be logged as a secondary signal; it cannot rescue a fidelity or edit-authority failure.

## 6. Promote narrowly and keep provenance

When a rule passes:

1. update the smallest relevant reference rather than expanding the entrypoint by default;
2. link the regression case to the rule conceptually through its name and scope;
3. record the version in which behaviour changed;
4. retain uncertainty and stopping boundaries;
5. remove or revise the rule if later evidence contradicts it.

Record which cases were used for development and which were untouched holdouts. A promoted rule should remain reversible: later cross-genre, multilingual, fairness, or fidelity failures are reasons to narrow or retire it.

Mode A may use promoted shared lessons without requiring historical evidence from the current user. Mode B may generate new candidate lessons from a measured pair, but those candidates do not become universal defaults until they pass this loop.
