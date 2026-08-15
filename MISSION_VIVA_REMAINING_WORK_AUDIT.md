# MISSION VIVA — REMAINING WORK & QUALITY AUDIT

**Audit date:** 2026-08-14
**Repository baseline:** `ff5d65b7b86684aed2076a1f4d621e4babb61409`
**Audited files:**

1. `MISSION_VIVA_PLAN.md`
2. `MISSION_VIVA_MASTER_UPGRADE_PLAN.md`
3. `MISSION_VIVA_CONTENT_MASTER.md`
4. `mission-viva.html`

> This is the consolidated source of truth for what remains. It distinguishes a feature that merely appears in the interface from one that is complete, reliable, and deep enough for interview preparation.

---

# 1. EXECUTIVE VERDICT

MISSION VIVA currently has a useful **visual prototype and broad feature scaffold**, but it is not yet a dependable interview-readiness system. The largest problem is that the HTML repeatedly reaches numerical targets by generating labels or placeholders rather than delivering substantive content.

The current build should be classified as:

- **Shell/UI:** usable prototype
- **Core runtime:** first repair pass complete; smoke-tested, but full real-browser QA remains
- **Content breadth:** many overview headings plus all twelve priority complete-v1 deep sheets
- **Content depth:** 12 of 12 priority sheets meet the complete-v1 schema; advanced and project-specific extensions remain
- **Question quality:** 555 prompt-level reviewed questions; 253 records resolve to 200 full models, 89 records resolve to deep-sheet answers through exact or reviewed-alias links, and 213 records remain cue-only
- **Progress/readiness evidence:** local evidence events now exist, but independent correctness validation remains limited
- **Project personalization:** structured 25-field truth ledger, status-aware pitch generator, tailored questions and board implemented; actual project facts are still required
- **Organization/current-affairs content:** twenty-four source-backed dossiers with 54 official links and stale/check-required states, including six company-specific Bengaluru/private-space profiles; mutable mission/recruitment facts still require current checks
- **Voice/AI:** optional provider adapter hardened with policy, timeouts, limits, structured reviews, and kill switch; real provider connectivity still depends on user endpoint/key, CORS, quota, and current provider API
- **Accessibility, privacy, and QA:** first accessibility/reliability hardening pass delivered; canvas alternatives, screen-reader/zoom validation, endpoint hardening, and full real-browser QA remain

The app no longer presents the old padded totals as completion. It now distinguishes reviewed prompts, factual flashcard seeds, concise overviews, contextual follow-ups, and complete-v1 deep sheets.

## Immediate release recommendation

**Do not call the entire system interview-ready yet.** The repaired runtime and all twelve priority deep sheets are suitable for structured practice, but confirmed project facts, answer/dossier expansion, advanced accessibility validation, and final browser QA remain.

## Implementation progress — 2026-08-15

### Latest autonomous upgrade batch

This dated block supersedes older numeric snapshots later in the historical audit:

- Expanded reviewed answer coverage to **200 full-model layers** and **101 explicit semantic aliases**. Runtime coverage is now **253 full-model · 89 deep-sheet · 213 cue-only** across 555 records.
- Completed the original **100-diagram target**: 36 complete-v1 sheet diagrams plus 64 source-controlled original extensions, each with speaking guidance and a five-point comparison checklist.
- Completed and exceeded the original **100-resource target** with **114 unique links**. The 22 reviewed study extensions include level, learning mode, expected use, check date, scope, and stable URL; new company sources increased the deduplicated total further.
- Expanded Signal Watch to **24 dossiers and 54 official source links**, adding source-backed records for Pixxel, Bellatrix Aerospace, Digantara, GalaxEye, KaleidEO, and SatSure. No salary or unverified vacancy claim was added.
- Added a persistent **Revision Queue** with next-review dates for self-identified weak answers, missed traps and formulae, and failed derivation steps. Mission Control routes due corrections.
- Cross-linked all 153 formula records to a topic derivation, limiting-case prompt, worked numerical, experiment/application, and matching equation SRS card.
- Added SRS daily limits, leech detection, suspend, and bury controls.
- Upgraded drawings with line, arrow, rectangle and ellipse tools, local drag/drop or camera image input, PNG export, reference-hidden practice, label toggling, and side-by-side comparison.
- Added strict structured vision-review JSON, a visible image payload preview, and natural-TTS endpoint/timeout/size/MIME/cancellation safeguards with browser-voice fallback.
- Added real mid-answer interruption events for applicable stress modes, project version snapshots/review export, Pre-flight emergency/accommodation/calendar controls, Exam Bridge weekly history, data-class deletion, and workload settings.
- Published build manifest **2.4.0 release-candidate**. The exact self-contained HTML passes the expanded zero-dependency smoke/schema battery.
- Split maintainable shell, CSS, and JavaScript into `src/`, added deterministic self-contained build/reproducibility checks, a documentation JSON Schema, and a zero-dependency cross-source validator.
- Added target-specific local evidence maps, dossier-to-topic fit maps, target/role boards, declared-subject follow-up ladders and state recommendations, and semantic near-duplicate avoidance in boards.
- Added deep-sheet failure routing, dedicated wrong-answer correction, reviewed factual-coverage self-checks, and user-authored simple/specialist answer revisions.
- Added repeated-phrase/weak-ending signals, duration-specific pace bands, breathing/delivery checks, consent-based in-memory audio playback, hold-to-talk, resumable live rooms/post-mortems, and eight live scoring lanes.
- Added per-project-field and per-organization-fact provenance browsers, 30-day manual current-fact cards, a 14-day SRS forecast, weakest trap-category routing, and derivation-to-visual links.

Still blocked or intentionally incomplete:

- **213 cue-only prompts** still need individually reviewed full layers or explicit aliases; no fuzzy auto-linking is permitted.
- Actual project material, route, parameters, hazards, instruments, contribution, observations, and next experiment remain unknown until supplied by the user.
- **0 source checks are currently due** after the 2026-08-15 official-link refresh; mutable sources still expire after 30 days and must be refreshed near use.
- Real screen-reader, zoom, forced-colour, stylus/touch, microphone, SpeechRecognition, print, and device testing requires external browsers/devices; no browser runtime is installed in this repository environment.
- Real provider AI/vision/TTS operation still requires a user-supplied session key or local endpoint, current model access, quota, and browser CORS. Mocked paths pass; no cloud provider is bundled or claimed verified.
- Advanced atomic/molecular, astronomy, radar/microwave, fluid/chaos, many-body/open-system, and other role-specific complete-v1 sheets remain optional extensions, to be prioritized only against a confirmed role need.

Phase 0 repair and subsequent depth work delivered:

- Implements the six previously undefined Project, HR, and Dossier handlers.
- Removes the duplicate `drill()` override and restores timed, voice, review, stress, and AI-assisted drill controls.
- Fixes the Answer Coach organization-lens crash.
- Builds metadata after all question batches and keeps `QUESTION_STATS` synchronized.
- Removes generated drill-number padding and separates orphan follow-ups, leaving **555 reviewed standalone subject/question prompts** plus **36 contextual follow-up templates**.
- Removes the original 250 numbered copies, preserves the 25 valid categories, and then expands them into **250 reviewed, meaningfully distinct trap/recovery records**.
- Replaces all 800 placeholders with **800 reviewed factual cards**: 180 definitions, 153 equations, 118 trap recoveries, 50 derivation summaries, 157 balanced rapid answers, 122 manual deep-sheet cards, and 20 foundation seeds.
- Enables Content Library search and full-bank question browsing.
- Completes **all twelve priority complete-v1, 16-tab deep sheets**, ending with Orbital Mechanics, Spacecraft Systems, and Remote Sensing.
- Adds 360 rapid questions, 120 intermediate questions, 60 deep questions, 60 worked numericals, 36 full derivations, 36 original reference SVGs, oral scripts, experiment matrices, traps, resources, and evidence-based readiness gates across those sheets.
- Stores the maintainable deep-sheet source in `content/deep-sheets.json` and reproducibly inlines it with `scripts/sync_deep_sheets.py`.
- Adds a 25-field project truth ledger across identity, synthesis, characterization, and evidence groups.
- Labels every project field `unknown`, `planned — not done`, `confirmed/user-entered`, or `not applicable`.
- Generates 30-second, 90-second, 3-minute, and non-specialist pitches only from status-labelled local fields.
- Generates tailored cross-questions and a project-only board without inventing missing material, method, instrument, result, or contribution facts.
- Implements local Again/Hard/Good/Easy spaced repetition with due queues, intervals, ease, repetitions, lapses, bounded history, legacy migration, immediate undo, Mission Control routing, and card-type-filtered sessions across the complete 800-card deck.
- Adds 200 reviewed full-model answer layers across seven batches, all twelve priority topics, atomic/astronomy extensions, HR/officer/project/research/teamwork, experimental design, and organization lanes, each with a 30-second answer, full explanation, assumptions, traps, and five follow-ups.
- Indexes 598 authored deep-sheet answer/outline/numerical records, keeps exact matching, and adds 40 explicitly human-reviewed semantic aliases rather than trusting automatic fuzzy matching.
- Adds Answer Coach status filters (`full model`, `deep answer`, `cue only`), reveal-after-attempt behavior, and locally saved draft history.
- Adds twenty-four source-backed organization/company dossiers with 72 stable fact statements and 54 official source links, stable/mutable labels, stale/check-required logic, manual local recheck evidence, search/type filters, and organization-specific interview drills.
- Adds skip navigation, accessible names/tooltips, semantic modal behavior, Escape/backdrop close, focus trap/restore, app inerting, visible keyboard focus, short-viewport rail scrolling, calm and high-contrast themes, reduced-motion handling, and print styles.
- Adds reusable drawing tools with draw/erase, colour/width, labels, undo/redo, clear confirmation, accessible text alternatives, diagram checklists, persistent evidence, and equivalent live-room controls.
- Adds validated backup import with format/version/size checks, forbidden-credential rejection, prototype-key filtering, safe replacement, and export object-URL cleanup.
- Hardens startup errors against HTML injection and makes storage-write failures visible instead of crashing silently.
- Upgrades Sparring Hall with actual board deadlines, mini/30/45/60-minute modes, six rotating personas, answer timing/communication metrics, progressive stress profiles, and saved five-category board post-mortems.
- Adds local communication trends for WPM, filler signals, hedging, sentence length, clear endings, and 30/60/90/120-second practice modes while stating metric limitations.
- Replaces static Mission Control with adaptive next action, weakest-three evidence signals, due-memory/project/source/board/exam/pre-flight planning, active target countdowns, and last-session routing.
- Adds five editable organization target profiles, a persistent Exam Bridge with mistake-to-oral-drill conversion, and target-scoped D-30/D-14/D-7/D-1/morning Pre-flight checklists and logistics.
- Adds a four-state declared-subject strategy across all twelve priority topics and a 153-record Formula Vault with active recall and persistent known/missed evidence.
- Adds nine Bengaluru/private-space role families, six company-specific records, a visible Evidence Ledger, a 114-link source-aware Resource Library, and expands organization coverage to twenty-four source-backed dossiers.
- Upgrades the Live Room with 5/15/30/45/60/90/custom durations, start/stop microphone, voice timeout, editable transcript, answer timing/metrics, pause/mic-event logs, drawing text alternatives, and saved post-mortems.
- Hardens the optional AI adapter with HTTPS/local-endpoint policy, session-only credentials, explicit permissions, 5–120 second timeouts, 8–512 KB response caps, active cancellation, HTTP/malformed-response errors, strict review JSON validation, visible network state, and a kill switch.
- Consolidates the 36 deep-sheet derivations with 14 reviewed extensions into a complete 50-item Derivation Dojo with ladder reveal, error-location history, attempts, pass evidence, search/status filters, and print mode.
- Delivers a 250-item Trap Radar across 25 categories with unique wrong statements/recoveries, rationale, follow-up, severity/tags, active-recall reveal, caught/missed history, and timed trap-to-question drills.
- Replaces the fabricated readiness percentage with a local evidence-event score and calendar-day streak.
- Saves timed-answer reviews, board answers, speaking drills, flashcard reviews, topic-review dates, and live post-mortems.
- Replaces unsafe grade-oriented project wording with truth-preserving professional wording.
- Removes persistent API-key storage and adds explicit online, transcript, project, and image permissions.
- Removes the injected Cloudflare iframe/network script.
- Adds `tests/phase0-smoke.js` to check padding, metadata, handlers, duplicate declarations, privacy invariants, and major module actions.

