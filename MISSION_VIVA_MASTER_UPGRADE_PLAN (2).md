# MISSION VIVA — MASTER UPGRADE PLAN
## The all-in-one interview readiness system for a fifth-year BS-MS student at IISER Thiruvananthapuram
### Target: ISRO · DRDO · BARC/DAE · Bengaluru private-space and aerospace organizations
### Profile: Mangalorean · astronomy enthusiast · final-year project under RC Nath · synthesis + characterization · preparing for GATE and CSIR-NET

> **Honesty clause:** MISSION VIVA cannot guarantee selection. No offline file can guarantee an interview result because panels, eligibility rules, vacancies, and competition vary. The purpose of this system is to make every trainable part of performance measurable: knowledge, project defence, communication, composure, organization awareness, exam-to-interview transition, and logistics.

---

# 1. PERSONAL MISSION PROFILE

The system must permanently understand this user profile:

- Fifth-year BS-MS student at IISER Thiruvananthapuram
- From Mangalore, targeting Bengaluru for work where possible
- Astronomy and space enthusiast
- Long-term ambition: work in space science or technology, learn deeply, innovate, and eventually build a private space venture
- Current project under RC Nath
- Project stages: synthesis followed by characterization
- Project is currently early-stage; results and exact techniques may not yet be known
- GATE and CSIR-NET are important routes toward interview eligibility
- Target organizations: ISRO, DRDO RAC/CEPTAM, BARC OCES/DGFS, DAE units, CSIR laboratories, private space and aerospace companies
- Interview weakness: low confidence and limited interview practice

The app must never make the project sound like an excuse or a low-effort choice. It should frame it honestly and professionally:

> “I selected a feasible project that allows me to develop hands-on experience in synthesis and characterization while managing my final-year responsibilities and preparing seriously for competitive examinations. My current focus is to understand the synthesis process carefully and establish reliable characterization methods.”

If asked about a previous preferred supervisor:

> “I had initially explored another project, but the available student capacity was limited. I then chose this project based on feasibility, supervision, and the opportunity to build practical experimental skills.”

Never say that the project was chosen only for an easy grade.

---

# 2. CORE DESIGN PRINCIPLE

MISSION VIVA must not be merely a question bank. It must function as:

1. A **diagnostic system** that finds weaknesses.
2. A **curriculum** that tells the user what to study next.
3. A **sparring partner** that applies pressure.
4. A **project-defence trainer** that knows the user's exact work.
5. A **communication coach** for a weak or nervous interviewee.
6. A **memory system** using spaced repetition.
7. A **mock-board simulator** that measures improvement.
8. A **mission-awareness dossier** for each organization.
9. A **pre-interview logistics and composure system**.
10. A **truth-preserving system** that never invents project results, official facts, or leaked questions.

The file must be usable offline, without accounts, APIs, network calls, external libraries, or secrets.

---

# 3. OPTIONAL AI COPILOT — USEFUL, CONTROLLED, AND NEVER REQUIRED

AI can substantially improve the interview system, especially for follow-up “why?” questions, answer critique, adaptive questioning, and project-specific cross-examination. However, AI creates a deliberate architecture trade-off:

- A truly offline single HTML cannot call a cloud AI model.
- A cloud AI model requires network access and usually an API key or a user-controlled local endpoint.
- An API key embedded in HTML is not secure.
- Project data and voice transcripts should not be uploaded automatically.

Therefore MISSION VIVA must have two modes:

## Offline Core Mode — default

Works forever without network:

- Curated question bank
- Deterministic why-chains
- Rule-based answer structure checks
- Local timers and post-mortems
- Local flashcards and scheduling
- Project question templates
- No key, no login, no transmission

## Optional AI Copilot Mode — explicit opt-in

The user must manually enable this mode and choose one of:

1. A user-provided compatible AI endpoint.
2. A locally running model endpoint such as Ollama or LM Studio.
3. A future hosted service configured by the user.

The HTML must never contain a developer’s secret key. It may accept a key at runtime, hold it only in memory, and clearly warn that browser-side keys are not secure.

AI settings:

