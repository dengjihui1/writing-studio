# Mode B — Comparative report learning

## Contents

1. Comparability, report types, and length controls
2. Editable, conditional, and protected text
3. Passage deltas and internal controls
4. Intervention classification and escalation
5. Evidence-led reconstruction and section resets
6. Paragraph interiors and source use
7. Ordered revision passes
8. Honest reporting and stopping boundaries

## Purpose and boundary

Read this file for Mode B or when the user supplies a detector report, highlighted passages, scores, or comparable versions. Mode B learns from a measured before-and-after pair. A single report may assist Mode A diagnosis, but cannot establish which earlier changes correlated with movement. A report is never an input requirement for first-pass humanization.

Use an AI-writing report as a noisy map of passages worth examining. It is not a verdict on authorship and not a reliable objective function. A lower percentage may follow from better writing, but it may also follow from changes in paragraph boundaries, qualifying-text count, document conversion, or model updates. A new user with only one draft must still receive a complete structural and stylistic reconstruction when the text warrants it.

The editorial objective remains clear, specific, evidence-bound prose with a recognisable authorial position. Never promise a target score or use deliberate errors, fabricated experience, hidden characters, translation loops, synonym spinning, or other bypass tactics.

## Mode B input and action contract

For a reliable comparative learning pass, identify:

| Role | Required evidence |
|---|---|
| Before state | before draft and its AI-writing report |
| After state | after draft and its AI-writing report |
| Revision target | the after draft or a later current draft to be revised |
| Optional integrity evidence | similarity report or other source-use report, reviewed separately |

Confirm report-to-draft pairing from filenames, submission metadata, length, headings, quotations, and representative highlighted text. If pair ownership is uncertain, say so and limit the diagnosis.

Choose exactly one action:

- **learn-and-revise:** produce a delta diagnosis, construct supported intervention hypotheses, revise the current target, and run fidelity checks;
- **learn-only:** leave all supplied drafts unchanged and record only reusable lessons supported by the comparison;
- **diagnose-only:** report the comparison and its uncertainty without rewriting.

If only reports are supplied without their corresponding editable drafts, compare report-level metadata and visible highlighted passages only. Do not claim reliable paragraph ancestry, edit attribution, or a complete next-pass rewrite from that evidence alone.

### Mode B diagnostic record

Before revising, create a compact internal record with:

1. pair identity and comparability limits;
2. overall percentages, segment counts, and reported word counts;
3. exited, persisted, entered, and unmeasured passage samples;
4. protected, conditional, editable, and mixed ownership classes;
5. the previous intervention mix: layout, surface, structural, and epistemic;
6. recurring differences between exits, persistent passages, and local unhighlighted controls;
7. supported next-pass hypotheses, rejected hypotheses, and the chosen change authority.

Do not start the next prose pass until this record identifies what should be preserved, what should change, and what the reports cannot establish.

## 1. Establish comparability

Record the available evidence before attributing a change:

- report provider and date;
- overall percentage and number of highlighted segments;
- qualifying or reported word count;
- document format, headings, tables, captions, quotations, and references;
- which prose, paragraph breaks, or layout elements changed between versions;
- whether the same detector model and settings were used, if known.

If structure, wording, and format all changed, describe the score movement as the result of a combined intervention. Do not assign a percentage-point effect to one edit unless the other variables were held stable.

### Keep AI-writing and similarity evidence separate

An AI-writing report and a similarity report answer different questions. Never combine their percentages or treat one as confirmation of the other.

- Use AI-writing highlights only as noisy editorial signals about passage patterns.
- Use similarity matches to inspect source dependence, citation placement, quotation treatment, match groups, and integrity flags.
- A modest non-zero similarity result can coexist with careful academic writing because references, technical terms, institutional wording, and legitimately cited material may overlap with sources.
- Zero similarity is not a quality target. Do not over-paraphrase, remove necessary terminology, weaken citations, or distort quotations to reduce it.
- When match categories are available, distinguish uncited/unquoted matches, missing quotation marks, missing citations, cited-and-quoted material, bibliography, and excluded text before deciding whether any action is warranted.

Record submission metadata separately for the two reports. Matching file name, page count, word count, character count, and file size support comparability, but different submission IDs or times should still be disclosed when the distinction matters.

### Treat length as a control, not an objective