Latest smoke-test result:

```text
555 questions · 336 core · 72 deep · 147 project
36 contextual follow-up templates · 555 prompt-level reviews
250 reviewed traps across 25 categories · 800 reviewed factual flashcards · 50 concise overviews
12/12 complete-v1 deep sheets · 360 rapid · 120 intermediate · 60 deep
60 numericals · 36 deep-sheet derivations · 50 complete Dojo derivations · 100 original reference diagrams
All tested handlers and all 32 deep-sheet tab views: OK
```

Prompt-level scientific/editorial review is complete and documented in `MISSION_VIVA_QUESTION_BANK_EDITORIAL_REVIEW.md`. The 12/12 priority depth build, structured project engine, SRS v2, 200 full-model answer layers, 100-diagram library, and twenty-four source-backed organization/company dossiers are delivered. Release work is **not closed yet**: 213 bank records remain cue-only, user-confirmed project facts are missing, mutable sources still require near-use refresh, and full real-browser/device QA is still required.

---

# 2. WHAT IS ACTUALLY IMPLEMENTED

The following work is real and should be retained rather than rebuilt blindly:

- A single self-contained HTML shell with no external JavaScript or CSS libraries.
- A coherent dark command-center visual direction and responsive two-breakpoint layout.
- Navigation for most planned modules.
- Local progress/settings storage, v1-to-v2 migration, JSON export, and reset.
- A broad starter collection of physics and organization-oriented question wording.
- Fifty concise topic **overview cards** covering a wide range of physics and engineering areas.
- Three complete-v1 deep sheets with a maintainable JSON source, 16-tab UI, and evidence gates.
- Search/filter UI across the full reviewed question bank.
- A deterministic five-level why-chain.
- A basic full-board question sequencer.
- Browser speech synthesis and browser speech-recognition fallbacks.
- Optional AI endpoint configuration and several provider presets.
- A live-room prototype with a timer, transcript capture, drawing canvas, image attachment, and optional follow-up generation.
- Strong honesty language around unknown answers, project results, leaked questions, and selection guarantees.
- A useful early collection of project-instrument questions, especially for XRD, SEM, TEM/EDS, Raman/FTIR, UV-Vis, XPS, thermal, electrical, and magnetic characterization.
- Node’s syntax check passes for the main JavaScript. The primary problems are runtime behavior, data quality, and incompleteness rather than a top-level syntax failure.

These are foundations, not finished modules.

---

# 3. MEASURED REALITY OF THE HTML

## 3.1 Headline counters versus substantive content

| Area | Current count/state | Substantive audit | Verdict |
|---|---:|---:|---|
| Questions | 555 reviewed standalone subject/question prompts | 535 globally distinct wordings, 20 linked cross-lane variants, and 36 separate contextual follow-ups | Prompt-level editorial review complete |
| Answer layers | 200 curated full-model layers | 253 question-bank records resolve to full models across core, project, characterization, atomic/astronomy, experimental design, HR/officer/research/teamwork, ISRO, BARC/DAE, DRDO, and private-space lanes; every layer has short/full answers, assumptions, traps, and five follow-ups | Seven reviewed batches delivered |
| Deep-sheet exact answer links | 598 indexed authored records | 25 question-bank records match exactly after curated full layers take precedence | Honest exact-link integration |
| Reviewed semantic aliases | 101 human-reviewed mappings | They cover alternate bank wording through an explicit deep-sheet or curated-full target and rationale; 61 new mappings reduce cue-only backlog without fuzzy attachment | No automatic fuzzy matching |
| Cue-only bank records | 213 | Clearly labelled as structure cues rather than scientific model answers | Largest remaining answer-depth backlog |
| Questions with metadata | 555 of 555 | Metadata is generated after all batches and includes review/cue/variant/risk fields | P0 data-pipeline fault resolved |
| Difficulty metadata | 336 core · 72 deep · 147 project | Current classification works, but authored enum metadata is still preferable | Functional first pass |
| Traps | 250 | 250 unique wrong statements and trap/recovery pairs across 25 reviewed categories; each has rationale, follow-up, severity, tags, and review date | 250/250 target delivered |
| Flashcards | 800 | 20 foundation seeds, 122 manual deep-sheet cards, and 658 generated-from-reviewed-source cards across definitions, equations, traps, derivations, and rapid answers; all participate in SRS | 800/800 target delivered |
| Complete-v1 deep sheets | 12 of 12 | All priority foundations through Orbital Mechanics, Spacecraft Systems, and Remote Sensing; roughly 50,500 words | Priority depth target delivered |
| Concise overviews | 50 | 5,743 words total; about 115 words per overview; clearly separated from deep sheets | Useful index; most still require depth builds |
| Required topic fields | 16 per Content Master | All twelve priority sheets render all 16 tabs; overview-only extension topics retain 9 short fields | 12/12 priority target complete |
| Derivations | 50 complete Dojo items | 36 deep-sheet derivations plus 14 reviewed extensions; every item includes assumptions, at least five steps, interpretation, unit check, mistake, interruption, and summary | 50/50 target delivered |
| Diagrams | 100 original reference SVGs | 36 complete-v1 sheet diagrams plus 64 role/core extensions; every item has a speaking script and comparison checklist | Original 100-reference target delivered |
| Resources | 114 unique links | Deduplicated deep-study links, 22 metadata-complete reviewed study extensions, 54 official organization/company sources, and 4 general catalogues | Original 100-link target delivered and exceeded without duplicates |
| Organization dossiers | 24 source-backed profiles | 72 stable fact statements and 54 official source links, including six company-specific Bengaluru/private-space profiles; all 54 sources checked on 2026-08-15, with mutable entries retaining 30-day expiry | Three sourced dossier batches delivered |
| Live-mode banks | 6 modes | 2 seed prompts per mode plus deterministic local follow-ups | Prototype only |

## 3.2 Content-depth evidence

The 50 objects called `FULL_SHEETS` contain these average field sizes:

- One-minute core: **14 words**
- Definitions: **10.5 words**
- Equations: **5.8 words**
- Theory: **20.5 words**
- Assumptions: **12.1 words**
- Trap: **17.3 words**
- Drawing prompt: **9 words**
- Panel questions: **15.6 words**
- Applications: **10 words**

This is not enough to teach a topic from first principles, support a derivation, show limiting cases, explain experiments, or prepare five layers of follow-up questions. The “one-minute core” is usually one sentence; the “theory” is often two sentences; the “equations” are unannotated formula signals.

A complete topic sheet must not be counted merely because all nine object keys are non-empty.

The new `DEEP_SHEETS` collection is separately validated. All twelve priority topics contain all 16 rendered tabs, 30 rapid questions, 10 intermediate questions, 5 deep questions, 5 numericals, 3 full derivations, 3 reference diagrams, spoken versions, technique/experiment sections, flashcards, resources, and evidence gates per sheet.

## 3.3 Question-to-topic mismatch

The legacy overview-to-question matcher still uses loose string inclusion. Of the 50 overview records:

- **18 topics have zero matching legacy-bank questions.**
- **26 topics have fewer than three matching questions.**
- The repaired UI now reports the gap instead of silently substituting unrelated global questions.
- The twelve complete-v1 deep sheets use authored topic-specific rapid, intermediate, deep, numerical, and derivation sets and do not depend on this matcher.

Examples still lacking matched legacy questions include Scientific Computing, Fluid Mechanics, Plasma Physics, Particle Physics, Special Relativity, Vacuum and Cryogenic Basics, Rocket Propulsion, Astrophysics, Superconductivity, Microwave Engineering, General Relativity Basics, and Advanced Data and Statistics.

---

# 4. P0 — BROKEN OR MISLEADING BEHAVIOR TO FIX FIRST

These items block reliable use and must be completed before more content counters are added.

## 4.1 Six undefined button handlers — **Resolved in first repair pass**

The interface renders buttons that call functions that do not exist:

- `pitch()`
- `projectQuestions()`
- `projectBoard()`
- `hrAnswer()`
- `scenario()`
- `dossier()`

Consequences:

- Every Project Lab action is broken.
- Every HR & Officer Craft action is broken.
- Every Signal Watch dossier action is broken.

**Acceptance:** automated navigation tests must click every visible action without producing a console error.

## 4.2 Duplicate `drill()` declaration disables the real drill — **Resolved in first repair pass**

There are two declarations named `drill`. The later simplified declaration overrides the earlier timed/voice/review version.

This breaks or removes:

- Two-minute timer
- Rapid-fire timer
- Stress timer
- Voice answer button
- Finish-and-review workflow
- AI answer analysis button
- Structure post-mortem

`stress()` then tries to write to a `voiceStatus` element that the overriding drill does not create, causing another runtime error.

**Acceptance:** retain one drill controller, and test quick, rapid, stress, voice-disabled, voice-enabled, offline, and AI-assisted paths.

## 4.3 Answer Coach has a runtime error — **Resolved in first repair pass**

`answerCoach()` accesses `MODEL_ANSWERS.org[...]`, but `MODEL_ANSWERS.org` does not exist. The available key is `organization` and it is a string, not an organization map.

**Acceptance:** organization lenses must be represented by an explicit object and every question’s Answer Coach must open successfully.

## 4.4 Question QA crashes on the last 100 questions — **Resolved in first repair pass**

One hundred instrumentation questions are appended after metadata generation. `questionQA()` later assumes `x[3].org` exists for every record and throws while calculating coverage.

Related faults:

- `QUESTION_STATS.total` remains 1,500 while the runtime bank contains 1,600.
- IDs stop before the last 100 records.
- The final 100 cannot participate safely in metadata-dependent features.

**Acceptance:** build all data first, then normalize and validate every record once. Reject the build if any ID, subject, organization, difficulty, kind, answer, or provenance field is missing.

## 4.5 Difficulty classification is completely wrong — **Functional first pass; schema refinement remains**

The code lowercases the search text and then checks it against capitalized strings such as `Advanced`, `Research`, `Project`, and `Rapid`. Those checks never match. As a result:

- First 1,500 questions are marked `core`.
- Zero are marked `deep`, `project`, or `rapid` by that classifier.
- Last 100 have no difficulty.

**Acceptance:** use controlled enum fields authored in the source data; do not infer important metadata from display strings.

## 4.6 Content search is inert — **Search resolved; advanced filters remain**

The Content Library displays a search input but has no search handler. It also has no difficulty, organization, mode, or prerequisite filters.

**Acceptance:** search must filter titles and all topic content; all specified filters must work from keyboard and pointer input.

## 4.7 Question browser exposes only 300 records — **Resolved in first repair pass**

The browser renders `q.slice(0,300)`. Search and filters therefore cannot browse the remaining 1,300 questions, even though the count says 1,600.

**Acceptance:** implement pagination or virtualized rendering across the complete validated bank.

## 4.8 Progress can be farmed and readiness can exceed reality — **Core exploit resolved; evidence model remains provisional**

The dashboard’s evidence model is not valid:

- Readiness starts at 42% and adds 3% for each checked task.
- The same task can be repeatedly checked after the dashboard rerenders.
- Readiness can exceed 100%.
- “Streak days” increments per checked task, not per day.
- Radar values are hardcoded at 35%, 28%, 22%, and 15%.
- Final gates use weak proxies such as two task checks or one board.
- Topic progress is granted by clicking “Mark studied,” with no oral check.
- Speaking drills close without recording evidence.
- Full-board answers are discarded.
- Live-room self-score sliders are not saved.

**Acceptance:** readiness must be derived from immutable evidence events: dated attempts, answer scores, derivation results, SRS reviews, project checks, and full-board performance. Clamp percentages to 0–100 and calculate streaks by unique calendar day.

## 4.9 Unsafe project framing is displayed — **Resolved in first repair pass**

The default project profile says the project was:

> “Chosen as a feasible, grade-supportive project while protecting preparation time for GATE and CSIR-NET.”

This conflicts with the Master Upgrade Plan’s instruction not to make the project sound like a low-effort or grade-driven choice. It is risky language to rehearse or expose in a project panel.

**Acceptance:** use the approved professional framing from the Master Upgrade Plan and keep private planning rationale separate from interview-facing copy.

## 4.10 Remove the injected Cloudflare script — **Resolved in first repair pass**

The final HTML contains a hidden-iframe Cloudflare challenge script that requests `/cdn-cgi/challenge-platform/...`.

This:

- Violates the stated offline/no-network core.
- Is unrelated to MISSION VIVA.
- Adds an unexplained hidden iframe.
- Suggests the HTML was saved from a served page rather than produced from a clean source.

**Acceptance:** a network audit of offline mode must show zero requests.

---

# 5. MODULE-BY-MODULE REMAINING WORK

Status meanings:

- **Missing:** no meaningful implementation
- **Broken:** interface exists but primary action fails
- **Shallow:** works only as a minimal demonstration
- **Partial:** useful subset exists but acceptance requirements are not met

## A. Mission Control dashboard — **Adaptive evidence planner v1 delivered**

Delivered:

- Replaced fabricated readiness and hardcoded radar values with explicitly labelled training-evidence signals.
- “Do this now” action generated from project unknowns, due SRS cards, weakest local skill, board-day gate, stale organization sources, Exam Bridge weakness, and a target within 30 days.
- Weakest-three signals across technical answers, structure, composure/recovery, project ledger, deep-sheet evidence, SRS, organization sources, and speaking repetitions.
- Five active-target cards with priority, post/route, editable date, and countdown.
- Full adaptive-plan list with reason and direct module action.
- Resume/review-last-session routing.
- Dashboard counts for reviewed prompts, deep sheets, full answers, cards, dossiers, and boards.

Remaining:

- Mission Control now displays “no evidence yet” instead of 0% mastery and shows sample counts plus an approximate 95% range for recent self-score signals. Independent correctness estimates remain unavailable.
- Target-specific local evidence coverage plus communication/project evidence trend charts are delivered across topic, source, project, target-board, answer, and snapshot signals.
- Resume routing now prioritizes an in-progress board, resumable live room, or unsaved live post-mortem before completed-session history.
- User-configurable daily plan minutes, SRS limits, and a 30-day daily-plan snapshot/rollover history are delivered.
- Validate that generated priorities remain useful during real multi-week use.

## B. Personal profile and target manager — **Editable target profiles v1 delivered**

Delivered:

- Editable target cycle and five target profiles: ISRO, BARC/DAE, DRDO, Private Space, and Research Institutes.
- Per-profile active state, organization label, post/route, primary/secondary/exploratory priority, and interview/application date.
- Target cards and countdowns feed Mission Control and target-scoped Pre-flight.
- User-entered planning dates are explicitly separated from official notification facts.
- Existing degree, institution, home/preferred city, declared-subject text, project-linked subject, and project summary remain editable.

Remaining:

- Declared, prepared, survival, and do-not-declare states are delivered and synchronize the legacy favourites field.
- Planning-only confidence, weekly available hours, and preferred private-space role-family fields are delivered.
- Different topic emphasis and local evidence-coverage formulas are delivered for ISRO, BARC/DAE, DRDO, private-space, and research profiles.
- Project pitch target lenses and dossier-backed technical-fit wording are delivered; mutable role facts remain source-gated.
- Complete escaping review for every remaining legacy `innerHTML` path.

## C. Subject Armory — **Priority depth target delivered: 12 of 12 complete-v1 sheets**

Delivered:

- The original 50 short objects are explicitly labelled concise overviews.
- All twelve priority topics implement the full 16-tab deep-sheet UI.
- All twelve include prerequisites, defined equations with units/conditions, derivations, limiting cases, experiments, applications, question ladders, traps, spoken versions, reference SVGs, derive-it plans, flashcards, resources, and readiness evidence.
- Each includes 30 rapid, 10 intermediate, 5 deep, 5 numerical, and 3 derivation exercises.
- Readiness requires unique self-recorded evidence by category and is explicitly not presented as independent correctness validation.

Remaining:

- Build only advanced or role-specific extension sheets after the priority core.
- An accessible SVG prerequisite graph and text alternative now connect the twelve priority sheets.
- Deep-sheet “needs revision” outcomes now remove the self-pass, schedule a shared correction item, and feed Mission Control when due.
- Add peer/teacher/AI-reviewed correctness evidence in addition to self-recorded passes.
- Expand project links after the actual material and methods are confirmed.

### First 12 complete sheets to build