- Disabled by default
- Clear online indicator
- User-controlled endpoint field
- Optional model name
- “Do not send project data” toggle enabled by default
- “Do not send voice transcript” toggle enabled by default
- One-click disable
- Request and response timeout
- Graceful offline fallback
- No automatic background calls
- No hidden telemetry
- No claim that AI grading predicts selection

## AI functions

### Adaptive why-chain

Instead of showing five fixed whys, AI can inspect the user’s answer and ask the next most useful question:

- If the definition is missing: ask for a definition.
- If the mechanism is missing: ask “why does that happen?”
- If an assumption is missing: ask what conditions are required.
- If the answer overclaims: ask what evidence supports the claim.
- If the answer is correct but shallow: ask for a limiting case.
- If the user says “I don’t know”: give a smaller bridge question rather than humiliating them.

The AI must not endlessly interrogate. It should stop after a configurable depth, normally five follow-ups.

### Answer critique

Ask the model to return structured feedback:

- Correct ideas
- Incorrect or doubtful ideas
- Missing definition
- Missing mechanism
- Missing example
- Missing limitation
- Unnecessary digression
- Suggested improved answer
- One next question
- Confidence level

The model must distinguish factual correctness from communication quality and must say when it is uncertain.

### Project examiner

Given only user-approved project fields, AI can generate:

- Synthesis questions
- Characterization questions
- Instrument-principle questions
- Controls and uncertainty questions
- Troubleshooting questions
- “What did you personally do?” questions
- Negative-result questions
- Alternative-method questions

The model must not invent material properties, results, instruments, or conclusions. Unknown fields must be labelled unknown.

### Model-answer coach

AI can transform a user’s rough answer into:

- 30-second version
- 90-second version
- Technical version
- Non-specialist version
- More concise version
- More rigorous version

It must preserve the user’s actual facts and mark any suggested fact requiring verification.

### Panel persona generator

AI can vary question style among:

- Fundamentalist
- Sniper
- Skeptic
- Project specialist
- Organization officer
- Mentor

Persona is a style instruction, not permission to invent official interview patterns.

### Confidence and communication coach

If transcript is explicitly approved for upload, AI may identify:

- Filler words
- Overlong sentences
- Weak endings
- Excessive hedging
- Unclear terminology
- Repeated phrases
- Abrupt or defensive tone

Local browser metrics should be preferred over sending audio or transcripts.

## AI response contract

Every AI request should request JSON with a strict schema. Example:

```json
{
  "nextQuestion": "string",
  "depth": 1,
  "correctIdeas": ["string"],
  "concerns": ["string"],
  "missingStructure": ["definition", "mechanism", "example", "boundary"],
  "modelAnswer": "string",
  "verificationWarnings": ["string"],
  "confidence": "low | medium | high"
}
```

If parsing fails, display the raw response safely and return to offline mode.

## AI safety rules

- Never describe generated questions as actual leaked questions.
- Never guarantee selection.
- Never invent current recruitment dates, pay, eligibility, mission status, or organization facts.
- Always label generated content.
- Ask the user to verify official facts.
- Do not send supervisor-confidential or unpublished project information.
- Do not send voice recordings by default.
- Do not store API keys in localStorage.
- Do not silently upload anything.

# 4. REQUIRED MODULES FOR THE FULL BUILD

## A. Mission Control dashboard

Display:

- Days to each editable interview date
- GATE and CSIR-NET preparation status
- Interview readiness score
- Project readiness score
- Communication confidence score
- Subject readiness radar
- Current streak
- Sessions completed
- Weakest three skills
- Today’s automatically generated plan
- Last session resume button
- “Do this now” single action

Daily plan must combine:

- Weak subjects
- Overdue flashcards
- Previous-paper practice
- One project question
- One speaking drill
- One organization-awareness card
- One composure drill

The dashboard must avoid overwhelming the user. Always show one next action first.

## B. Personal profile and target manager

Editable fields:

- Degree and year
- Institution
- Home city
- Target city: Bengaluru
- Target organizations
- Target posts
- Exam routes
- Interview dates
- Declared favorite subjects
- Prepared-but-not-declared subjects
- Project details
- Current confidence level
- Weekly available hours

