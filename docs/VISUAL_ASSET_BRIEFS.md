# Writing Studio visual asset briefs

These briefs define a coherent public visual identity without committing generated binaries to the repository yet. They are ready to paste into Nano Banana. Generate the icon first, then use it as a reference image for the workflow and social-preview assets so the system remains visually consistent.

## Brand direction

Writing Studio should feel editorial, intelligent, calm, and trustworthy. It should not look like a generic AI chatbot, a neon technology product, or a university crest.

### Core visual idea

An editorial mark formed from three ideas:

1. an open manuscript or two facing pages;
2. a precise pen-nib or revision cut;
3. two paths that converge into one clear line, representing Mode A and Mode B.

### Palette

| Role | Colour | Hex |
|---|---|---|
| primary | deep editorial teal | `#315B5A` |
| background | warm paper ivory | `#F5F1E8` |
| text | graphite | `#232826` |
| accent | muted amber | `#D8A657` |
| secondary line | sage grey | `#9BAEAA` |

The visual system should work in light and dark interfaces, at favicon size, and in monochrome.

## Asset 1 — primary app icon

### Nano Banana prompt

```text
Design a premium square app icon for an open-source Codex skill called “Writing Studio”.
Create one distinctive geometric editorial symbol that combines an open manuscript,
a subtle fountain-pen nib, and two revision paths converging into one confident line.
The symbol should communicate evidence-bound writing, careful editing, and iterative learning.

Style: modern editorial design, intelligent and calm, minimal but not generic, strong negative
space, precise geometry, slightly tactile paper quality, flat vector-like construction with very
subtle depth. Use deep editorial teal #315B5A as the dominant colour, warm paper ivory #F5F1E8
as the background, graphite #232826 for a small structural accent, and muted amber #D8A657 for
one restrained highlight. Centre the mark with generous breathing room. It must remain legible
at 32 px and work in monochrome.

No text, no letters, no robot, no human face, no brain, no magic wand, no sparkle cluster,
no chat bubble, no circuit-board pattern, no gradient mesh, no glossy 3D plastic, no neon,
no stock pen-on-paper clip-art, no university crest, no watermark. Output 1024 × 1024 PNG.
```

### Acceptance criteria

- recognisable at 32 × 32 px;
- one central silhouette, not a collection of small objects;
- Mode A / Mode B convergence is implied rather than diagrammed literally;
- no typography or generated pseudo-letters;
- no visual resemblance to a generic chatbot logo;
- sufficient contrast on both warm ivory and transparent backgrounds.

### Deliverables

```text
assets/icon-1024.png      1024 × 1024, warm ivory background
assets/icon-400.png        400 × 400, simplified small-size export
assets/icon-transparent.png 1024 × 1024, transparent background
```

After adding the files, update `agents/openai.yaml`:

```yaml
interface:
  icon_small: "./assets/icon-400.png"
  icon_large: "./assets/icon-1024.png"
  brand_color: "#315B5A"
```

## Asset 2 — workflow overview

The README already contains the canonical Mermaid diagram. The generated illustration is a visual companion, not the source of truth.

### Required information architecture

```text
Writing request
├─ no comparable measured pair → Mode A
│  └─ contract → evidence spine → draft / polish / reconstruct
└─ comparable before/after pair → Mode B
   └─ comparability → passage delta map → ownership classes → supported hypotheses

Mode A and Mode B converge at:
fidelity and quality gates → finished text or artifact

Optional learning loop:
accepted correction → candidate rule → regression case → adjacent-case check
→ promote / narrow / reject
```

### Nano Banana prompt

```text
Create a polished 16:9 editorial workflow infographic for “Writing Studio”, an evidence-bound
writing and revision system. Use a clean left-to-right structure with two clearly differentiated
lanes that merge before delivery.

Top entry: “Writing request”. A decision point asks “Comparable measured pair?”.

Upper lane, Mode A — Direct writing: “Contract” → “Evidence spine” →
“Draft / polish / reconstruct”.

Lower lane, Mode B — Comparative learning: “Verify comparability” → “Map passage deltas” →
“Separate protected and editable text” → “Supported revision hypotheses”.

The two lanes merge into “Fidelity + quality gates” → “Finished text or artifact”.

Below the main flow, show a smaller circular learning loop:
“Accepted correction” → “Candidate rule” → “Regression case” → “Adjacent-case check” →
“Promote, narrow, or reject”. Connect this loop lightly back to the shared workflow, making it
clear that historical reports are optional and not required for Mode A.

Visual style: premium editorial information design, warm paper ivory #F5F1E8 background,
deep editorial teal #315B5A for Mode A, sage grey #9BAEAA for Mode B, graphite #232826 text,
and muted amber #D8A657 only for decision points and accepted learning. Precise grid, generous
white space, rounded rectangular nodes with subtle paper texture, thin consistent connectors,
high legibility, restrained hierarchy, no decorative clutter. Use the supplied Writing Studio
icon as a small title mark if a reference image is provided.

Do not use robots, brains, circuit boards, glowing AI effects, 3D isometric scenes, tiny body
text, tangled arrows, or invented steps. Preserve every label exactly. Output 1920 × 1080 PNG.
```

### Acceptance criteria

- both modes are readable in under ten seconds;
- Mode A remains visibly complete without Mode B;
- the two lanes merge only at the shared revision and fidelity stages;
- the learning loop is secondary and does not look mandatory for every request;
- all labels match the canonical information architecture exactly;
- text remains readable when embedded at approximately 900 px width.

### Deliverable

```text
assets/workflow-overview.png  1920 × 1080
```

Recommended README alt text:

```text
Writing Studio workflow: direct single-draft writing and comparative report learning
converge at shared fidelity gates, followed by an optional correction-to-regression loop.
```

## Asset 3 — GitHub social preview

### Nano Banana prompt

```text
Design a 1280 × 640 GitHub social-preview image for the open-source project “Writing Studio”.
Use the approved Writing Studio icon on the left and a restrained editorial composition on the
right. Include only this exact text:

Writing Studio
Evidence-bound writing. Two modes. One fidelity standard.

Use deep editorial teal #315B5A, warm paper ivory #F5F1E8, graphite #232826, and one muted
amber #D8A657 accent. Create a quiet premium publishing aesthetic with a subtle manuscript grid
and two lines converging into one. Strong typography, generous margins, high contrast, no fake
interface screenshots, no robots, no neon, no excessive gradients, no additional copy, and no
watermark. Output 1280 × 640 PNG with all important content inside a 1120 × 520 safe area.
```

### Deliverable

```text
assets/social-preview.png  1280 × 640
```

Upload this file in GitHub under **Settings → General → Social preview** after visually verifying the exact text.

## Generation order

1. Generate three to five icon candidates from the primary prompt.
2. Select one based on small-size legibility and distinctiveness, not visual complexity.
3. Generate the 400 px and transparent icon variants from the selected reference.
4. Use the selected icon as a reference image for the workflow overview.
5. Use the same icon, palette, and geometry for the social preview.
6. Check spelling, dimensions, contrast, and crop safety before committing binaries.

Keep generated source variants outside the repository. Commit only the selected, compressed deliverables and record the generator and date in the commit message or pull request.
