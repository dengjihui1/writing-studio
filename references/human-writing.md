# Human writing and anti-slop pass

## Purpose

Make prose feel genuinely authored by improving thought, specificity, voice, and movement. This is an editorial pass, not a method for evading AI detectors. Never promise a detector result or report a fabricated AI percentage.

Human writing is not defined by messiness. Do not add typos, grammar errors, random slang, fake hesitation, eccentric punctuation, anecdotes, opinions, or personal details to simulate a person. Preserve accuracy and genre standards.

## 1. Set the calibration level

Choose the lightest level that solves the problem.

- **Light:** already sound prose; remove obvious residue and preserve nearly all structure.
- **Standard:** ordinary drafts and substantial rewrites; inspect structure, voice, specificity, rhythm, and endings.
- **Deep:** heavily templated, uniformly generated, answer-shaped, or high-stakes prose, including a sole first draft with no report or revision history; recover its claims, evidence, limits, and judgements, then rebuild rather than paraphrasing sentence by sentence.

Adjust by genre:

- **Academic:** prioritize evidence boundaries, disciplined qualification, terminological stability, and argumentative continuity. Do not force informality or active voice.
- **Technical:** prioritize exact agents, conditions, sequence, reader tasks, and unambiguous reference. Neutrality can be natural.
- **Business:** prioritize decisions, consequences, ownership, and evidence. Remove executive-sounding abstraction that hides the action.
- **Marketing:** allow energy and compression, but require concrete value and proof; remove empty superlatives and generic aspiration.
- **Essay or blog:** allow a more individual cadence, selective image, opinion, and surprise when supported by the author or brief.
- **Personal writing:** preserve ownership and emotional truth. Never invent biography, dialogue, motivation, hardship, or reflection.

Chinese and English must be judged in their own idiom. Do not translate an English blacklist into Chinese or force English sentence logic onto Chinese prose.

## 2. Build a voice model when evidence exists

Use the user's style guide and two or more representative samples when available. Infer stable tendencies across samples:

- degree of directness and formality;
- sentence span and syntactic complexity;
- common vocabulary level and technical density;
- how the author qualifies, contrasts, exemplifies, and concludes;
- paragraph length and movement;
- punctuation, pronouns, contractions, and rhetorical questions;
- emotional temperature and acceptable humor.

Distinguish voice from accident. Do not reproduce isolated typos, factual errors, copied phrases, inconsistent habits, or quirks that reduce readability. If samples conflict with the required genre, preserve the author's recognizable cadence while honoring the genre's stronger constraints.

Without samples, use a restrained default: concrete nouns and verbs, visible logical relations, varied but controlled rhythm, earned emphasis, and no invented personality.

## 3. Read globally before editing locally

Write a one-sentence account of what the piece is trying to do. Then reverse-outline its paragraphs. Check whether the apparent AI quality actually comes from one of these larger failures:

- the introduction delays the real subject with generic context;
- sections repeat the same claim in different language;
- paragraphs follow identical topic-explanation-summary shapes;
- evidence is listed without interpretation;
- transitions announce logic that the content does not supply;
- the conclusion repeats the introduction or ends in generic uplift;
- every point receives equal weight despite unequal importance.

Repair these problems before replacing words. Sentence-level variation cannot rescue template-level thinking.

## 4. Reconstruct paragraph interiors

Natural long-form prose is not a row of polished mini-essays. It shows thought changing under the pressure of evidence. Before rewriting a deeply templated paragraph, label each sentence by function: claim, evidence, mechanism, qualification, comparison, consequence, or judgement. If the sequence repeats across several paragraphs, redesign the paragraphs rather than disguising the sequence with new transitions.

Give each paragraph a governing question, then make its sentences depend on one another. A sentence should change at least one of these: the evidence, actor, scale, condition, confidence, objection, or consequence. Do not add a summary merely because the paragraph is ending.

Use these diagnostics:

- **Dependency:** a generic sentence that can move anywhere in the section is probably not doing local work.
- **Swap:** adjacent paragraphs that can trade places without consequence form an inventory, not an argument.
- **Seam:** a second setup or mini-conclusion halfway through a paragraph often reveals mechanical merging.
- **Closure:** several consecutive paragraphs ending in fully balanced verdicts create a preassembled cadence.