Allow separate profiles for:

- ISRO
- DRDO
- BARC/DAE
- Private space
- Research institute

Each profile should generate different interview emphasis.

## C. Subject Armory

Each topic must contain:

- First-principles explanation
- One-page interview sheet
- Definitions
- Formulae and units
- Physical interpretation
- 20–60 rapid questions
- 10 intermediate questions
- 5 deep questions
- 5 numerical problems
- 3 derivations
- Common traps
- “Explain to a child” drill
- “Explain to a scientist” drill
- Boundary conditions and limitations
- Cross-links to the user’s project
- Confidence rating
- Last reviewed date
- Spaced-repetition status

Required topic groups:

### Core physics

- Classical Mechanics
- Electromagnetic Theory
- Quantum Mechanics
- Thermodynamics
- Statistical Mechanics
- Mathematical Physics
- Special Relativity
- Atomic and Molecular Physics
- Optics
- Solid State Physics
- Nuclear Physics
- Particle Physics basics
- Fluid Mechanics
- Plasma Physics
- Condensed Matter basics

### Engineering and experimental

- Analog Electronics
- Digital Electronics
- Semiconductor Devices
- Signals and Systems
- Control Systems
- Instrumentation
- Measurement and Calibration
- Error Analysis
- Numerical Methods
- Scientific Programming
- Sensors and Detectors
- Vacuum and Cryogenic basics

### ISRO-oriented

- Orbital Mechanics
- Spacecraft Systems
- Launch Vehicles
- Rocket Propulsion basics
- Satellite Communication basics
- Remote Sensing
- Space Optics
- Attitude Determination and Control
- Telemetry, Tracking and Command
- Space Environment
- Thermal Control
- Space-qualified materials

### DRDO-oriented

- Radar
- Antennas
- Microwave basics
- Signal Processing
- Sensors
- Electronic Warfare basics
- Guidance and Navigation
- Defence materials
- Optoelectronics
- Image processing
- Reliability and testing

### BARC/DAE-oriented

- Radioactive Decay
- Nuclear Reactions
- Nuclear Models
- Reactor Physics
- Radiation Detection
- Radiation Protection
- Dosimetry
- Health Physics
- Nuclear Instrumentation
- Particle Accelerators
- Nuclear Materials
- Fuel-cycle basics

### Astronomy and astrophysics

- Celestial coordinates
- Magnitudes and flux
- Spectroscopy
- Stellar structure basics
- Stellar evolution
- Galaxies
- Cosmology basics
- Telescopes and detectors
- Angular resolution
- Doppler effect
- Exoplanet detection
- Solar physics
- Space missions and payloads

## D. Declared-subject strategy

The app must distinguish:

1. **Declared favorites:** subjects the panel may probe deeply.
2. **Prepared subjects:** subjects the user can answer reasonably.
3. **Survival basics:** all other foundational areas.
4. **Do-not-declare-yet:** subjects not ready for deep follow-up.

Initial safe recommendation for this user:

- Optics
- Thermodynamics
- Basic Electronics

Project-linked subject:

- Solid State Physics

The app must warn that an “easy” subject can become difficult if declared without depth. It should generate five levels of follow-up questions before allowing a subject to be marked interview-ready.

## E. Sparring Hall

Modes:

- Warm-up interview
- Why-chain: five successive why questions
- Rapid fire: 60-second answers
- Deep dive: one topic for 10–15 minutes
- Full board: 30, 45, and 60-minute simulations
- Project-only board
- Organization-only board
- Silent-pause drill
- Hostile-face simulation
- Interruptions drill
- “I don’t know” drill
- Explain like I am five
- Explain like I am a colleague
- Recovery after a wrong answer

Panel personas:

- Fundamentalist: first principles and derivations
- Sniper: short rapid questions
- Skeptic: challenges certainty
- Project specialist: experimental detail
- Organization officer: mission and service questions
- Mentor: calming but probing

Every session must record:

