# MISSION VIVA — QUESTION BANK SCIENTIFIC & EDITORIAL REVIEW

**Review date:** 2026-08-14
**Reviewed build:** `mission-viva.html` after the first Phase 0 repair pass
**Review scope:** Every surviving standalone question prompt, every repeated rubric cue, all topic-specific cues, taxonomy, duplication, safety wording, and question-bank presentation

---

# 1. REVIEW RESULT

The bank has been reduced from the original padded runtime total of 1,600 to:

- **555 reviewed standalone subject/question prompts**
- **535 globally distinct wordings**
- **20 deliberate cross-lane variants**, each linked to its canonical question with `variantOf`
- **36 context-dependent follow-up templates**, separated from the standalone bank
- **178 reviewed topic-specific cues**
- **377 reviewed rubric cues explicitly labelled “not a model answer”**

Current difficulty distribution:

| Difficulty | Count |
|---|---:|
| Core | 336 |
| Deep | 72 |
| Project | 147 |

Current organization distribution:

| Lane | Count |
|---|---:|
| Core | 289 |
| Research/Astronomy | 59 |
| ISRO | 48 |
| BARC/DAE | 56 |
| DRDO | 60 |
| Private Space | 43 |

Current question-kind signals:

| Kind | Count |
|---|---:|
| Concept | 427 |
| Why | 124 |
| Derivation | 4 |

> The original low question-bank derivation count was intentional. The separate Derivation Dojo has since been completed with 50 full derivations.

## Answer-layer implementation addendum

Since this prompt review, four reviewed answer batches have been added:

- **327 curated full-model answer layers**
- **395 question-bank records** resolve to those full models, including reviewed full-layer aliases and cross-lane variants
- **103 additional records** resolve to reviewed deep-sheet answers/outlines through exact or explicit alias links
- **128 human-reviewed semantic aliases** explicitly target a named deep-sheet or curated full layer without automatic fuzzy matching
- **57 records** remain structure-cue-only

Each curated layer contains a short answer, full model answer, assumptions, traps, and five follow-ups. Answer-level scientific acceptance applies to those 327 layers and explicit reviewed aliases only; expansion remains deliberately manual.

---

# 2. WHAT “REVIEWED” MEANS

Every surviving question now carries:

- `reviewStatus: "prompt-reviewed"`
- `reviewedOn: "2026-08-14"`
- `cueReview: "reviewed-specific-cue"` or `"reviewed-rubric-not-model-answer"`
- `variantOf` when the same wording is intentionally retained in another organization lane
- `riskTags` for radiation/nuclear safety or mutable organization context where applicable

The review checked:

1. Whether the prompt is intelligible without an absent parent question.
2. Whether it asks a defensible scientific or interview-relevant question.
3. Whether the cue avoids a clear scientific overclaim.
4. Whether assumptions or measurement dependencies are needed.
5. Whether safety-sensitive wording encourages procedure and authorized supervision.
6. Whether a repeated cue is honestly described as a rubric rather than a model answer.
7. Whether apparent duplicates serve a distinct organization lane.
8. Whether a question improperly counts a generic panel interruption as standalone content.

“Reviewed” does **not** mean:

- The cue is a complete model answer.
- Every question has five deep follow-ups.
- Every formula or derivation has been independently checked.
- Current organization facts have been verified.
- The bank alone meets the Content Master depth standard.

---

# 3. MAJOR EDITORIAL CHANGES

## 3.1 Removed orphan follow-ups from standalone counts

Thirty-six prompts such as these require a parent answer and are not meaningful standalone questions:

- “What happens in the high-temperature limit?”
- “Check the dimensions of the result.”
- “What boundary condition applies here?”
- “What symmetry simplifies this problem?”
- “What approximation would you make first?”
- “Can you solve a simpler limiting version?”

They now live in `FOLLOWUP_TEMPLATES`, grouped as:

- Limiting cases
- Estimation
- Derivation interruptions
- Model criticism
- Units and dimensions
- Boundary conditions
- Symmetry
- Numerical reasoning
- Unfamiliar problem

They can later be attached to a real answer or topic instead of inflating question totals.

## 3.2 Corrected or strengthened 35 prompts/cues

The highest-impact corrections include:

### Optics and EM

- Laser directionality now emphasizes resonator geometry, transverse-mode selection, and diffraction rather than implying stimulated emission alone creates directionality.
- Brewster-angle wording now specifies vanishing reflected p-polarized amplitude and the assumptions behind the index relation.
- Antenna wording changed from “Why are antennas directional?” to “What determines an antenna’s directionality?” because not every antenna is strongly directional.
- Satellite-link wording now asks about link performance as distance increases and points to a complete link-budget structure.

### Semiconductor and materials physics

- Hall-effect wording now states that carrier mobility requires conductivity/resistivity in addition to Hall data and depends on a justified carrier model.
- Band-gap estimation now warns that optical/Tauc estimates are model-dependent and do not universally equal the fundamental band gap.
- XRD cues now include instrument broadening, detection limits, amorphous content, minor phases, and complementary evidence.
- “Can XRD prove purity?” is now “Can XRD alone prove phase purity? Why not?”
- Phase equilibrium now uses equality of relevant chemical potentials and minimization of the appropriate thermodynamic potential.

### Thermodynamics and statistical mechanics

- The Gibbs free-energy criterion now states the closed-system, fixed-temperature, fixed-pressure, pressure–volume-work assumptions and separates spontaneity from rate.
- The Fermi-Dirac cue now uses antisymmetric many-fermion states and Pauli exclusion rather than implying indistinguishability alone is sufficient.

### Quantum and mathematical physics

- Bound-state normalizability no longer implies that normalizability alone is a complete quantization rule.
- The Hermitian-operator cue now mentions domains/boundary conditions and distinguishes formal Hermiticity from self-adjointness.