Record the reported word count and, when available, the editable body word count for each version. If a score falls while the document stays approximately the same length or becomes slightly longer, the result is evidence against attributing the change to compression. Look instead at changes in paragraph function, evidence order, situated judgement, and section dependency. This remains correlational: stable length does not prove that any one rhetorical change caused the movement.

Never infer the reverse rule that expansion is inherently more human. Preserve the user's content budget. Shorten repetition and padding when editorially justified; restore or retain development when it carries evidence, reasoning, qualification, or a required explanation.

## 2. Separate editable and protected text

Before interpreting any highlight, classify the underlying text:

| Class | Typical material | Permitted action |
|---|---|---|
| protected | verbatim interview or survey quotations, numerical results, proper names, fixed labels, equations, titles, and exact source language that must remain quoted | keep exact; revise only the author's framing around it |
| conditional | conventional methods terminology, instrument wording, institutional or ethics language, definitions, and close source paraphrase | edit only if accuracy, compliance, and citation scope remain intact |
| editable | the author's synthesis, interpretation, transitions, argument, section framing, and conclusions | restructure or rewrite within the evidence boundary |

Estimate both the report-wide highlighted share and the highlighted share of editable author prose when the report permits it. Also record how much of the highlighted material is protected or conventional. This is not a replacement score; it prevents the workflow from treating immutable testimony or data as if it were weak prose.

If protected text creates an apparent score floor, state that plainly. Do not alter a participant's wording, split a quotation to conceal it, translate it back and forth, or convert data into less precise prose for the sake of a detector.

## 3. Build a passage delta map

Compare text, not only page images. Map representative passages into four groups:

| State | Meaning | Editorial use |
|---|---|---|
| exited | highlighted before, not highlighted now | look for changes shared across several exits |
| persisted | highlighted in both versions | local polishing probably did not reach the underlying pattern |
| entered | newly highlighted | check for new abstraction, symmetry, seams, or factual drift |
| unmeasured | moved, deleted, reformatted, or outside qualifying prose | do not treat as evidence of improvement |

For every mapped passage, note:

- paragraph job and local question;
- concrete actors, objects, actions, and conditions;
- claim-to-evidence relationship;
- citation function: evidence, definition, contrast, limit, or context;
- sentence-function sequence, not just sentence length;
- opening and closing move;
- whether the paragraph contains a visible seam from two earlier units;
- whether adjacent paragraphs could be swapped without damaging the argument.
- whether the highlighted span is protected, conditional, editable, or mixed.

Look for clusters across passages. One transition, one long sentence, or one tidy paragraph proves nothing.

### Use negative space as an internal control

Do not study highlights alone. Select several substantial passages that stayed unhighlighted in the same version and compare them with persistent clusters. This controls, imperfectly, for the writer, topic, genre, citation style, and file conversion.

Record differences in:

- entry point: case, actor, problem, definition, or summary;
- information selection: one local issue or exhaustive coverage;
- syntactic load: concrete clauses or noun-heavy compression;
- citation work: evidence, limit, contrast, or background;
- ending: consequence, unresolved boundary, judgement, or complete recap;
- paragraph ancestry: whether the paragraph still exposes the outline or prompt from which it was generated.

Treat repeated contrasts as hypotheses. An unhighlighted paragraph is a positive local control, not proof that its surface style should be copied everywhere.

Build a short internal-control profile before rewriting. Prefer substantial unhighlighted passages from the same chapter and same prose type. Record only stable contrasts that recur across at least three examples. Useful dimensions include where the paragraph enters, how it allocates space, whether a case develops across sentences, how citations change the reasoning, and whether the ending leaves a live consequence. Do not imitate accidental quirks or copy wording.

## 4. Distinguish surface change from reasoning change

Classify the intervention that produced each difference:

1. **Layout:** paragraph break, heading, caption, list, quotation, or file conversion changed.
2. **Surface:** vocabulary, transition, punctuation, or sentence length changed while the reasoning stayed the same.
3. **Structural:** the order, paragraph job, evidence allocation, or argument dependency changed.
4. **Epistemic:** the writer changed what is claimed, how strongly, on what evidence, or with what limit.

Layout and surface changes can improve readability, but they are weak evidence that a deeply templated passage has been repaired. Persisting highlights after paraphrase usually call for structural or epistemic work.