- Question
- Answer
- Time taken
- Word count
- Hesitation estimate if voice is available
- Structure score
- Technical score
- Composure score
- Recovery score
- Whether the answer was honest
- Follow-up questions missed
- Next revision date

## F. Answer Coach

Teach the user to answer using multiple structures:

### Technical answer

1. Define
2. State the governing principle
3. Explain the mechanism
4. Give an equation or example
5. State assumptions
6. State limitation or boundary

### Project answer

1. Motivation
2. Objective
3. Material/system
4. Method
5. Characterization
6. Observation
7. Interpretation
8. Limitation
9. Next step

### HR answer

1. Situation
2. Action
3. Result
4. Learning

### Unknown answer

> “I am not certain of the exact answer. What I do know is … My first-principles reasoning would be … I would verify the remaining detail before making a firm claim.”

Automatic post-mortem checks should look for words or concepts indicating definition, mechanism, example, limitation, and uncertainty. These are prompts, not grades.

## G. Communication and confidence trainer

This is critical because the user identifies as weak in interviews.

Features:

- 30-second speaking drills
- 60-second speaking drills
- 90-second introduction trainer
- 2-minute technical explanation
- Filler-word counter
- Pace estimate
- Long-pause tracking
- Sentence-length warning
- Eye-contact and posture checklist
- Voice warm-up
- Breathing timer
- Pre-answer pause training
- “Speak slower” mode
- “Do not over-explain” mode
- Playback if browser support allows it
- Typed fallback always available

Daily confidence ladder:

1. Read an answer silently.
2. Read it aloud alone.
3. Answer from bullet points.
4. Answer with a timer.
5. Answer with interruptions.
6. Complete a full mock board.

## H. Project Presentation Lab

Required fields:

- Supervisor
- Material/material family
- Scientific motivation
- Synthesis method
- Precursors
- Key parameters
- Safety considerations
- Planned characterization
- Instrument principles
- Expected observations
- Main property
- Application
- Current stage
- Personal contribution
- Known limitations
- Next experiment

Auto-generate:

- 30-second summary
- 90-second summary
- 3-minute technical presentation
- Non-specialist explanation
- Instrument questions
- Synthesis troubleshooting questions
- Control-experiment questions
- Uncertainty questions
- Supervisor-contribution distinction
- “What if the result is negative?” answer
- “What did you personally do?” answer
- “Why this method?” answer
- “What would falsify your interpretation?” answer

Important early-stage answer:

> “The project is currently in the initial phase. I have not yet reached final characterization results, so I do not want to claim conclusions prematurely. At present I can explain the motivation, planned synthesis, characterization principles, expected observations, and how I would interpret competing outcomes.”

## I. Exam-to-Interview Bridge — no duplicate exam tracker

The user already maintains a separate approximately 47 MB HTML system for GATE and CSIR-NET preparation. MISSION VIVA must **not duplicate** that large tracker.

MISSION VIVA should only contain a lightweight bridge:

- Optional exam status fields: current target, latest mock/rank, weak topic, next exam milestone
- A manual “exam weakness to interview drill” entry box
- A place to record concepts that need verbal explanation
- A checklist for converting solved-paper knowledge into spoken answers
- A simple link/instruction to open the separate exam HTML file
- No copied syllabus, previous-paper database, mock engine, or large exam content bank

Conversion prompts:

- Conceptual mistake → first-principles interview question
- Calculation mistake → estimation drill
- Formula-memory mistake → derivation drill
- Units mistake → dimensional-analysis drill
- Time-pressure mistake → rapid-fire drill

The separate exam tracker remains the authority for:

- Syllabus completion
- Previous-year questions
- Accuracy
- Speed
- Mistake types
- Mock scores
- Revision cycles

MISSION VIVA remains the authority for:

- Interview communication
- Project defence
- Technical oral questioning
- Composure
- Organization awareness
- Full-board practice

Weekly interview-side routine:

- 1 project block
- 3 short speaking blocks
- 2 technical oral-question blocks
- 1 organization-awareness block
- 1 pressure drill
- 1 full rest/recovery period

## J. Organization Dossiers

Every organization fact must include:

- Fact
- Official source URL or source note
- Date verified
- Confidence level
- “May change” flag

Dossiers:

- ISRO and major centres
- DRDO and relevant Bengaluru laboratories
- BARC and DAE units
- CSIR-NIIST and materials labs
- NPL and measurement science
- RRCAT, IGCAR, VECC
- PRL, RRI, IIA, TIFR
- BEL, ECIL, HAL, NAL
- Private space companies in Bengaluru

Questions should focus on:

- What the organization does
- Why the user wants to join
- What technical skills fit
- What work culture may require
- Location and transfer readiness
- Service orientation
- Current missions or programs

## K. Bengaluru and private-space track

Add role families:

- Space instrumentation
- Materials scientist
- Sensor engineer
- Payload engineer
- Test and validation engineer
- Remote-sensing scientist
- Space-data analyst
- Optics and detector engineer
- Reliability engineer
- R&D engineer

Add startup-style questions:

- What would you build with limited resources?
- How would you test a prototype?
- What is the cheapest experiment that reduces uncertainty?
- How would you document a failed test?
- What makes a component space-ready?
- How would you communicate risk to a non-specialist?

## L. Derivation Dojo

Target at least 50 derivations, including:

- Bragg’s law
- Thin-film interference
- Fraunhofer single-slit diffraction
- Grating equation
- Brewster angle
- Wave equation from Maxwell equations
- Poynting theorem
- RC charging
- Diode equation meaning
- Carnot efficiency
- Thermodynamic identities
- Maxwell relations
- Partition function to energy
- Boltzmann distribution
- Radioactive decay
- Binding energy
- Semi-empirical mass formula terms
- Bohr model energy
- Particle in a box
- Harmonic oscillator basics
- Uncertainty relation
- Angular momentum commutators
- Hall coefficient
- Drude conductivity
- Band-gap estimate
- Fermi-Dirac distribution
- Debye heat capacity
- Kepler’s laws
- Escape velocity
- Hohmann transfer
- Radar range equation
- Doppler shift
- Telescope resolution
- Signal-to-noise ratio
- Error propagation
- Least-squares fitting

Every derivation needs:

- Assumptions
- Step ladder
- Physical interpretation
- Common mistake
- Panel interruption
- One-minute summary

## M. Flashcard and spaced repetition engine

Target:

- 800 cards
- Formula cards
- Definition cards
- Unit cards
- Organization cards
- Mission cards
- Project cards
- Trap cards
- “Explain in one sentence” cards

Use local scheduling with:

- Again
- Hard
- Good
- Easy
- Due date
- Ease factor
- Review history

## N. Trap Radar

Include at least 250 trap patterns, such as:

- Giving a formula without physical meaning
- Confusing heat with temperature
- Saying a wavefunction is a physical wave
- Calling every satellite geostationary
- Treating half-life as activity
- Saying XRD proves every property
- Claiming a result before characterization
- Confusing exposure and contamination
- Ignoring units
- Overclaiming personal contribution
- Saying “I like all subjects”
- Criticizing a former supervisor
- Saying the project was chosen only for easy marks
- Giving generic “I love space” motivation
- Bluffing after uncertainty

## O. Stress Inoculation Bay

Add progressively harder sessions:

- Timer only
- Timer plus interruption
- Timer plus unrelated follow-up
- Repeated “are you sure?”
- Deliberate wrong premise
- Silence after answer
- Project result challenge
- “You are overqualified/underqualified” challenge
- “Why not private industry?” challenge
- “Are you willing to relocate?” challenge

Grade composure separately from correctness.

## P. Pre-flight Command

D-30, D-14, D-7, D-1, and interview-morning checklists.

Include:

- Documents
- Travel
- Venue
- Clothes
- Sleep
- Food and hydration
- Device and call-letter check
- Ten gentle warm-up questions
- No-new-topic rule
- Breathing routine
- Recovery plan if delayed
- Walk-in mantra

## Q. Evidence and honesty system

The app must visibly label:

- Verified official fact
- User-entered fact
- Reconstructed interview pattern
- Training example
- Outdated fact requiring verification
- Unknown or not-yet-available project information

