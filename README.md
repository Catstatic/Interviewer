# MISSION VIVA

An offline-first, self-contained scientist-interview preparation system for physics, materials, instrumentation, space, defence, nuclear, and research-institute roles.

## Open the application

Open [`mission-viva.html`](mission-viva.html) directly in a modern browser. No build step, account, or network connection is required for the offline core.

External study links and the optional AI/TTS integrations require internet or a user-controlled local endpoint.

## Current reviewed build

- 12/12 priority complete-v1 deep sheets
- 555 reviewed standalone interview prompts
- 325 reviewed full-model answer layers
- 128 human-reviewed semantic answer aliases, including explicit deep-sheet and full-layer targets
- 598 indexed deep-sheet answers/outlines/numericals
- 393 question-bank records resolving to full models, 103 to deep answers, and 59 still cue-only
- 250 reviewed distinct traps
- 800 reviewed factual SRS cards with daily limits, leech, suspend, and bury controls
- 50 complete Derivation Dojo items
- 153 reviewed Formula Vault records with derivation, limiting-case, numerical, experiment, and SRS links
- 24 source-backed organization/company dossiers, including six Bengaluru private-space records; all 54 official links checked on 2026-08-15
- 114 deduplicated, metadata-complete study/official resource links
- 100 original SVG references with reference-hidden drawing and comparison practice
- Cross-module revision scheduling for weak answers, traps, formulae, and derivation steps
- Structured project truth ledger
- Adaptive Mission Control, target-specific evidence maps, timed/role-specific boards, stress profiles, communication metrics, Exam Bridge, and target-scoped Pre-flight
- Five-level declared-subject trees, dedicated answer-correction sequences, reviewed factual checklists, and user-authored simple/specialist revisions
- Resumable Live Room/post-mortem state, hold-to-talk, local in-memory audio practice, and respectful timed interruptions

Counts are schema-tested and do not include numbered placeholder variants.

## Maintainable sources

- `src/mission-viva.template.html` — semantic page shell
- `src/mission-viva.css` — offline styles and print/accessibility rules
- `src/mission-viva.js` — application logic plus synchronized content bundles
- `scripts/build_self_contained.py` — deterministic single-file builder

Maintainable content is stored under [`content/`](content/):

- `deep-sheets.json`
- `answer-layers.json`
- `answer-aliases.json`
- `derivation-extensions.json`
- `expanded-flashcards.json`
- `trap-radar.json`
- `organization-dossiers.json`
- `resource-extensions.json`
- `visual-extensions.json`

Maintainable application sources live in `src/mission-viva.js`, `src/mission-viva.css`, and `src/mission-viva.template.html`. Content sync scripts update the JavaScript source; the final build step produces the self-contained HTML. Re-sync and rebuild after editing source content:

```bash
python3 scripts/build_expanded_flashcards.py
python3 scripts/build_trap_radar.py
python3 scripts/build_answer_aliases.py
python3 scripts/build_answer_batch5.py
python3 scripts/build_answer_batch6.py
python3 scripts/build_answer_batch7.py
python3 scripts/build_answer_batch8.py
python3 scripts/build_answer_batch9.py
python3 scripts/build_answer_batch10.py
python3 scripts/build_answer_batch11.py
python3 scripts/build_answer_batch12.py
python3 scripts/build_visual_extensions.py
python3 scripts/sync_expanded_flashcards.py
python3 scripts/sync_deep_sheets.py
python3 scripts/sync_answer_layers.py
python3 scripts/sync_answer_aliases.py
python3 scripts/sync_organization_dossiers.py
python3 scripts/sync_derivation_extensions.py
python3 scripts/sync_trap_radar.py
python3 scripts/sync_resource_extensions.py
python3 scripts/sync_visual_extensions.py
python3 scripts/build_self_contained.py
```

## Validation

Run the zero-dependency smoke and schema battery:

```bash
python3 scripts/validate_content.py
node tests/phase0-smoke.js
```

It checks runtime boot, content hashes, unique IDs, question metadata, handlers, deep tabs, full answers, aliases, traps, SRS scheduling, derivations, project privacy, organization provenance, boards, communication metrics, backup validation, AI request policies, accessibility invariants, and major module actions.

## Privacy

- Offline mode sends no interview data.
- AI is disabled by default.
- API keys remain in memory for the current page session only.
- Project fields, transcripts, and images have separate permissions.
- No project image is transmitted without explicit confirmation.
- Backup export excludes credentials.

## Important limitations

- AI availability depends on a user-configured current endpoint/model/key, provider quota, and browser CORS. Mocked provider tests pass, but no cloud connection is bundled or guaranteed.
- Current missions, programmes, careers, eligibility, dates, salaries, and posting details must be rechecked on official sources.
- Project context now records Prof. RC Nath, a grinding/firing synthesis phase, and a subsequent characterization phase. Personalization remains incomplete until the exact compound, precursors, firing schedule/atmosphere, instruments, safety controls, contribution, and next run are confirmed.
- Training evidence and AI feedback do not predict selection.

See [`MISSION_VIVA_REMAINING_WORK_AUDIT.md`](MISSION_VIVA_REMAINING_WORK_AUDIT.md) for the detailed completion and remaining-work ledger.