### Nuclear and radiation physics

- Microscopic cross section is now described as an interaction measure with dimensions of area, not loosely as a probability.
- Moderator wording now includes scattering, parasitic absorption, and dependence on reactor spectrum/fuel.
- Criticality now explicitly uses `k_eff < 1`, `k_eff = 1`, and `k_eff > 1`.
- Activity, absorbed dose, equivalent dose, and effective dose are separated with becquerel, gray, and sievert.
- Irradiation is separated from external/internal radioactive contamination.
- Shielding remains conceptual and points to qualified radiation-safety procedures.
- Suspected-contamination response says not to improvise and to follow facility/radiation-safety-officer procedures.
- Irradiated-material characterization is explicitly restricted to authorized facilities and approved handling.

### Radar and space systems

- Doppler radar wording now specifies line-of-sight relative velocity and the monostatic transverse-velocity limitation.
- “What is radar range?” is now split into pulse-delay measurement and maximum detectable range.
- Geostationary-orbit wording now states circular, equatorial, prograde, and sidereal-day requirements.
- Cryogenic-stage wording now balances potential specific-impulse benefit against density, insulation, boil-off, ignition, turbomachinery, and operations.

### Astronomy

- “What does a telescope measure?” now asks what a complete telescope–detector system measures and includes instrumental convolution and noise.
- Solar-spectrum wording now separates photospheric continuum, opacity, line formation, Doppler/magnetic effects, and instrumental response.

### Experimental/project content

- DSC transition claims now require calibrated, reproducible thermal evidence and corroboration against reaction/decomposition using TGA, cycling, and structural measurements.
- XPS binding-energy interpretation now includes referencing, background/line-shape choices, surface contamination, and final-state effects.
- Hall mobility now explicitly combines Hall and conductivity measurements under a suitable model.
- Propulsion-subsystem testing is framed only within an authorized programme using approved facilities, hazards analysis, instrumentation, abort criteria, and documentation.
- Detector specification questions now begin from mission requirements rather than pretending one specification is universally most important.

---

# 4. AUTOMATED REVIEW GUARDS

`tests/phase0-smoke.js` now checks that:

- Generated drill-number padding does not return.
- Every standalone question has complete metadata.
- Every prompt has editorial review metadata.
- Every cue is labelled as a specific cue or a rubric that is not a model answer.
- The 36 context-dependent follow-ups remain outside the standalone bank.
- Duplicate wording across lanes has a valid `variantOf` link.
- Hall-effect mobility wording retains the conductivity requirement.
- Nuclear cross section retains dimensions-of-area wording.
- The Gibbs criterion retains its closed-system conditions.
- Irradiation/contamination terminology remains corrected.
- Trap and flashcard padding does not return.
- Previously broken handlers still execute in the smoke environment.

Current test output:

```text
555 questions
336 core · 72 deep · 147 project
36 contextual follow-up templates
555 reviewed prompts
250 reviewed distinct traps across 25 categories
800 reviewed factual flashcards
50 concise overviews · 12 complete-v1 deep sheets
360 deep-sheet rapid questions · 36 full derivations
All tested handlers and deep-sheet tab views: OK
```

---

# 5. IMPORTANT REMAINING CONTENT WORK

The editorial review makes the **prompts safer, clearer, and honestly counted**. It does not solve content depth.

## 5.1 Generic cues still need topic answers

The 377 rubric cues are intentionally generic. Examples include:

- State governing physics, assumptions, constraints, and mission relevance.
- Use actual project context and never invent results.
- Connect the model to observable evidence and uncertainty.
- Define requirements, test method, reliability, and confidentiality.

These are useful scoring rubrics but cannot teach the answer. Priority questions need:

- Accurate answer outline
- Full model answer
- Symbols and units
- Assumptions
- Limiting case
- Experiment/application
- Common trap
- Five follow-ups
- Source or review note where appropriate

## 5.2 Taxonomy still needs authored fields

Current metadata is reliable enough for the repaired prototype, but final content should author rather than infer:

- Difficulty
- Question kind
- Topic/subtopic
- Prerequisites
- Organization relevance
- Project relevance
- Expected answer duration
- Numerical/derivation requirements
- Safety/provenance tags

## 5.3 Scientific review must continue with model answers

Prompt-level review is complete for this seed bank, and 327 full-answer layers plus 50 Dojo derivations have since passed their first scientific-content review. Every additional answer or derivation batch must still check:

- Equations and sign conventions
- Dimensions and units
- Boundary/initial conditions
- Experimental limitations
- Numerical scales
- Safety
- Sources for mutable facts
- Whether the answer actually addresses the prompt

## 5.4 Current organization content remains unverified

Questions about ISRO, BARC/DAE, DRDO, IIA, IUCAA, CSIR, and private space are training prompts. No current programme, centre, recruitment, eligibility, or mission fact becomes trusted merely because the prompt is reviewed.

Those answers still require official sources and verification dates.

---

# 6. EDITORIAL ACCEPTANCE DECISION

The seed question bank now passes **prompt-level editorial acceptance** with these restrictions:

- It is a **555-prompt reviewed seed bank**, not a 1,500-question complete forge.
- Repeated rubrics are **not model answers**.
- Context-dependent interruptions are **not standalone questions**.
- Cross-organization duplicates are linked variants, not hidden duplication.
- Radiation/nuclear and mutable-organization prompts carry risk context.
- Full answer-level scientific acceptance is delivered for 327 curated layers; runtime aliases extend reviewed coverage, while 57 records remain cue-only.

> The question bank is now honest enough to build upon. The next content step should deepen the highest-priority subject sheets and replace generic rubrics with scientifically reviewed answer layers—not increase the counter again.