### Escalation rule after a failed revision

When comparable reports remain effectively unchanged, classify what the previous pass actually changed and move up at least one level:

| Previous pass | Do not repeat | Next legitimate intervention |
|---|---|---|
| synonym or rhythm edit | another synonym or rhythm edit | rebuild paragraph function and evidence order |
| paragraph merge or split | more arbitrary merging or splitting | reconstruct around one governing question and remove seams |
| paragraph reconstruction with the same section order | another close paraphrase | reset the section spine and redistribute evidence |
| full section reset | endless rewrites for a percentage | audit protected/conventional text, integrity, and whether further change would harm the work |

Treat a change of a few segments with a flat or worse overall percentage as no demonstrated improvement unless the editable-prose mapping shows otherwise. Do not congratulate the intervention because some spans exited when longer spans entered.

## 5. Reconstruct from evidence units

For deep mode, stop editing sentence by sentence. Build a small ledger for the affected section:

| Unit | Preserve exactly | Editorial question |
|---|---|---|
| claim | proposition and scope | what is the narrowest defensible claim? |
| evidence | case, quotation, number, example, or source | what does it establish, and what does it not establish? |
| mechanism | actor, action, condition, consequence | how does the evidence bear on the claim? |
| limit | uncertainty, counterexample, or boundary | where would the claim stop being reliable? |
| judgement | implication for this document's thesis | what decision or interpretation follows here? |

Then rebuild each paragraph around one live question or tension. Useful movements include:

- a case exposes a problem, which changes the interpretation;
- a claim is narrowed by a mechanism or counterexample;
- two sources disagree or operate at different levels, requiring a local judgement;
- an operational decision creates a trade-off whose distribution matters;
- a general proposition is tested against one concrete instance.

These are options, not templates. Consecutive paragraphs should not repeat the same movement.

### Discourse reset for persistent clusters

Use a discourse reset when a passage survives a substantive rewrite, or when several adjacent paragraphs remain recognisably answer-shaped. Stop revising the old sentences. Preserve only the evidence ledger and citation boundaries, then:

1. choose a concrete case, decision, disputed record, or operational failure as the section's spine;
2. decide what the reader must learn from that spine before introducing general concepts;
3. ration background and definitions to what the local question needs;
4. let evidence receive unequal space according to its importance instead of balancing every benefit with a matching cost;
5. move secondary material to another paragraph or remove it when it merely proves coverage;
6. write a new sequence without consulting the old sentence order, then run a fidelity comparison.

The aim is not novelty for its own sake. It is to remove the inherited prompt-to-outline-to-paragraph pipeline while preserving the supported argument.

### Source-blackout drafting

For a cluster that has persisted across a substantive revision, use a temporary source blackout:

1. extract a ledger of exact claims, evidence, citations, quotations, numbers, and limits;
2. write the new section-function sequence without copying the old headings or paragraph sequence unless they are mandated;
3. put the old prose out of view and draft only from the ledger and the new sequence;
4. reopen the source for a line-by-line fidelity audit;
5. restore any required content that was lost, but do not restore the old rhetorical order by default.

The proposed section must have a materially different function chain. For example, `background -> benefits -> risks -> balanced conclusion` has not changed merely because it becomes `context -> opportunities -> limitations -> synthesis`.

### Learn from improvement without overfitting

When a comparable revision produces a real but modest improvement, do not treat the whole pass as either a success or a failure. Build two small samples from editable author prose:

- passages that exited after revision;
- passages that remained substantially highlighted after revision.

Compare them by editorial function, not surface statistics. Ask whether exited passages became more situated in an actual decision, procedure, participant difference, contrast, negative case, or operational consequence; whether citations changed the local judgement instead of being processed as source cards; whether persistent passages still read as literature inventories, conventional methods assurances, complete answer units, compressed chapter summaries, or mixed quotation islands; and whether the section still allocates equal space and closure to every point. Also check whether conclusions resolve a governing distinction through evidence rather than replaying every research question in equal blocks.

Require these contrasts to recur across several passages before turning them into a rule. Do not copy wording, punctuation, openings, paragraph length, or isolated quirks from an exited passage. The legitimate lesson is the change in reasoning, evidence use, and section dependency. A percentage movement produced by a combined rewrite is evidence that some intervention correlated with improvement, not a calibration table for manufacturing a further drop.