Never include alleged leaked questions as real.

## R. Accessibility and reliability

- Fully offline
- No external assets
- Responsive on a laptop
- Keyboard usable
- Reduced-motion mode
- High-contrast mode
- Print-friendly sheets
- Voice optional
- Typed fallback
- Local backup/export
- Local reset
- No sensitive data transmission
- Graceful recovery if speech APIs fail

---

# 4. READINESS GATES

The app must not show “interview ready” merely because modules are opened.

## Gate 1: Foundation

- 80% basic-topic accuracy
- Units and definitions reliable
- Can explain 20 core ideas in one minute

## Gate 2: Declared subjects

For each declared subject:

- 30 rapid questions
- 10 intermediate questions
- 5 deep follow-ups
- 3 derivations
- 2 numerical problems
- One 5-minute explanation

## Gate 3: Project

- 90-second pitch without notes
- Can explain every planned instrument
- Can state what is known and unknown
- Can answer 20 project cross-questions
- Can describe one failure and troubleshooting path

## Gate 4: Communication

- Introduction under 90 seconds
- Most answers under two minutes unless invited deeper
- Reduced filler words
- Comfortable pause before answering
- Clear ending to each answer

## Gate 5: Full board

Complete three full boards on separate days with:

- Technical score at least 4/5
- Structure score at least 4/5
- Composure score at least 4/5
- No fabricated facts
- Recovery after unknown questions

## Gate 6: Organization readiness

For every target organization:

- What it does
- Why the user wants it
- Why the user fits
- One current or stable program
- One relevant centre/lab
- Transfer/relocation answer
- Service and teamwork answer

---

# 5. BUILD ORDER

The next large build should proceed in this order:

1. Expand the question bank to 250 questions.
2. Build the 12 full topic sheets.
3. Add model answers and trap patterns.
4. Complete the 50-derivation Dojo.
5. Add the GATE/CSIR-NET mistake tracker.
6. Add project-specific generation after the material and instruments are known.
7. Add 200 flashcards and local scheduling.
8. Add 30-minute full-board mode.
9. Add communication metrics and daily confidence ladder.
10. Add organization dossiers with source notes.
11. Add final QA and print-friendly export.
12. Expand toward the full 1,500-question forge.

---

# 6. USER'S IMMEDIATE ACTIONS OUTSIDE THE FILE

The file helps, but it cannot replace deliberate practice. The user should:

- Study consistently for GATE and CSIR-NET.
- Ask the supervisor what material and techniques will be used.
- Maintain a project notebook.
- Record every experimental decision and failure.
- Learn the principles of every instrument used.
- Practise speaking aloud daily.
- Solve previous-year questions under time pressure.
- Review official recruitment notices rather than relying on old numbers.
- Apply for internships, research positions, and Bengaluru opportunities.
- Practise with a real person whenever possible.

Minimum weekly interview routine:

- 5 days × 10 minutes speaking aloud
- 3 days × 5 technical questions
- 2 days × one project answer
- 1 day × one pressure drill
- 1 full mock every two weeks initially
- 1 full mock every week near the interview

---

# 7. LIVE VOICE-TO-VOICE BOARD SIMULATOR

This is a major future module and should become the crown jewel of MISSION VIVA.

## User experience

The user selects an interview mode, grants microphone permission if desired, and presses **Begin interview**. The system then behaves like a live board:

1. A brief waiting/room-opening screen.
2. Interviewer greeting and introduction.
3. “Please introduce yourself.”
4. Natural pauses while the user answers by voice.
5. Automatic speech-to-text transcript.
6. Interviewer asks follow-up questions based on the answer.
7. Interviewer can interrupt, change subject, ask for a derivation, or ask for a simpler explanation.
8. User may say “I don’t know,” request the question again, or ask for a moment.
9. Interview continues until the selected duration ends.
10. The board closes formally and generates a post-mortem.

Voice-to-voice requires an optional AI endpoint or local model. The offline core must remain available as typed practice and browser speech-synthesis practice.

## Duration presets