Vary paragraph function, not paragraph length for its own sake. A case-led paragraph, a mechanism paragraph, a source disagreement, and a decision paragraph will naturally have different shapes. Merge only when two units answer the same local question; split at a real turn in problem, actor, evidence, scale, or direction. A long paragraph containing two independent templates is still mechanical.

For academic and professional prose, authorial presence does not require informality. It can appear through evidence selection, precise source comparison, an explicit limit, attention to who bears a cost, or a local judgement that another informed writer might contest. Use only positions supportable from the supplied material.

Selection is part of voice. Human writers do not normally give every available category equal space merely to demonstrate coverage. Let the central case or difficulty receive sustained attention, introduce background when it becomes necessary, and leave secondary points compressed. Unequal emphasis should reflect the evidence and purpose, not random variation.

Perform a discourse reset as soon as the draft itself shows several adjacent answer-shaped or interchangeable paragraphs; do not wait for a detector result or failed prior rewrite. Set aside the old wording and sentence order, keep a ledger of facts and citations, and rebuild from a case, decision, disagreement, mechanism, or observable consequence. A cluster that survived a substantive rewrite is additional evidence for the same intervention, not the prerequisite for it. Use one recurring case as a spine when it genuinely connects several sections; do not force every paragraph back to it.

After rebuilding paragraphs, audit the section as a unit. Individually polished paragraphs can still produce a mechanical result when each one is self-sufficient. Mark the entry move and final-sentence function of each paragraph. If a run repeatedly uses `summary -> evidence -> qualification -> verdict`, change the allocation of work: let a concrete result or methodological decision open one paragraph, carry its unresolved implication into the next, and allow evidence or a bounded consequence to close where a recap adds nothing. Cross-paragraph dependency must reflect the reasoning, not be staged as artificial suspense.

## 5. Detect high-risk patterns

Treat patterns as prompts for judgment, never as automatic deletion rules.

### Empty importance and abstraction

- inflated claims of significance, transformation, timelessness, or broad impact without support;
- abstract nouns stacked where a concrete actor and action would be clearer;
- vague authorities such as "experts agree," "research shows," or "it is widely recognized" without a traceable source;
- generic superlatives, promotional praise, and prestige by association;
- conclusions that gesture toward a brighter future without stating a consequence, limit, decision, or next action.

### Mechanical structure

- repeated "not X but Y" turns;
- forced groups of three, repeated mini-lists, or symmetrical sentences with no conceptual need;
- identical paragraph openings or sentence frames;
- excessive headings that fragment a continuous argument;
- preview and recap sentences that tell the reader what will be or was said without adding substance;
- transitions chosen from habit rather than cause, contrast, refinement, sequence, or consequence.

### Manufactured profundity or intimacy

- fragments presented as insights when they only restate the preceding sentence;
- a forced final aphorism or slogan;
- fake candor such as announcing honesty, bluntness, or an "uncomfortable truth" without need;
- rhetorical questions that answer themselves or introduce objections no reader raised;
- invented alternatives used only to make the chosen point look decisive;
- false personal detail, sensory description, memory, dialogue, or emotion.

### Chatbot and editorial residue

- meta-commentary about fulfilling the request, revising the text, or being unable to do something;
- greetings, acknowledgements, praise, or offers that belong to the conversation rather than the deliverable;
- placeholder citations presented as real, fake quotations, or unverified specificity;
- excessive headings, bold labels, emojis, or list formatting that the genre did not call for;
- repeated qualifiers, filler clauses, and conclusion phrases that add no information.

### Monotonous movement