1. Units, vectors, mathematical methods, data, and uncertainty — **complete-v1 delivered**
2. Classical mechanics and oscillations — **complete-v1 delivered**
3. Electromagnetic theory — **complete-v1 delivered**
4. Optics and lasers — **complete-v1 delivered**
5. Thermodynamics — **complete-v1 delivered**
6. Statistical mechanics — **complete-v1 delivered**
7. Quantum mechanics — **complete-v1 delivered**
8. Basic electronics and instrumentation — **complete-v1 delivered**
9. Solid-state physics — **complete-v1 delivered**
10. Materials characterization and experimental claim design — **complete-v1 delivered**
11. Nuclear physics and radiation protection — **complete-v1 delivered**
12. Orbital mechanics, spacecraft systems, and remote sensing — **complete-v1 delivered**

All twelve priority complete-v1 deep sheets, structured project engine, SRS v1, first answer/dossier batches, and first accessibility/reliability hardening pass are delivered. Next work should expand coverage and complete real-browser release QA.

## D. Declared-subject strategy — **Four-state evidence strategy delivered**

Delivered:

- Four explicit states for every priority topic: declared favourite, prepared but not declared, survival basics, and do not declare yet.
- Defaults preserve Optics, Thermodynamics, and Basic Electronics as declared; Solid State and Materials Characterization as prepared.
- All twelve complete-v1 sheets appear in the strategy manager.
- Each subject shows rapid/intermediate/deep/numerical/derivation volume and its complete readiness gate.
- Declared subjects without all evidence gates display a warning and are not counted ready.
- Strategy changes persist in the profile and evidence history.

Remaining:

- Five-level subject-specific ladders now select unpassed rapid, intermediate, deep, numerical, and derivation-interruption items.
- Evidence-based state recommendations are delivered and always require explicit user confirmation.
- Target-profile-specific priority advice and declared-without-evidence warnings are delivered; richer imported-settings age checks remain optional.

## E. Sparring Hall — **Functional practice engine v2; automated evaluation remains**

Delivered:

- One stable drill controller for two-minute technical, 60-second rapid, five-level why-chain, and stress practice.
- Actual continuing deadlines for mini 5-minute and 30/45/60-minute boards.
- Organization-filtered, mixed, and personalized project boards with category balancing.
- Six rotating personas: Fundamentalist, Sniper, Skeptic, Project Specialist, Organization Officer, and Mentor.
- Every board answer stores question ID/text, answer, elapsed seconds, word/pace/filler/sentence metrics, board timing, and timeout state.
- Board post-mortem separately records technical depth, structure, composure, recovery, and honesty.
- Board and review histories are bounded locally and feed evidence/readiness gates.
- Active boards and unsaved post-mortems persist locally and can be resumed after navigation/reload; state clears only after evidence is saved.
- Timed-out boards finish safely and retain captured answers.

Remaining:

- Reviewed factual-coverage checklists are delivered separately from communication scoring, but remain self-recorded rather than independent grading.
- Dedicated three-step wrong-answer correction and subject deep-dive ladders now save retries and next-revision dates.
- Board composition now balances difficulty/category and rejects high-overlap semantic near-duplicates where the pool permits.
- Consent-based local recording now measures approximate quiet pauses with an explicit amplitude/threshold heuristic; real-device calibration and SpeechRecognition pause timing remain external.
- Complete three-board separate-day validation in real use.

## F. Answer Coach — **Functional layered coach; coverage expansion remains**

Delivered:

- Fixed organization-lens routing and retained technical, project, HR, and unknown-answer frameworks.
- Added 200 reviewed full-model layers in seven batches spanning all twelve priority topics plus atomic/astronomy, project, characterization, experimental design, HR/officer/research/teamwork, ISRO, BARC/DAE, DRDO, and private-space lanes.
- Each curated layer contains a 30-second answer, full model answer, assumptions, traps, five follow-ups, topic, review date, and stable ID.
- Indexed 598 deep-sheet concise answers, outlines, and worked numericals for exact-match reuse.
- Added 101 human-reviewed semantic aliases linking alternate wording to a specific deep-sheet or curated full-layer target; no automatic fuzzy match is trusted.
- Exact and reviewed-alias deep links now cover 89 bank records after curated full models take precedence.
- Explicit statuses: reviewed full model, reviewed deep-sheet answer, and structure cue only.
- Question Bank can filter by answer status and shows coverage before opening a card.
- Answer layers stay hidden until the user attempts and presses Reveal.
- Drafts are saved locally with question ID, answer status, timestamp, word count evidence, and bounded history.
- Source JSON is hash-synchronized into the self-contained HTML.

Remaining:

- Expand reviewed full-model or explicitly reviewed alias coverage; 213 bank records remain cue-only.
- Factual-coverage checklists now use reviewed assumptions/traps separately from communication scores; independent grading remains external.
- User-authored plain-language and rigorous-specialist revision editors are delivered and clearly remain subordinate to the reviewed source.
- Twenty-six organization-facing answer layers now carry explicit dossier provenance and mutable-fact policy fields.
- Continue semantic linking only through explicit human review and named deep-sheet targets; never auto-attach fuzzy matches.

## G. Communication and confidence trainer — **Functional local transcript metrics v1**

Delivered:

- Saved 30-, 60-, 90-, and 120-second speaking drills.
- Approximate WPM from elapsed answer time.
- Filler-phrase count, hedge count, sentence count, longest sentence, average sentence length, and clear-ending signal.
- Last-ten-answer trend summary plus fillers per 100 words.
- Metrics integrated into single-answer reviews and every board answer.
- Typed and speech-transcript paths use the same local analysis.
- Explicit warning that metrics do not infer scientific correctness, tone, eye contact, or true audio pauses.

Remaining:

- Consent-based in-memory recording/playback is delivered; automatic voice-activity pause timing remains browser-dependent.
- Repeated-phrase and weak-ending signals, a breathing reset, and posture/breath/eye-contact/ending self-checks are delivered.
- 30/60/90/120-second answer modes now use distinct approximate WPM bands and label them as transcript heuristics.
- Validate metrics against real speech transcripts and accents; do not present them as objective communication grades.

## H. Project Presentation Lab — **Structured personalization engine delivered; user facts pending**

Delivered:

- Twenty-five editable fields covering supervisor, material/system, motivation, objective, stage, personal/supervisor contribution, synthesis, precursors, parameters, atmosphere, safety, controls, characterization, observations, properties, application, limitations, and next experiment.
- Explicit states: unknown, planned—not completed, confirmed/user-entered, and not applicable.
- Required-field completeness evidence without pretending it validates scientific correctness.
- 30-second, 90-second, 3-minute, and non-specialist pitch generation from status-labelled fields only.
- Fact ledger shown alongside every generated pitch.
- Tailored honesty questions for missing required fields and method/technique-specific follow-ups for entered facts.
- Personalized project-only board with locally generated metadata.
- Local snapshots/evidence on profile updates.

Remaining:

- User must enter the actual material, route, precursors, parameters, hazards, techniques, personal work, and next experiment.
- Add richer instrument/troubleshooting branches after those facts are confirmed.
- A truth-ledger-bound scorecard now records negative-result, falsification, alternative-method, contribution, and reproducibility self-evidence; real project facts are still required for substantive scoring.
- Project version snapshots and a truth-labelled supervisor-review JSON export are delivered. Formal approval/signature remains external and is never inferred.
- Never convert a planned field into a completed claim automatically.

## I. Exam-to-Interview Bridge — **Functional lightweight bridge v1 delivered**

Delivered:

- Saved current target, latest mock/rank/score, weak topic, next milestone, and concepts needing verbal explanation.
- Converts conceptual, calculation, formula-memory, units, and time-pressure mistakes into first-principles, estimation, derivation, dimensional, or rapid-fire oral drills.
- Stores up to 100 converted mistake records with type, topic, note, drill, and timestamp, and directly launches the matching question or derivation practice.
- Persistent weekly interview-side checklist including project, speaking, technical, organization, pressure, and recovery blocks.
- Optional local file selector opens the separate tracker without importing its large content database.
- Exam weakness feeds the adaptive Mission Control plan.

Remaining:

- Weekly archive/reset history and a retained mistake-type count chart are delivered.
- Validate tracker-opening behavior across browsers and revoke local URLs after the opened page has loaded.
- Continue to avoid duplicating syllabus, PYQ, mock, and revision-cycle authority.

## J. Organization Dossiers and Signal Watch — **Three source-backed batches delivered**

Delivered:

- Twenty-four dossiers: ISRO, DRDO, BARC/DAE, CSIR-NIIST, IIA, IUCAA, RRI, PRL, IN-SPACe/private-space, CSIR-NPL, RRCAT, IGCAR, VECC, TIFR, BEL, ECIL, HAL, CSIR-NAL, Pixxel, Bellatrix Aerospace, Digantara, GalaxEye, KaleidEO, and SatSure.
- Seventy-two stable fact statements, technical-fit lanes, interview-focus lists, location/posting cautions, and why-organization frameworks.
- Fifty-four official source links with source label, confidence, `verifiedOn`, and `mayChange` fields.
- Stable-profile sources use a 365-day review horizon; mutable career/programme sources use a 30-day horizon.
- Current, stale, and check-required badges plus aggregate Signal Watch counts.
- Manual local recheck workflow that requires explicit confirmation after opening the official source and records evidence without altering source truth.
- Search by organization, location, role, or technical lane and filters for space, defence, nuclear, and research organizations.
- Organization-specific interview drills clearly labelled as training prompts rather than leaked questions.
- Mutable mission, vacancy, eligibility, salary, deadline, and selection-process facts are not inferred from stable summaries.
- Source JSON is hash-synchronized into the offline HTML.

Remaining:

- Six verified company-specific records are delivered. Add another employer only when it matches a confirmed role and has current official company/role sources; do not expand for count alone.
- A manual current-fact card workflow now requires an HTTPS official URL, verification date, and expiry no more than 30 days later; no feed or claim is prefilled.
- Organization-facing reviewed answers carry dossier provenance, and every dossier now exposes a local deep-topic fit map. Additional centre-specific answers should follow a confirmed application.
- Recheck all mutable careers, recruitment, and programme sources immediately before application/interview use.