- Warm-up: 5 minutes
- Mini interview: 15 minutes
- ISRO-style practice: 30 minutes
- DRDO-style practice: 30–40 minutes
- BARC-style technical grill: 45–90 minutes
- Research-institute interview: 30–60 minutes
- Private-space technical interview: 30–45 minutes
- Custom duration

The duration is a training preset, not a claim that every real panel follows exactly that format.

## Mode profiles

Mode profiles must be labelled **training simulations based on publicly described tendencies and user-provided preferences, not exact replicas or leaked panels**.

### ISRO mode

Emphasis:

- Favourite subjects and fundamentals
- Project explanation
- Space and mission awareness
- Optics, electronics, EM, mechanics, materials, orbital basics depending on user profile
- Calm technical probing
- Practical engineering relevance
- Teamwork, service, and posting questions

Style:

- Begins formally and generally
- Moves from introduction to project or declared subject
- Tests fundamentals through follow-ups
- May pivot to organization awareness
- Values concise, technically grounded answers

### BARC/DAE mode

Emphasis:

- First-principles derivations
- Quantum, nuclear, thermodynamics, statistical physics, solid state, EM
- Radiation, detectors, reactor and safety basics where relevant
- Rapid transitions between easy basics and deep derivations
- Assumptions, limiting cases, and physical interpretation

Style:

- Technical grill with repeated why questions
- May ask the candidate to derive rather than recite
- May return to a basic question after a difficult one
- Tests stamina and recovery from uncertainty

### DRDO mode

Emphasis:

- Fundamentals plus application
- Electronics, EM, radar, sensors, signal processing, materials, optics, instrumentation
- Reliability, testing, constraints, defence relevance, and systems thinking
- Project troubleshooting and practical decision-making

Style:

- Mixes technical questions with applied scenarios
- May challenge the candidate’s confidence
- May ask what changes in real operating conditions
- Tests whether science can become dependable technology

### IIA mode

Emphasis:

- Astronomy and astrophysics
- Observational methods
- Telescopes, detectors, spectroscopy, data analysis
- Mathematical and physical reasoning
- Scientific curiosity and research maturity
- Proposed research interests

Style:

- Research-conversation format with technical depth
- May ask what the candidate would measure and why
- Values uncertainty, evidence, literature awareness, and original questions

### IUCAA mode

Emphasis:

- Astrophysics and cosmology fundamentals
- Mathematical reasoning
- Gravitation, relativity basics, stellar and galactic systems
- Data analysis and computational thinking
- Research motivation and readiness for advanced study

Style:

- Conceptual and research-oriented
- May probe mathematical assumptions
- May ask the candidate to reason through an unfamiliar problem

### Private-space mode

Emphasis:

- Practical engineering
- Rapid learning
- Testing and validation
- Materials, sensors, payloads, software, electronics, or propulsion according to the selected role
- Trade-offs, cost, reliability, deadlines, and teamwork

Style:

- Project and prototype driven
- May ask what the candidate would build first
- Tests communication with engineers from other disciplines

## Live interviewer behaviours

The AI interviewer should be able to:

- Wait silently for a configurable period
- Ask “Are you sure?”
- Ask “Why?” repeatedly
- Ask for a simpler explanation
- Ask for a limiting case
- Ask for an order-of-magnitude estimate
- Interrupt politely or firmly
- Challenge an unsupported claim
- Switch from project to fundamentals
- Return to an earlier incomplete answer
- Ask the candidate to compare two methods
- Ask the candidate to draw or derive something
- Ask “What would you do if the experiment failed?”
- Ask “What did you personally do?”
- End the interview professionally

The AI must not be abusive, humiliating, or falsely claim to reproduce a real named panel.

## Speech pipeline and realistic interviewer voice

Browser speech synthesis alone may sound robotic and must not be presented as a realistic human interviewer. The voice system must have clear tiers:

### Tier 1 — Browser fallback

- Uses the browser’s available speech-synthesis voices.
- Adjustable voice, rate, pitch, and pause length.
- Fully offline.
- Clearly labelled as fallback quality.

### Tier 2 — Optional natural TTS endpoint

