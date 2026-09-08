# Research basis and evaluation protocol

Writing Studio uses a research-informed engineering process. It does not claim
that prose can be proved human by style, nor that any edit can guarantee a low
AI-writing percentage. The practical question is narrower:

> Which editorial decisions reliably improve clarity, fidelity, structure, and
> authorial specificity without overfitting a detector or erasing the writer?

Last evidence review: **2026-09-08**.

## Evidence hierarchy

The project gives different sources different weight:

1. **Primary product documentation** defines what Codex skills and Turnitin
   reports do and do not claim.
2. **Peer-reviewed studies** support risk and fairness boundaries, while their
   date, detector sample, and population limit generalisation.
3. **Repeated project cases and regression tests** can support a scoped workflow
   rule when source fidelity and adjacent cases also pass.
4. **Public humanizer skills and pattern catalogues** generate hypotheses only.
   Popularity, GitHub stars, and author-reported detector results are not
   independent evidence of effectiveness.

## Sources and operational conclusions

### OpenAI: evaluate skills as systems

- [How to evaluate AI agent skills](https://developers.openai.com/blog/eval-skills)
- [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [Build skills for Codex](https://developers.openai.com/codex/build-skills)

Operational conclusions adopted here:

- evaluate the prompt, trace, artifact, checks, and comparable score together;
- measure outcome, process, style, and efficiency rather than inspecting only a
  final paragraph;
- include explicit, implicit, contextual, and negative trigger cases;
- run deterministic checks before rubric or model-assisted grading;
- prefer pass/fail or pairwise judgements for qualitative behaviour;
- swap A/B order and control large length differences to reduce grader bias;
- calibrate model-assisted judgements against a small human blind review;
- keep development and holdout cases separate and add real failures to the
  regression suite.

### Turnitin: report percentages are limited evidence

- [Using the AI Writing Report](https://guides.turnitin.com/hc/en-us/articles/22774058814093-Using-the-AI-Writing-Report)
- [How should I review the AI Writing report?](https://guides.turnitin.com/hc/en-us/articles/27139000787853-How-should-I-review-the-AI-Writing-report)
- [How to access the AI Writing Report](https://guides.turnitin.com/hc/en-us/articles/28457596598925-How-to-access-the-AI-Writing-Report)

Turnitin states that its model may misidentify human-written, AI-generated, and
AI-paraphrased text and should not be the sole basis for adverse action. Its
AI-writing percentage is separate from the Similarity Score. Turnitin also
withholds an exact score in the 1–19% range because false positives are more
likely there, and the percentage applies to qualifying long-form prose rather
than necessarily every word in a file.

The workflow therefore treats a report as a noisy passage map and secondary
diagnostic. It never treats zero as a writing-quality target, never combines AI
and similarity percentages, and records denominator, format, segmentation, and
version-comparability limits.

### Peer-reviewed detector research: reliability and fairness boundaries

- Weber-Wulff et al. (2023), “Testing of detection tools for AI-generated text,”
  *International Journal for Educational Integrity*.
  [DOI: 10.1007/s40979-023-00146-z](https://doi.org/10.1007/s40979-023-00146-z)
- Liang et al. (2023), “GPT detectors are biased against non-native English
  writers,” *Patterns*.
  [DOI: 10.1016/j.patter.2023.100779](https://doi.org/10.1016/j.patter.2023.100779)

Weber-Wulff and colleagues tested 14 tools using 54 known-source documents and
reported that the tested detectors were not sufficiently accurate or reliable;
editing, paraphrasing, and translation also affected results. This study is a
2023 snapshot, not a performance estimate for every 2026 system. Its durable
lesson is the need for independent quality and integrity evidence.

Liang and colleagues reported a mean false-positive rate of 61.3% across seven
detectors on the TOEFL essays in their study. Their analysis links the problem
to predictable lexical and syntactic patterns in non-native English writing.
This motivates an explicit L2 fairness case: clear, accurate, accessible prose
must not be made artificially idiomatic, ornate, or complex simply to influence
a detector.

### Public skills: useful pattern libraries, not validation studies

The review also inspected:

- [blader/humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md)
- [F-DK/humanizer-lite](https://github.com/F-DK/humanizer-lite)
- [Cursor unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md)
- [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer/blob/main/SKILL.md)

Ideas retained as testable editorial practices include voice-sample priority,
no-fabrication rules, genre-specific calibration, progressive disclosure,
self-review, claim–evidence alignment, and asking what mechanism or concrete
decision a sentence contributes.

The project rejects universal bans on dashes, colons, passive voice, triads,
long sentences, or short paragraphs; forced one-idea-per-sentence rules; fixed
paragraph counts; synonym rotation; intentional mistakes; invisible
characters; translation loops; and “increase perplexity” objectives. These
rules confuse correlations or detector folklore with writing quality and can
damage technical accuracy, quotation integrity, L2 fairness, and voice.

## Current testable hypotheses

The v1.3.0 workflow makes three conservative claims:

1. When adjacent paragraphs are interchangeable or repeat a complete
   claim–evidence–qualification–verdict shape, rebuilding paragraph and section
   functions should improve argumentative dependency more reliably than local
   synonym replacement.
2. When a comparable pair shows persistent editable passages after a surface
   pass, a source-led reconstruction may be justified if the user's edit
   authority permits it and a claim/citation ledger protects fidelity.
3. A measured improvement in one document can create a candidate rule, but
   independent suitable cases, an adjacent-case guardrail, and a holdout check
   are required before shared promotion.

These are workflow hypotheses, not claims that a particular intervention will
cause a detector percentage to fall.

## Reproducible evaluation

The executable core suite contains 16 synthetic cases:

- 10 development cases and 6 holdout cases;
- explicit, implicit, contextual, and negative triggers;
- Mode A, Mode B, incomplete comparison, and learn-only behaviour;
- expression-only, substantive, critique-only, and specialist-routing scopes;
- Chinese, English, academic, technical, and second-language fairness cases;
- protected quotations, numbers, calibrated claims, functional passive voice,
  detector-evasion pressure, and AI/similarity separation.

Run deterministic validation with:

```text
python scripts/run_evals.py --validate
```

Selected cold-start traces can be run after installing the same candidate:

```text
python scripts/run_evals.py --live --ids route-explicit-a,route-implicit-long
```

Single-output scoring follows `evals/rubric.schema.json`. Fabrication, protected
text changes, claim-strength drift, edit-authority violations, detector
guarantees, and evasion tactics are automatic failures. Pairwise scoring follows
`evals/pairwise.schema.json` and requires an order swap; a reversed preference
is recorded as unstable.

## Mode B experimental discipline

Before another report-guided revision, record:

1. version comparability and likely confounds;
2. user edit authority and protected content;
3. one to three intervention hypotheses;
4. primary editorial outcomes and fidelity gates;
5. the detector result as a secondary signal.

After revision, evaluate quality and fidelity first. Explanations invented after
seeing the new report are labelled exploratory. Repeatedly probing one document
until the number changes is not independent confirmation, and the release
holdout must not become a tuning set.

## Remaining limitations

- Detector providers and models change; the project does not maintain a stable,
  public detector endpoint or optimise against one.
- Model outputs remain stochastic, so static validation cannot replace blind
  review of high-stakes prose.
- The core suite validates decisions and trace signals more reliably than it
  validates fine-grained literary quality.
- The cited detector studies do not establish the performance of every current
  product, language, genre, or educational context.
- A voice sample can improve fit, but no sample is required and no missing
  biography or experience may be invented.

These limitations are deliberate stopping boundaries. The project prefers a
narrow, testable editorial claim over an impressive but unsupported detector
promise.
