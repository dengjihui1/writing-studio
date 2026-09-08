# Writing Studio evaluation kit

This directory turns Writing Studio's editorial claims into small, repeatable
checks. It is intentionally not a detector benchmark. A detector percentage is
a noisy secondary observation; factual fidelity, edit authority, reasoning
quality, and useful delivery remain the primary outcomes.

## Files

- `core-cases.jsonl` contains a compact development/holdout suite. Each line is
  one synthetic case with a routing expectation, observable process
  requirements, protected literals, and prohibited behaviour.
- `rubric.schema.json` defines the record for single-output grading.
- `pairwise.schema.json` defines an order-swapped A/B comparison record.
- `../references/evaluation.md` retains the larger behavioural catalogue.
- `../scripts/run_evals.py` validates the suite and can run selected cold-start
  Codex traces.

No private draft, detector report, report identifier, interview quotation, or
local user path belongs in this directory. Convert real failures into synthetic
fixtures before committing them.

## Quick checks

Run the deterministic validation before every release:

```text
python scripts/run_evals.py --validate
```

This checks JSONL shape, unique IDs, development/holdout separation, coverage,
schema readability, protected-literal declarations, and obvious privacy leaks.

Live traces are optional because they consume model usage and have stochastic
outputs. Install the candidate skill first, then run only the cases needed for
the change:

```text
python scripts/run_evals.py --live --ids route-explicit-a,route-implicit-long
```

The runner refuses to test when the installed skill differs from the candidate
runtime files unless `--allow-skill-mismatch` is supplied. This prevents a
common false result: editing one copy while evaluating another.

## Evaluation protocol

1. Write the failure and candidate rule before changing runtime instructions.
2. Put ordinary iterations in the `dev` split.
3. Keep `holdout` cases hidden from rule-by-rule tuning; run them at a release
   boundary or after a coherent batch of changes.
4. Run deterministic checks first: routing trace, protected literals, forbidden
   zero-width characters, command count, and token usage.
5. Grade content with `rubric.schema.json`. Any integrity failure is an
   automatic failure regardless of the mean score.
6. For qualitative comparisons, anonymise candidates as A and B, judge twice
   with their order swapped, and use `pairwise.schema.json`. Treat a reversal as
   unstable rather than choosing the preferred order.
7. Calibrate model-assisted grading against a small human blind review. Control
   large length differences because graders can prefer longer answers.
8. Promote a rule only after representative and adjacent cases pass. One score
   movement in one document remains exploratory evidence.

The live runner records trace and efficiency signals; it does not pretend to
automatically judge prose quality. Human or model-assisted rubric scoring is a
separate, inspectable step.