When a material movement occurs while facts, citations, protected text, argument, and overall length remain stable, treat that as evidence against a simple compression explanation. If the user has decided that the document is finished, switch to **learn-only mode**: freeze the artifact, record the evidence, update the skill and its evaluation cases, and make no further prose changes.

### Second reset for persistent section patterns

A source-blackout paragraph can still inherit the section's old cognitive shape. Before another rewrite, audit the full cluster on four dimensions:

1. **Entry:** Do consecutive paragraphs enter through a generic summary or a source name, or do they begin from different supported objects such as a result, case, methodological choice, disagreement, or unresolved observation?
2. **Partition:** Does each paragraph contain a complete claim-evidence-qualification-verdict package? If so, redistribute the work so that at least some paragraphs depend on the evidence or problem established immediately before them.
3. **Citation staging:** Are sources processed one at a time with the same safe gloss? Synthesize overlapping findings once, place disagreement or scope difference where it changes the argument, and keep every citation attached to the proposition it actually supports.
4. **Closure density:** Do three or more consecutive paragraphs end with broad balanced judgements? Replace only the unnecessary closures. A paragraph may end on a concrete consequence, remaining limit, evidential complication, or a term the next paragraph must resolve.

Then write a new section-function sequence. This second reset must change at least two of entry point, evidence grouping, paragraph dependency, citation function, or allocation of space. Rephrasing every paragraph separately is not enough.

For methods prose, the same test has a specific form. Replace generic assurances that a standard method was appropriate, flexible, rigorous, or aligned with the actual audit trail: what the researcher did first, what was checked, which alternative was rejected, what constraint remained, and how that choice limits interpretation. Conventional terminology may remain where needed, but it should not carry the paragraph by itself.

For findings containing protected quotations, distinguish quotation islands from author prose. A report may highlight the verbatim testimony and the framing around it as one visual block. Preserve the testimony exactly; revise the analytical relation before and after it only when that relation is weak. Report the protected share separately instead of forcing a visual break or changing quotation boundaries to influence segmentation.

Also inspect the detector's segmentation boundary. A single coloured region may extend across a protected quotation, a short framing sentence, and the next analytical paragraph. Do not label all text inside that visual island as the same ownership class, and do not claim that a newly highlighted paragraph necessarily became worse when it may have entered a larger contiguous segment. Passage mapping must be checked against paragraph text and page images.

### Academic section patterns that often need different resets

These are diagnostic options, not replacement templates:

- **Introduction:** begin from the specific empirical or interpretive problem already supported, then introduce only the concepts needed to define the gap. Avoid a complete topic tour before the research problem appears.
- **Literature review:** organise around a disagreement, unresolved mechanism, scope boundary, or difference in level of analysis. Avoid one source card per paragraph and repeated consensus-limit-takeaway endings.
- **Methods:** present the actual chain of research decisions, constraints, alternatives rejected, and consequences for interpretation. Do not pad the chapter with generic claims that every standard method is flexible, appropriate, rigorous, and aligned.
- **Findings:** keep participant quotations exact. Let the author's analysis compare, narrow, or complicate them instead of adding a complete explanatory sentence after every quotation.
- **Discussion:** organise around what the findings changed, failed to confirm, or made conditional. Do not simply replay the literature review with new citations.
- **Conclusion:** resolve the governing judgement from the strongest evidence and remaining boundary. Do not inventory every research question in equal blocks unless the brief requires it.

## 6. Repair paragraph interiors

A paragraph should develop, not merely contain, a point. Check every sentence for what changes after it: the evidence, scale, actor, condition, confidence, objection, or consequence.

Use three tests:

- **Dependency test:** if a sentence can move anywhere in the section unchanged, its relation is probably too generic.
- **Swap test:** if two adjacent paragraphs can change places with no effect, the section is a stack of mini-essays rather than an unfolding argument.
- **Seam test:** if a long paragraph contains a second topic sentence, repeated setup, or a fresh summary halfway through, it was probably merged rather than rebuilt.

Merge paragraphs only when they answer the same local question and the combined paragraph has one movement. Split at a genuine change of problem, scale, actor, evidence type, or argumentative direction. Paragraph length is an outcome of thought; do not target a fixed word count or make all paragraphs deliberately uneven.