Current provenance status:

- Twenty-four dossiers, seventy-two stable fact statements, and fifty-four official links are stored in `content/organization-dossiers.json`.
- At the build date, all fifty-four source entries are currently checked; mutable entries become check-required after their 30-day horizon.
- Deep-sheet learning resources retain scope, internet-required labels, and checked dates.

## K. Bengaluru/private-space track — **Nine-family role explorer delivered**

Delivered:

- Space Instrumentation, Materials Scientist, Payload Engineer, Test/Validation, Remote-Sensing Scientist, Space Data Analyst, Optics/Detector Engineer, Reliability Engineer, and R&D Engineer tracks.
- Each role maps three complete-v1 topics, three skill lanes, startup-style questions, and a self-recorded topic-evidence score.
- Persistent preferred-role selection and evidence history.
- Explicit Bengaluru-preference wording without implying refusal to relocate.
- Prototype, cheapest uncertainty-reducing test, failure documentation, interface, reliability, and iteration doctrine.
- IN-SPACe ecosystem dossier and sourced public-sector/aerospace organization profiles.

Remaining:

- Six company records and their current official career/profile pages are delivered with short review horizons. Add role-specific boards or another employer only against a confirmed application target.
- Add salary/location/work-culture claims only from current official sources or user-entered experience.
- Nine role-specific 30-minute boards and truth-ledger-aware project/portfolio mapping are delivered.

## L. Derivation Dojo — **Complete 50-item engine delivered**

Delivered:

- Fifty reviewed derivation objects: 36 from priority deep sheets plus 14 source-controlled extensions.
- Every item has topic, assumptions, at least five numbered steps, physical interpretation, dimensional/unit check, common mistake, panel interruption, and one-minute summary.
- One-step-at-a-time ladder reveal that requires the candidate to derive before opening the next step.
- Search by title, topic, assumption, or interruption and filter by topic/new/attempted/passed.
- Persistent attempts, self-pass date, marked error step counts, retry evidence, and aggregate progress.
- Prior error counts appear beside the exact step on later attempts.
- A pass cannot be recorded until all steps have been revealed.
- Print mode for the open derivation.
- Source JSON and embedded hash validation for the 14 extension derivations.

Remaining:

- Every derivation now resolves to a topic visual and opens reference-hidden canvas comparison.
- Add independent factual grading rather than self-pass only.
- Failed derivation steps now receive exact-step next-review dates in the shared Revision Queue; independent grading remains unavailable.
- Validate printed board sheets and attempt history in real browsers.

## M. Flashcards and spaced repetition — **800-card target and functional SRS v1 delivered**

Delivered:

- Removed all placeholder cards and delivered exactly 800 unique reviewed factual cards.
- Composition: 180 definitions, 153 equations with meaning/units/conditions, 118 deep-sheet trap recoveries, 50 Dojo derivation summaries, 157 topic-balanced rapid answers, 122 manually authored deep-sheet cards, and 20 foundation seeds.
- Every generated expansion card has a stable ID, topic, card type, front, back, review date, immutable-physics status, and non-mutable flag.
- Source generator reads reviewed deep-sheet and derivation content rather than inventing unrelated facts.
- Integrated all cards into one visible deck with type-filtered due, new, and random sessions.
- Implemented due, new, learning, mature, next-seven-days, and total-review statistics.
- Added Again, Hard, Good, and Easy ratings with local interval/ease/repetition/lapse updates.
- Again schedules a ten-minute relearning step; Good uses one-day then three-day learning steps before ease scaling.
- Added bounded per-card review history, legacy state migration, immediate undo, backup-compatible storage, and Mission Control routing.
- Source JSON/hash, exact 800-card runtime count, unique ID/front, schema, and type-filtered-session tests.

Remaining:

- Seventy-two source-aware organization fact cards are generated separately from the immutable 800-card deck and schedule missed recall through the Revision Queue. Project cards remain blocked until actual facts exist.
- Leech detection, suspend/bury, configurable new/review limits, and a 14-day day-by-day forecast are delivered. Version-1 and nested-malformed import fixtures are also validated.
- Validate interval behavior with longer real-use history; scheduling supports retrieval practice but does not prove mastery.

## N. Trap Radar — **Complete 250-item reviewed engine delivered**

Delivered:

- Two hundred fifty unique wrong statements and unique wrong/recovery pairs across 25 categories.
- Formula, units, thermo, entropy, quantum, uncertainty, XRD, project, ownership, optics, EM, nuclear, radiation safety, ISRO, DRDO, radar, astronomy, statistics, experimental integrity, HR, unknown-answer, diagram, and current-fact coverage.
- Medium, high, and critical severity plus topic/organization/safety tags.
- Every trap includes why it fails, a specific recovery, follow-up prompt, review date, stable ID, and reviewed status.
- Active-recall correction before revealing the reviewed recovery.
- Search plus category, severity, and new/practised/caught/missed filters.
- Persistent correction text, caught/missed counts, attempt history, and evidence events.
- Timed trap-to-question drills that inject the risky claim into a relevant reviewed question and save trap context with the answer review.
- Source generator, readable JSON output, embedded hash verification, and duplicate-pair tests.

Remaining:

- Missed/caught traps receive next-review dates, and a weakest-category miss-rate panel routes direct correction practice; all scores remain local self-evidence.
- Add reviewed model corrections for more trap records where the current recovery is concise.
- Validate anxiety/safety behavior and filter usability in real browsers.

## O. Stress Inoculation Bay — **Eleven-profile configurable trainer delivered**

Delivered:

- Timer pressure, polite interruption/reframing, certainty challenge, wrong premise, silence tolerance, project truth challenge, relocation/service readiness, unrelated topic pivot, over/under-qualified challenge, private-industry comparison, and failed-result challenge.
- Gentle, standard, and firm intensity settings that adjust time pressure.
- Per-profile enable/disable controls persisted in settings.
- Project/failed-result modes draw from project-relevant questions.
- Per-profile deadlines and separate composure/recovery scoring.
- Stop/review at any time and explicit non-abusive training doctrine.

Remaining:

- Actual mid-answer timed interruption events are delivered for interruption, certainty, wrong-premise, unrelated-pivot, and silence profiles. Real audio/VAD timing remains browser-dependent.
- Validate that pressure modes help rather than reinforce anxiety; never make them humiliating.

## P. Pre-flight Command — **Persistent target-scoped workflow v1 delivered**

Delivered:

- D-30, D-14, D-7, D-1, and interview-morning phases with 20 persistent checklist items.
- Separate checklist/logistics state for each active organization target.
- Venue/reporting, travel/backup route, official-notice document notes, and delay/recovery notes.
- Completion progress, evidence events, automatic D-30 Mission Control trigger, and print action.
- Explicit warning that organization-specific documents and reporting requirements must come from the current official notice/call letter.

Remaining:

- Add target-specific document templates only after official notice verification.
- Emergency-contact and accommodation fields plus optional `.ics` calendar export are delivered.
- Automatic D-30/D-14/D-7/D-1/interview-day phase display and passed-date warnings are delivered.
- Validate printed output and persistence in real browsers.

## Q. Evidence and honesty system — **Visible evidence ledger and provenance model delivered**

Delivered:

- Evidence Ledger module with verified official-source, user-entered project, planned project, unknown project, reconstructed pattern, reviewed training prompt, and AI-trusted-fact categories.
- AI-trusted-fact count is intentionally fixed at zero; AI output never becomes source truth automatically.
- Project known/planned/unknown state model, organization current/stale/check-required states, review dates, local source-check history, and evidence event counts.
- Stable labels for training examples and reconstructed patterns rather than leaked-interview claims.
- Evidence export through validated credential-free backup.
- Honesty rules shown in the UI and enforced in project pitch generation, source checks, answer statuses, and AI rendering.

Remaining:

- Per-field project snapshot history and per-statement organization source-pack provenance browsers are delivered.
- Actual snapshot reviews can now be recorded with an offline SHA-256 lock and explicit reviewer attestation. The app correctly labels these as tamper-evident local records, not authenticated digital signatures.
- Data-class deletion controls are delivered for answer/transcript history, drawings, source checks, project history, and evidence events.

## R. Accessibility and reliability — **First hardening pass delivered; validation remains**

Delivered:

- Skip-to-main-content link and focusable live main region.
- Accessible names and tooltips for every permanent navigation button, including icon-only responsive mode.
- Semantic modal dialog with `aria-modal`, hidden state, labelled close button, centralized opening, focus placement, Tab trapping, Escape/backdrop close, focus restoration, and inert background app.
- Visible `:focus-visible` outlines and scrollable sticky rails for short viewports.
- Command-dark, calm-light, and high-contrast themes persisted in settings.
- `prefers-reduced-motion` handling.
- Print stylesheet that removes controls/rails and prints clean cards.
- Assertive storage-failure status and safe text-only startup error rendering.
- Backup import with JSON parsing, format/version/plain-object validation, 5 MB limit, credential rejection, prototype-key filtering, confirmation, and safe local replacement.
- Backup export strips credentials and revokes object URLs.
- Automated static checks for skip link, modal semantics, focus styling, reduced motion, print CSS, and navigation accessible names.

Remaining:

- Perform real pointer/stylus/touch testing for the delivered canvas tools.
- Perform real screen-reader testing, 200%/400% zoom, forced-colours, mobile keyboard, and short-height browser testing.
- Audit every dynamically generated form for explicit label/control association and error announcements.
- Complete escaping/security review for all remaining legacy `innerHTML` paths.
- Version-1 legacy and nested credential/malformed backup fixtures are delivered; additional anonymized real-world fixtures can be added when available.
- Optional natural TTS now uses the endpoint allowlist, timeout, response-size, MIME, cancellation, object-URL cleanup, visible fallback, and session-key policy; real endpoint/audio testing remains external.
- Run full browser automation and real provider/CORS tests rather than only DOM and mocked-provider smoke tests.