- uniform sentence length or repeated clause count;
- every sentence carrying the same emphasis and polish;
- paragraphs ending with summaries rather than implications, evidence, turns, or concrete images;
- sequences of claims with no change in pace around difficult, important, or surprising material.
- repeated claim-evidence-qualification-summary sequences across adjacent paragraphs;
- source-by-source exposition in which every citation receives the same safe gloss;
- long paragraphs created by joining two complete units without rebuilding the seam;
- sustained abstraction with no named actor, operational action, observed consequence, or local decision where the sources provide one.
- prompt-shaped completeness: a paragraph defines, lists, balances, qualifies, and concludes as though answering a rubric in miniature;
- long runs of nominalisations, present-participial add-ons, or coordinated noun phrases that compress actions and obscure who does what;
- conclusions that inventory every earlier section instead of resolving the governing question from a changed vantage point.
- sections made of uniformly self-contained paragraphs, even when the paragraphs use different sentence lengths and vocabulary;
- repeated source-led openings followed by a neutral gloss and a polished closing judgement;
- three or more adjacent paragraphs whose final sentences all summarise or balance the material instead of changing what the next paragraph must do.

## 6. Revise by function

For every flagged feature, ask: what work is this expression doing?

1. **Keep it** if it improves accuracy, evidence calibration, emphasis, rhythm, cohesion, or genre fit.
2. **Replace it** if the function is useful but the expression is canned or vague.
3. **Compress it** if the same work is already done elsewhere.
4. **Rebuild it** if the sentence or paragraph has no clear relationship between claim, evidence, and consequence.
5. **Remove it** if it performs no work.

Prefer substantive fixes:

- name the supported actor, action, condition, or consequence;
- connect evidence to the exact claim it supports;
- integrate a citation according to its actual function rather than giving every source the same summary-and-limitation treatment;
- let a transition express the real relation;
- combine choppy fragments when the thought needs continuity;
- split overloaded sentences at a genuine conceptual turn;
- vary emphasis by importance, not randomly;
- end paragraphs on the point that changes the reader's understanding.
- convert noun-heavy compression into finite clauses when actors, sequence, or responsibility matter;
- replace exhaustive category coverage with the smallest set of evidence needed for the paragraph's local question;
- use a concrete case as connective tissue across a section, while allowing other evidence to interrupt, qualify, or redirect it.
- redistribute explanation across paragraph boundaries when the argument genuinely accumulates; not every paragraph needs its own miniature thesis and conclusion.
- in methods, replace generic claims of suitability with the actual order of work, checks performed, rejected alternatives, remaining constraints, and interpretive consequences.

Do not mechanically ban passive voice, adverbs, dashes, semicolons, long sentences, hedging, parallelism, triads, rhetorical questions, or any individual word. Repetition and marked syntax become problems when habitual, empty, or mismatched to the genre.

## 7. Compare against the source

After revision, check the output against the supplied text, notes, and sources. Verify:

- names, numbers, dates, chronology, quotations, citations, and terminology;
- causal direction and logical scope;
- claim strength, uncertainty, limitations, and attribution;
- personal experience, intention, motivation, and emotional stance;
- requested point of view, register, and audience relationship.

If naturalness conflicts with factual fidelity, fidelity wins. Mark a gap or use a neutral formulation instead of inventing specificity.

## 8. Human-writing scorecard

For internal review, score each dimension from 1 to 5. Revise any dimension below 4 for high-stakes work.

| Dimension | Question |
|---|---|
| Directness | Does the prose reach the real subject without ritual setup or process talk? |
| Specificity | Are claims grounded in the concrete detail actually available? |
| Logic | Can the reader follow why each sentence and paragraph comes next? |
| Movement | Do paragraphs change the state of the argument instead of repeating one internal template? |
| Rhythm | Does movement vary with meaning without becoming mannered or random? |
| Voice | Does the prose fit the author, audience, and genre rather than a universal polished register? |
| Trust | Are claims, uncertainty, attribution, and personal ownership honest? |
| Density | Does each passage perform enough useful work for its length? |
| Selectivity | Does the distribution of detail reveal judgement rather than checklist coverage? |
| Situatedness | Do claims emerge from identifiable cases, actors, decisions, or evidence boundaries where available? |

Do not normally expose the numeric score unless the user requests an audit. Deliver the revised text first.

## 9. Final read

Read the text once for meaning and once aloud or as spoken cadence in the target language. Confirm that no local edit damaged the argument. Stop when the piece is clear, specific, credible, and recognizably situated in its genre; over-editing can erase the author's voice as surely as generic drafting can.