For a genuinely human-like interviewer voice, use an explicitly configured TTS service or a local neural TTS model. The HTML must not embed a secret provider key.

Settings:

- TTS endpoint
- Voice or speaker ID
- Speaking rate
- Warmth/formality slider if supported
- Pause behaviour
- “Speak only the question” option
- Test voice button
- Offline fallback button

The natural voice should speak short interviewer turns rather than long feedback. It should include realistic pauses, varied intonation, professional formality, and mode-specific delivery:

- BARC: precise, restrained, technically intense
- ISRO: formal, calm, mission-oriented
- DRDO: direct, applied, probing
- IIA/IUCAA: thoughtful, research-oriented
- Private space: energetic but technically focused

### Transcript and question flow

1. Browser microphone captures speech.
2. Speech recognition produces a transcript.
3. Transcript is sent only if the user has enabled the AI endpoint.
4. AI returns the next question.
5. Natural TTS endpoint speaks the question if configured.
6. Browser synthesis is used only as fallback.
7. Transcript and timing are logged locally.

The app must show the current voice tier visibly, for example:

```text
VOICE: Natural TTS endpoint
VOICE: Browser fallback
VOICE: Typed-only mode
```

No voice should claim to be an actual employee or reproduce a specific real interviewer. It is a realistic training persona, not impersonation.

The system needs:

- Start/stop microphone button
- Push-to-talk option
- Automatic voice activity timeout
- “Repeat question” command
- “Give me a moment” command
- Typed fallback
- Recognition failure recovery
- Visible listening/thinking/speaking states
- Transcript correction before submission where practical

The AI should not speak long feedback during the interview. Detailed feedback belongs in the post-mortem.

## Derivation and image response mode

During a live board, the interviewer may say:

- “Derive it.”
- “Draw the graph.”
- “Sketch the potential.”
- “Show the orbit.”
- “Plot the expected trend.”
- “Write the free-body diagram.”

The user must be able to:

- Open a blank drawing canvas
- Draw with mouse, trackpad, stylus, or touchscreen
- Add text labels
- Erase and undo
- Upload an image
- Paste an image directly from the clipboard
- Drag and drop an image
- Photograph handwritten work if the browser permits camera access
- Submit the image to the AI only after explicit confirmation

Image review should return:

- What the drawing appears to show
- Correct elements
- Missing labels or steps
- Mathematical or physical errors
- A follow-up question
- A corrected sketch description
- Confidence and uncertainty

Vision review must be labelled approximate. Handwriting, low resolution, glare, and ambiguous diagrams can cause errors. The user should always be able to ask for a text-based review instead.

## Live-board transcript and post-mortem

Save locally:

- Start and end time
- Mode and duration
- Every question
- Every transcript
- User pauses
- Interruptions
- Uploaded drawing references if the user chooses to retain them
- AI feedback
- Missed follow-ups
- Final scores

Post-mortem categories:

- Technical correctness
- Depth
- Structure
- Project ownership
- Communication
- Composure
- Recovery
- Diagram quality
- Honesty
- Organization awareness

## Live AI privacy rules

- Voice-to-voice is opt-in.
- The microphone is visibly active only while listening.
- No audio or transcript is uploaded without a clear setting.
- Project images are never uploaded by default.
- The user confirms before sending each image if privacy mode is enabled.
- No API key is stored in the HTML or localStorage.
- The user can delete transcripts and images.
- Offline typed mode remains available.
- The AI must not be described as an actual ISRO, DRDO, BARC, IIA, IUCAA, or NASA interviewer.

# 8. FINAL DOCTRINE

The objective is not to sound like a memorised coaching book. The objective is to become someone who:

- Understands fundamentals
- Explains clearly
- Thinks when surprised
- Knows the limits of their knowledge
- Defends their own work honestly
- Learns from mistakes
- Handles pressure without collapsing
- Connects science to mission
- Can work as part of a disciplined team

MISSION VIVA should make the user more prepared, not falsely overconfident.

> Build the rank. Build the fundamentals. Build the voice. Defend the work. Walk into the room as a scientist in training—not as someone pretending to know everything.