---

# 6. LIVE VOICE, DRAWING, AND AI REMAINING WORK

## 6.1 Live room — **Functional offline-first live board v2; real audio/provider validation remains**

Delivered:

- ISRO, BARC, DRDO, IIA, IUCAA, and Private Space mode profiles with deterministic organization/core follow-ups offline.
- 5-, 15-, 30-, 45-, 60-, and 90-minute presets plus 1–120-minute custom duration.
- Start and explicit stop microphone controls, configurable timeout, recognition error state, and editable transcript before submission.
- Repeat question, “I don’t know,” and “give me a moment” recovery actions.
- Per-answer elapsed time, WPM/filler/sentence metrics, timestamp, drawing text alternative, and local transcript.
- Pause count and microphone start/end/error event history.
- Shared accessible drawing toolkit, local image/paste handling, explicit image permission and confirmation.
- Offline fallback when AI is disabled/unavailable; transcript transmission only when online and transcript permission are enabled.
- Saved technical, structure, composure, and recovery post-mortem plus complete local live-history evidence.
- Timer, recognition, paste handler, and object-URL cleanup on exit.

Remaining:

- True hold-to-talk behavior is delivered for pointer and keyboard; real voice-activity detection remains browser-dependent.
- One optional respectful mid-answer assumption/limit/measurement pivot is delivered in live sessions, alongside the dedicated stress events.
- Organization awareness, diagram quality, project ownership, and honesty sliders are delivered in the live post-mortem.
- Verify real browser SpeechRecognition support, permissions, mobile behavior, and natural-TTS fallback labelling.
- Complete live cloud/local AI tests with a user-supplied endpoint and current provider CORS/quota.

## 6.2 Drawing/image response — **Accessible drawing toolkit v1 delivered; advanced capture/review remains**

Delivered:

- Reusable draw and erase tools with adjustable colour and line width.
- Text labels, undo, redo, and clear confirmation.
- Accessible text alternative that can fully replace canvas use for keyboard-only users.
- Axes, variables, directions, units, and boundary-condition checklist.
- Persistent local drawing evidence with topic, text description, checklist, stroke count, and timestamp.
- Live-room canvas uses the same undo/redo/draw/erase/label controls and saves its text alternative with the transcript.
- Existing clipboard paste and file upload remain local until explicit AI submission.
- Explicit confirmation before image transmission and shared AI provider adapter.

Remaining:

- Delivered line, arrow, rectangle and ellipse tools, drag/drop, optional camera capture, and downloadable local PNG export.
- Delivered a strict structured vision-review JSON contract and payload preview; real provider validation still requires user configuration.
- Delivered reference-hidden and side-by-side comparison against all 100 reference SVGs.
- Validate pointer, stylus, touch, keyboard-only, and screen-reader workflows in real browsers.

## 6.3 AI architecture and privacy — **Hardened optional adapter v1; real-provider verification remains**

Delivered:

- API keys are session-only, excluded from settings/backups, and cleared by the kill switch.
- Online Copilot, approved project fields, live transcripts, and explicitly submitted images have separate opt-in controls.
- Shared provider request builder supports Gemini, OpenAI-compatible providers, and local Ollama-style chat.
- Endpoint policy requires HTTPS except local `localhost`, `127.0.0.1`, or `::1` endpoints.
- Configurable 5–120 second request timeout and 8–512 KB maximum response size.
- Active `AbortController` tracking, timeout cancellation, and one-click cancellation/disable.
- HTTP status errors, quota responses, oversized responses, malformed provider JSON, and unsupported response shapes surface explicit errors.
- Visible offline/connecting/online/error network state.
- Connection test uses the currently selected provider, endpoint, model, timeout, response cap, and session key without saving the key.
- Answer critique requests a strict JSON schema and validates arrays, strings, confidence enum, and verification warnings before rendering.
- Generated reviews are escaped, visibly labelled AI-generated/approximate, and never promoted automatically into project or organization facts.
- Live chat and image review use the shared provider adapter and retain explicit transcript/image permission checks.
- Mocked success, HTTP 429, malformed JSON, endpoint policy, provider request, strict review schema, and kill-switch tests pass.

Remaining and external constraints:

- A real cloud provider cannot be declared working until the user supplies a valid session key/endpoint and the provider permits browser CORS and current model/API access.
- Local AI requires a running local server configured to accept browser requests from the page origin.
- Provider model names, quotas, authentication, and APIs can change and require periodic live tests.
- Add real vision-provider tests with user-approved non-sensitive images.
- Natural TTS now enforces timeout, response size, audio MIME, endpoint policy, cancellation, and local fallback before playback. Real provider tests remain required.
- Provider, endpoint, model, and exact text-data previews are delivered before answer-review, live-transcript, image, or natural-TTS requests; no current action sends project fields.
- AI grading remains advisory and must not predict selection or override reviewed content.

---

# 7. CONTENT MASTER — SUBJECT GAPS STILL REMAINING

The current overview cards mention many of these areas, but mention is not mastery. Every group below still needs full interview-depth treatment.

## Mathematical foundation

Delivered in complete-v1 form:

- Units, dimensions, scaling, order-of-magnitude and limiting-case checks
- Gradient, divergence, curl, Gauss and Stokes interpretations
- Linear algebra, eigenproblems, Hermitian matrices, conditioning, ODE boundaries, and Fourier derivative methods
- Probability models, Gaussian/Poisson assumptions, likelihood, covariance, weighted means, fitting and residuals
- Random versus systematic effects, correlated uncertainty propagation, significant figures, Monte Carlo and numerical convergence
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, seven experiment/analysis cards, oral scripts, traps, flashcards, and readiness gates

Still remaining outside this priority sheet:

- Dedicated advanced Green-function, PDE, tensor, group-theory, Bayesian-inference, and scientific-computing sheets if a target role demands them

## Classical mechanics

Delivered in complete-v1 form:

- Newtonian mechanics, free-body diagrams, work-energy, impulse-momentum, centre of mass, torque and angular momentum
- Rotating-frame acceleration with Coriolis, centrifugal and Euler terms
- Generalized coordinates, stationary action, Euler–Lagrange, cyclic coordinates, Hamiltonian/phase-space qualifications
- Central forces, planar motion, angular-momentum reduction, effective potential, circular-orbit stability
- SHM, damping, driving, resonance, Q, coupled oscillators, normal modes, phase/group velocity and nonlinear-model tests
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, seven experiment cards, oral scripts, traps, flashcards, and readiness gates

Still remaining outside this priority sheet:

- Dedicated rigid-body tensor/Euler-angle, continuum, fluid, chaos and advanced Hamiltonian sheets if target roles demand them

## Electromagnetic theory

Delivered in complete-v1 form:

- Electrostatics, potential, Poisson/Laplace, conductors, dielectrics, D/P and boundary-value qualifications
- Magnetostatics, Lorentz force, Biot–Savart, Ampère, B/H/M, vector potential and gauge freedom
- All Maxwell equations, displacement current, continuity, source-free waves and transverse plane-wave relations
- Poynting theorem, energy density/flux, momentum/radiation pressure, interfaces and constitutive-law limits
- Conductors, skin depth, impedance, near/far fields, antennas, Friis link, ionosphere/atmosphere and EMC applications
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, eight experiment cards, oral scripts, traps, flashcards, and readiness gates

Still remaining outside this priority sheet:

- Dedicated advanced waveguide, microwave-network, relativistic-covariance, plasma-electrodynamics and full antenna-theory sheets if target roles demand them

## Optics and photonics

Delivered in complete-v1 form:

- Geometrical optics, sign conventions, paraxial limits, refraction, total internal reflection, and Brewster angle
- Coherence, two-beam interference, thin-film phase, single-slit diffraction, gratings, polarization, wave plates, fibres, and resolution
- Laser gain, population inversion, cavities, threshold, mode selection, linewidth cautions, and detector-facing safety context
- Photodiode responsivity/quantum efficiency plus CCD/CMOS, noise, calibration, bandwidth, and dynamic-range considerations
- Three full derivations, five worked numericals, thirty rapid, ten intermediate, five deep questions, three reference SVGs, oral scripts, experiments, traps, cards, and readiness gates

Still remaining outside this priority sheet:

- A dedicated advanced nonlinear/quantum optics sheet if required for a specific role
- Instrument-specific payload tailoring after actual target roles and project methods are confirmed

## Thermodynamics and statistical mechanics

Thermodynamics delivered in complete-v1 form:

- Zeroth, first, and second laws; system boundaries; explicit heat/work sign convention
- State versus path functions; quasistatic versus reversible; adiabatic versus isentropic
- Entropy transfer/generation, engines, refrigerators, Carnot limits, and COP
- U, H, F, G natural variables; Maxwell relations; chemical potential and phase coexistence
- Clapeyron/Clausius–Clapeyron, calorimetry, PVT, DSC, thermal conductivity, thermal-vacuum testing, spacecraft/synthesis applications
- Three full derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, oral scripts, experiments, traps, cards, and readiness gates

Statistical Mechanics delivered in complete-v1 form:

- Microstates/macrostates, multiplicity, Gibbs/Boltzmann entropy and ensemble constraints
- Canonical reservoir derivation, partition-function thermodynamics, grand ensemble and fluctuations
- MB/BE/FD occupations, thermal wavelength, density of states, classical limit and equipartition failure
- Free-electron Fermi energy, degeneracy, thermodynamic limit, ergodicity and critical-fluctuation cautions
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, seven experiment cards, oral scripts, traps, flashcards, and readiness gates