## 7. Control abstraction and source use

Avoid long runs in which every sentence names abstractions and supplies a complete judgement. Move between levels when the evidence allows it:

- institution or person;
- action or workflow;
- observable consequence;
- interpretation;
- boundary or decision.

Do not manufacture a scene or anecdote. In academic and professional writing, concrete institutional action, procedural detail, source disagreement, and bounded judgement provide authorship without informality.

Integrate citations by function. A source should do identifiable work in the sentence or paragraph. Avoid both citation dumping and the repeated pattern of source summary followed by a safe qualification followed by a universal takeaway. Where several sources make the same broad point, synthesise them once and spend more space on what the comparison changes.

Inspect linguistic density when academic prose remains unnaturally compressed. Instruction-tuned prose often overuses nominalisations, present-participial add-ons, and coordinated noun phrases. These are not prohibited forms. Revise only sustained clusters that hide actors, actions, chronology, or relative importance. Prefer a finite clause when it makes responsibility or sequence clearer; unpack a noun chain when the reader otherwise has to reconstruct the action.

Run the **answer-shape test**: could the paragraph be reduced to a generic instruction such as “define the concept, list advantages and disadvantages, qualify them, then conclude”? If so, its completeness may be the problem. Re-enter through the evidence and allow the paragraph to answer one narrower question.

## 8. Run passes in the right order

1. **Comparability and ownership:** record report facts; separate protected, conditional, editable, and mixed spans.
2. **Delta diagnosis:** compare versions and classify report changes.
3. **Internal-control profile:** compare persistent editable prose with substantial unhighlighted prose of the same type.
4. **Strategy escalation:** identify the previous intervention class and prohibit a failed class from being repeated.
5. **Argument reset:** recover claims, evidence, limits, and section dependency; write a materially different section-function sequence.
6. **Source-blackout reconstruction:** draft persistent clusters from the ledger rather than the old sentences.
7. **Seam and adjacency pass:** run dependency, swap, ancestry, closure, and seam tests.
8. **Sentence pass:** remove formulaic wording, hollow transitions, mechanical symmetry, and uniform closure.
9. **Fidelity pass:** compare names, numbers, quotations, citations, causality, scope, and certainty with the source.
10. **Prompt-shape and density pass:** inspect nominalisation clusters, participial add-ons, coordinated noun strings, exhaustive coverage, and over-complete conclusions.
11. **Section-dependency pass:** map entry type, citation staging, and final-sentence function across each persistent cluster; repair repeated self-contained answer cards and excessive closure density.
12. **Independent read:** ask what still feels preassembled, over-complete, or interchangeable; revise only those passages.
13. **Paired-report integrity pass:** if a similarity report is supplied, review its match categories and integrity flags separately; never optimise its percentage as part of the AI-writing pass.
14. **Stop check:** honour a user decision to end document revision; convert the remaining evidence into workflow learning rather than continuing to edit.

The helper `scripts/turnitin_passage_map.py` can map coloured report rectangles back to Markdown paragraphs and produce a reproducible passage table. Use it only when the report format is compatible and visually confirm representative matches.

Do not repeatedly rewrite until a self-scored detector proxy reaches zero. Repetition can erase voice, weaken evidence, and create a different formula.

## 9. Report the result honestly

When useful, provide:

- the report facts;
- the strongest recurring passage patterns;
- the protected or conventional material that limits what can legitimately be changed;
- what changed between versions and what remains uncertain;
- the reported word-count movement, especially when it rules out a simple compression explanation;
- similarity match categories and integrity flags separately, when a similarity report was supplied;
- the clean revised text or edited file;
- a short fidelity note covering citations, facts, and claim strength.

Use language such as “correlates with”, “is consistent with”, or “suggests”. Do not claim that paragraph length, burstiness, a word blacklist, or any single device caused a detector result.

### Default Mode B delivery

For **learn-and-revise**, deliver:

1. a concise delta diagnosis naming the strongest supported lessons and major uncertainty;
2. the complete revised text or requested artifact;
3. a fidelity note covering protected text, citations, facts, claim strength, and content budget.

For **learn-only**, deliver the evidence-backed workflow lessons and confirm that the document was not changed. For **diagnose-only**, deliver the comparison findings and stopping boundary without a replacement draft.