## Quantum, atomic, and molecular physics

Quantum Mechanics delivered in complete-v1 form:

- States, wavefunctions, Born probabilities, normalization, operators, self-adjointness/domain cautions, expectation and measurement
- Commutators, Robertson uncertainty, unitary Schrödinger evolution, stationary states, current and boundary conditions
- Infinite/finite wells, tunnelling, harmonic oscillator, parity, degeneracy and classical-limit qualifications
- Angular momentum, spin-½, identical particles, Pauli exclusion, perturbation, variation and WKB
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, seven experiment cards, oral scripts, traps, flashcards, and readiness gates

Still remaining outside this priority sheet:

- Atomic spectra, Zeeman/Stark/fine/hyperfine structure
- Molecular rotation/vibration, selection-rule depth and Born–Oppenheimer approximation
- Advanced many-body, open-system, relativistic and quantum-information sheets where roles demand them

## Solid state, materials, and the user’s project

Delivered in complete-v1 form:

- Crystal/reciprocal structure, diffraction, bands, carriers, defects, phonons, transport, Hall response, magnetism, and superconductivity foundations
- Deep technique matrix for XRD, SEM, TEM, EDS, AFM, Raman, FTIR, UV-Vis, XPS, TGA/DSC, four-probe, Hall, and magnetometry
- For each technique: principle, signal, sample/preparation, resolution, calibration, artifacts, claim boundary, and complementary evidence
- Six derivations, ten worked numericals, sixty rapid questions, twenty intermediate questions, ten deep questions, six reference diagrams, oral scripts, traps, cards, and readiness gates across the two sheets

Still remaining:

- Project-specific synthesis kinetics/thermodynamics, contamination controls, reproducibility, and troubleshooting for the actual chosen route
- Project-specific material chemistry and safety after the user supplies confirmed facts
- Deeper dedicated superconductivity/magnetism treatment if selected as a declared subject

## Nuclear and radiation

Delivered in complete-v1 form:

- Nuclear size/force, binding energy, SEMF, shell/magic-number roles and stability limits
- Exponential decay, activity, half/mean life, parent–daughter Bateman chains and secular-equilibrium cautions
- Q values, conservation, cross section, thresholds, fission/fusion, moderation, multiplication and criticality concepts
- Alpha/beta/gamma/neutron interactions, attenuation, scintillation/semiconductor detectors, efficiency, background and dead time
- Bq/Gy/Sv distinctions, irradiation versus contamination, ALARA and explicitly procedure-controlled safety wording
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, eight authorized/conceptual experiment cards, oral scripts, traps, flashcards, and readiness gates

Still remaining outside this priority sheet:

- Current BARC/DAE reactor/programme/recruitment facts from official sources
- Advanced reactor kinetics, fuel cycle, health physics and accelerator detail where a target role requires them
- Any operational radiation work, which remains restricted to authorization, qualified supervision and current facility procedures

## Electronics, instrumentation, and sensors

Delivered in complete-v1 form:

- Lumped circuits, Kirchhoff laws, R/C/L dynamics, impedance, p–n junctions, diode regimes, transistor bias, and small-signal limitations
- Op-amp amplifiers, negative feedback, gain-bandwidth, slew rate, stability, filters, oscillation cautions, ADC and sampling
- Johnson/shot noise, grounding, shielding, loading, oscilloscope/DMM limits, calibration, dynamic range, linearity, hysteresis, drift, and uncertainty
- Sensor-to-data and payload signal chains with ISRO, DRDO, BARC, materials-instrumentation, and private-space applications
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, eight experiment cards, oral scripts, traps, flashcards, and readiness gates

Still remaining outside this priority sheet:

- Dedicated digital logic, control systems, microwave/RF, and advanced signal-processing sheets where target roles require them
- Actual project sensor/instrument signal-chain tailoring after methods are confirmed

## Space, astronomy, DRDO, and private-space applications

Orbital/spacecraft/remote-sensing priority sheet delivered in complete-v1 form:

- Two-body equations, elements, energy/angular momentum, Kepler laws, vis-viva, escape, perturbations, Hohmann and plane-change maneuvers
- Rocket equation, station keeping, attitude determination/control, reaction wheels, magnetorquers and star sensors
- Structure, propulsion, power, thermal, communication, C&DH, TT&C, GNC/ADCS, FDIR and subsystem trade-offs
- Active/passive remote sensing, four resolutions, optical GSD, radar range resolution, SAR, radiometric calibration, atmospheric correction and ground truth
- Three derivations, five numericals, thirty rapid, ten intermediate, five deep questions, three SVGs, eight experiment/validation cards, oral scripts, traps, flashcards and readiness gates

Still remaining outside this priority sheet:

- Dedicated astronomy/astrophysics depth for coordinates, stellar evolution, galaxies, cosmology, exoplanets and space weather
- Dedicated DRDO radar/microwave/EW and advanced private-space product/reliability tracks
- Current ISRO missions, centres and recruitment facts from official sources

## Experimental science

Delivered across Materials Characterization and Mathematical Foundations/Data:

- Calibration, blanks, references, drift, repeatability/reproducibility, random/systematic effects, covariance and uncertainty propagation
- Residuals, fitting, outlier handling, numerical convergence, counting models, Monte Carlo propagation and reproducible analysis
- Complementary evidence, controls, representative sampling, artifacts, claim boundaries and negative/contradictory data reasoning

Still remaining:

- Project-specific hypotheses, independent/dependent variables, replicates, notebook workflow, ethics and lab-safety plan after actual methods are confirmed

---

# 8. FORMULA, DIAGRAM, AND RESOURCE VAULTS

## Formula Vault — **153-record active-recall module delivered**

Delivered:

- All 153 reviewed equations from the twelve priority deep sheets in one searchable module.
- Every record contains name, formula, symbols, units, physical meaning, and conditions/domain.
- Search across formula, symbol, meaning, and condition plus topic and new/recalled/missed filters.
- Active recall before reveal, persistent attempt text, recalled/missed counts, bounded history, and evidence events.
- Stable formula IDs and test-verified 153-record count.

Delivered in the 2026-08-15 extension batch:

- Every formula now exposes a topic-linked Derivation Dojo item, limiting-case prompt, worked numerical scale, experiment/application context, and matching equation SRS card.
- Known and missed outcomes schedule the next retrieval in the shared Revision Queue; due corrections feed Mission Control.

Remaining:

- Independent correctness grading remains unavailable without reviewed external feedback; the current links and recall ratings are training evidence.

## Diagram Library — **100/100 original references delivered**

The Content Master’s original SVG target is complete across mechanics, EM, optics, materials, thermodynamics, electronics, quantum/statistical/nuclear physics, orbital/remote-sensing, radar, astronomy, data, and characterization.

Every visual item now provides:

- Original reference SVG
- Reference-hidden active recall and hide/reveal labels
- “What to say while drawing” script
- User canvas and accessible text alternative
- Five-point comparison checklist
- Printable view and downloadable local PNG

The extension source is maintained in `content/visual-extensions.json` and built deterministically by `scripts/build_visual_extensions.py`.

## Resource Library — **Source-aware aggregator delivered; 114 unique links**

Delivered:

- Deduplicates resources from all twelve deep sheets, twenty-four organization/company dossiers, twenty-two reviewed study extensions, and four general catalogues.
- One hundred fourteen unique links with title, topic/organization, scope, study/organization/catalogue type, internet-required behavior, check date, and checked/stale/check-required state.
- Twenty-two reviewed study extensions add level, expected-use task, learning mode, and a verification date; new company dossier sources raise the deduplicated total beyond the original target.
- Search plus resource-type and check-state filters.
- Official organization sources remain separate from study resources and use local recheck evidence.

Remaining:

- Continue using official portals for recruitment, centre roles, missions, and current programmes; mutable links retain a 30-day horizon.
- Refresh or replace a study link if its checked page moves, changes scope, or becomes unavailable. Opening a link is not counted as study or verification evidence automatically.

---

# 9. DOCUMENTATION CONFLICTS TO RESOLVE

## 9.1 Offline-only versus optional network mode

`MISSION_VIVA_PLAN.md` states “zero network” and “no external services.” The later Master Upgrade Plan allows optional AI/TTS endpoints.

**Resolution:** define the contract as:

- Offline Core: zero requests, complete typed practice, browser-local voice where supported.
- Online Copilot: explicit opt-in, visible indicator, per-data-class consent, no embedded or persistently stored secret.

## 9.2 Attempt cycle mismatch

- Original plan default: 2026
- HTML default and right rail: 2027

**Resolution:** make cycle and dates editable; do not hardcode a global target year in presentation markup.

## 9.3 Stage/version mismatch

The navigation says `S0`, the Armory says `S4 upgrade`, the data says `v2`, and the UI displays end-state target counts.

**Resolution:** add one build manifest with version, stage, schema version, content counts, and release status.

## 9.4 “Full sheet” definition drift

The specifications require deep 16-tab sheets. The HTML calls ~115-word summaries “full theory sheets.”

**Resolution:** rename current content “overview” and reserve “complete” for sheets that pass the full acceptance schema.

## 9.5 Question/model-answer terminology drift

Many third fields are structure cues, not model answers. Generated drill-number copies are counted as separate questions.

**Resolution:** separate `question`, `answerOutline`, `modelAnswer`, `followUps`, and `variantOf`. Count a variant only when its scientific demand changes.

## 9.6 Target scope drift

The original plan centers ISRO/DRDO/BARC. Later documents add IIA, IUCAA, CSIR, DAE units, and private space. The HTML profile settings still hardcode only ISRO/BARC/DRDO targets.

**Resolution:** define primary, secondary, and exploratory targets in the profile.

## 9.7 Storage contract drift

The original plan proposes separate progress, SRS, mocks, and settings stores. The HTML declares a sessions key but never appends session records to it, and stores most evidence in one progress object.

**Resolution:** publish and validate a versioned storage schema; add import/migration tests.

## 9.8 Duplicate document section numbering

`MISSION_VIVA_MASTER_UPGRADE_PLAN.md` uses `# 4` for both Required Modules and Readiness Gates.

**Resolution:** renumber sections and add a status field or links to this audit.

## 9.9 Filename and deliverable drift — **Resolved**

The repository now uses canonical filenames:

- `mission-viva.html`
- `MISSION_VIVA_PLAN.md`
- `MISSION_VIVA_MASTER_UPGRADE_PLAN.md`
- `MISSION_VIVA_CONTENT_MASTER.md`

History remains in Git rather than download-style filename suffixes.

---

# 10. TECHNICAL DEBT AND TESTING BACKLOG

## Source structure

A single-file **deliverable** does not require an unmaintainable single-line source. The HTML has only about 90 physical lines, with one JavaScript line exceeding 53,000 characters.

Delivered:

- The maintainable shell, CSS, and JavaScript now live under `src/`; reviewed content remains in source JSON and generators.
- `scripts/build_self_contained.py` reproducibly produces the exact single-file HTML, and the smoke test rejects a stale artifact.
- A documentation JSON Schema and zero-dependency cross-source validator cover deep sheets, answers, aliases, traps, cards, derivations, dossiers, resources, and visuals.

Remaining:

- Further split the large generated JavaScript source into view/storage/practice/AI modules if maintenance requires it.
- Remove global function exposure and inline-event dependence only through a tested event-delegation migration; do not risk breaking the offline artifact for cosmetic architecture.

## Required automated tests

1. Parse/syntax test for the built HTML.
2. Boot test with empty, valid, migrated, and corrupt local storage.
3. Click every navigation item and every visible button.
4. Validate zero undefined handlers.
5. Validate every question schema and globally unique ID.
6. Detect semantic padding after stripping generated suffixes.
7. Validate every mutable fact has source and verification date.
8. Validate each complete topic against the 16-tab schema.
9. Test search/filter/pagination across the full bank.
10. Test timers and cleanup with deterministic fake time.
11. Test progress calculations, day streaks, and readiness bounds.
12. Test SRS scheduling and date rollover.
13. Test export/import round-trip and migration.
14. Test offline mode with network blocked and assert zero requests.
15. Test denied/unavailable speech APIs.
16. Test AI timeout, malformed JSON, HTTP errors, provider differences, and kill switch.
17. Test user/AI text escaping against HTML injection.
18. Run keyboard and automated accessibility checks.
19. Test print sheets.
20. Test at narrow width, 720p laptop, zoomed text, and reduced motion.

## Manual scientific review

Automated counts cannot validate physics. Every complete content batch needs review for:

- Correct notation and sign conventions
- Units and dimensions
- Hidden assumptions
- Limiting cases
- Experimental realism
- Safety
- Organization relevance
- Claims versus evidence
- Current-fact provenance
- Oral clarity

---

# 11. PRIORITIZED DELIVERY ROADMAP

## Phase 0 — Truth and runtime repair

- Fix all undefined handlers.
- Remove duplicate `drill`.
- Fix Answer Coach and Question QA.
- Rebuild metadata after all records are loaded.
- Remove Cloudflare injection.
- Remove fake readiness and misleading counters.
- Rename shallow sheets and placeholder banks honestly.
- Add baseline automated route/action tests.

**Exit gate:** no console errors through every offline user path; all displayed counts reflect substantive validated records.

## Phase 1 — Data architecture and evidence

- Introduce schemas and validation.
- Implement real session/event records.
- Implement readiness formulas and daily streaks.
- Add import/export/migrations.
- Implement source/provenance badges.
- Add complete profile and project field models.

**Exit gate:** progress can be reconstructed entirely from evidence events and cannot be increased by repeatedly checking a task.

## Phase 2 — Depth-first Content MVP — **Priority target complete: 12/12**

Delivered:

1. Solid State Physics — complete-v1
2. Materials Characterization — complete-v1
3. Optics and Lasers — complete-v1
4. Thermodynamics — complete-v1
5. Basic Electronics and Instrumentation — complete-v1
6. Mathematical Foundations, Data, and Uncertainty — complete-v1
7. Classical Mechanics and Oscillations — complete-v1
8. Electromagnetic Theory — complete-v1
9. Quantum Mechanics — complete-v1
10. Statistical Mechanics — complete-v1
11. Nuclear Physics and Radiation Protection — complete-v1
12. Orbital Mechanics, Spacecraft Systems, and Remote Sensing — complete-v1

Priority depth target complete. Structured project personalization, SRS v1, first reviewed answer/dossier batches, and accessibility hardening v1 are delivered; next work should expand coverage and complete release QA.

Advanced extension sheets should be added only for confirmed target roles, while project-specific synthesis must use confirmed project facts.

**Exit gate per sheet:** all 16 tabs, required question mix, 3 derivations, 5 numericals, diagrams, oral modes, resources, and a passing readiness gate.

## Phase 3 — Real practice and memory engines — **Core engines delivered; coverage remains**

Delivered:

- Reviewed prompt bank and 200 full-model answer layers.
- Timed single drills, why-chain, six-persona full boards, project/organization boards, progressive stress, answer metrics, and saved post-mortems.
- Functional SRS v1.

Remaining:

- Expand reviewed answer coverage and add factual scoring.
- Next-revision scheduling now connects weak answers, Dojo steps, traps, and formula outcomes through a shared correction queue. Independent factual grading remains.

**Exit gate:** three complete offline boards can be run, saved, resumed, reviewed, and used to generate the next daily plan.

## Phase 4 — Project, HR, and communication — **Project/communication engines delivered; facts and HR depth remain**

Delivered:

- Structured project fact ledger, truth-preserving pitches, tailored questions, and project-only board.
- Local communication metrics, timed confidence ladder, and history.
- Basic introduction, organization, officer scenario, relocation, service, and teamwork prompts.

Remaining:

- User-confirmed project facts and advanced project scoring.
- Deeper reviewed HR answer layers and organization-specific scenarios.
- Audio-pause/playback validation where consent and browser support allow.

**Exit gate:** project and communication readiness gates use saved evidence and no unknown project fact is presented as known.

## Phase 5 — Organization and Bengaluru tracks

- Build sourced dossiers.
- Add stale-fact workflow.
- Build private-space role tracks.
- Add current-awareness cards only with official sources and verification dates.

**Exit gate:** every displayed mutable fact is traceable and can be marked stale.

## Phase 6 — Live voice and optional AI

- Complete consent/privacy controls.
- Normalize provider adapters.
- Add deterministic offline interviewer behavior.
- Complete live transcript, drawing, and post-mortem evidence.
- Add realistic TTS only as a clearly labeled optional tier.

**Exit gate:** live mode remains useful with network disabled and transmits nothing without explicit permission.

## Phase 7 — Accessibility, print, and release QA — **Hardening v1 delivered; final validation pending**

Delivered:

- Accessible permanent navigation and modal lifecycle.
- Themes, high contrast, reduced motion, short-viewport rail behavior, and print views.
- Validated backup import/export and storage/startup error hardening.
- Static accessibility/security assertions in the smoke test.

Remaining:

- Canvas alternatives, complete form audit, screen-reader and high-zoom manual tests.
- Full real-browser automation and network/error-path tests.
- Canonical filenames, README, build manifest, and release changelog are delivered.

**Exit gate:** all readiness, content, privacy, offline, accessibility, and scientific-review gates pass.

---

# 12. DEFINITION OF “DONE”

MISSION VIVA is not done when a counter reaches a target. It is done when:

- Every visible action works.
- Offline mode makes zero network requests.
- No secret is embedded or persistently stored against policy.
- Every question is substantively distinct or explicitly linked as a meaningful variant.
- Every claimed model answer is scientifically reviewed.
- Every complete topic passes the 16-part schema.
- Every derivation contains actual steps.
- Every flashcard contains actual knowledge and participates in SRS.
- Every trap is meaningfully distinct.
- Every diagram has a reference, labels, and speaking guidance.
- Every mutable fact has provenance and a verification date.
- Every readiness score is based on recorded evidence.
- Every project statement is known, planned, unknown, or user-entered—never invented.
- Every target organization has a sourced and refreshable dossier.
- Voice and AI are optional, transparent, and privacy-preserving.
- Keyboard, zoom, contrast, reduced motion, screen reader, and print use are supported.
- The full test battery passes against the exact self-contained HTML delivered to the user.

---

# 13. USER INFORMATION STILL REQUIRED

The app cannot become genuinely personalized until the following are confirmed:

- Active target cycle and known interview/application dates
- Exact target posts and priority order
- Final declared and prepared subjects
- Project material/material family
- Synthesis method and precursors
- Planned/available characterization instruments
- Current project stage and work completed personally
- Known safety constraints, controls, limitations, and next experiment
- Weekly interview-practice time
- Private-space role interests
- Relocation preferences framed professionally
- Whether optional AI is desired
- Which project/transcript/image data, if any, may leave the device

Unknown fields must remain visibly unknown until the user supplies them.

---

# FINAL AUDIT DOCTRINE

> Build depth before breadth, evidence before readiness, and working behavior before counters.

The next upgrade should not add another hundred labels, another navigation button, or another generic card. It should make the existing core truthful:

1. Fix what is broken.
2. Remove padding.
3. Complete the highest-priority subjects deeply.
4. Record real practice evidence.
5. Personalize the project honestly.
6. Source every changing fact.
7. Test the exact offline file end to end.

Only then should the system expand toward the full vision in the three planning documents.
documents.
