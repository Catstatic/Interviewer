# MISSION VIVA — CONTENT MASTER SPECIFICATION
## Full interview-day knowledge system for a fifth-year BS-MS Physics student at IISER Thiruvananthapuram
### Targets: ISRO · BARC/DAE · DRDO · IIA · IUCAA · CSIR labs · Bengaluru private-space organizations

> This document defines the **Content Armory** that must be added to `mission-viva.html`. It is deliberately broader than a question bank. Every topic must be taught at interview depth: concept, equation, physical meaning, assumptions, limiting cases, derivation, experiment, application, traps, and oral explanation.

> **Important:** No file can contain literally every fact in physics or guarantee selection. The target is complete coverage of the trainable interview core and a reliable method for handling unfamiliar questions.

---

# 1. CONTENT FORMAT FOR EVERY TOPIC

Every topic card in the HTML must contain these tabs:

1. **One-minute core** — what the concept means in plain language.
2. **Prerequisites** — mathematics and earlier ideas required.
3. **Definitions** — precise but interview-friendly.
4. **Equations** — symbols, units, and physical interpretation.
5. **Derivation** — assumptions shown step by step.
6. **Limiting cases** — what happens when a parameter is very small or large.
7. **Experiments** — what is measured and what the result means.
8. **Applications** — ISRO, DRDO, BARC, astronomy, materials, or instruments.
9. **Rapid questions** — short answers.
10. **Deep questions** — panel-level follow-ups.
11. **Traps** — common wrong answers.
12. **Speak it** — 30-second, 90-second, and 3-minute explanation.
13. **Draw it** — required diagrams and graphs.
14. **Derive it** — chalkboard version.
15. **Flashcards** — definitions, formulae, units, and exceptions.
16. **Readiness gate** — cannot be marked ready until the user passes oral checks.

Every fact that can become stale must have `sourceNote` and `verifiedOn`. Stable physics does not need web verification; current missions, organizations, eligibility, and dates do.

---

# 2. MATHEMATICAL FOUNDATION

## 2.1 Units and dimensions

Must know:

- SI base quantities and derived units
- Dimensional homogeneity
- Significant figures
- Order-of-magnitude estimation
- Unit conversion
- Natural units in nuclear/particle physics
- Common traps: radians dimensionless, Hz = s⁻¹, eV as energy, tesla and weber relation

Interview drills:

- Check whether an equation is dimensionally valid.
- Estimate escape speed, thermal wavelength, orbital period, or detector count rate.
- Explain why dimensional analysis cannot determine dimensionless constants.

## 2.2 Vectors and vector calculus

Must know:

- Dot and cross products
- Gradient, divergence, curl, Laplacian
- Physical interpretation of each
- Line, surface, and volume integrals
- Gauss theorem
- Stokes theorem
- Conservative fields
- Irrotational and solenoidal fields
- Coordinate systems: Cartesian, cylindrical, spherical
- Jacobians and volume elements

## 2.3 Linear algebra

Must know:

- Vectors, basis, dual vectors
- Matrices and transformations
- Eigenvalues/eigenvectors
- Hermitian and unitary matrices
- Orthogonality and completeness
- Diagonalization
- Degeneracy
- Inner products
- Why quantum observables use Hermitian operators

## 2.4 Differential equations and transforms

Must know:

- First- and second-order ODEs
- Boundary and initial conditions
- Separation of variables
- Fourier series and Fourier transform
- Laplace transform basics
- Green functions concept
- PDE classification
- Wave, diffusion, and Laplace equations
- Physical meaning of frequency and spatial modes

## 2.5 Probability and statistics

Must know:

- Random variables and distributions
- Mean, variance, covariance
- Gaussian, Poisson, binomial, exponential distributions
- Central limit theorem
- Maximum likelihood
- Least squares
- Error bars and confidence intervals
- Correlation versus causation
- Propagation of uncertainty

---

# 3. CLASSICAL MECHANICS

## 3.1 Newtonian mechanics

Must know:

- Inertial frames
- Newton’s laws and free-body diagrams
- Constraints and normal forces
- Friction and drag
- Work-energy theorem
- Conservative forces and potential energy
- Linear momentum and centre of mass
- Angular momentum and torque
- Collisions
- Small oscillations
- Central-force motion

Core equations:

- `F = ma`
- `W = ∫F · dr`
- `K = 1/2 mv²`
- `p = mv`
- `τ = r × F`
- `L = r × p`
- `E = K + V`

Deep questions:

- Why is angular momentum conserved?
- What changes in a non-inertial frame?
- Why can potential energy be defined only for conservative forces?
- Why does a central force imply planar motion?

## 3.2 Rotating frames

Must know:

- Coriolis force
- Centrifugal force
- Euler force
- Foucault pendulum concept
- Earth rotation and projectile deviation
- Difference between real and fictitious forces

## 3.3 Lagrangian mechanics

Must know:

- Generalized coordinates
- Principle of stationary action
- Lagrangian `L = T − V`
- Euler-Lagrange equation
- Cyclic coordinates
- Generalized momentum
- Constraints
- Noether connection between symmetry and conservation laws

## 3.4 Hamiltonian mechanics

Must know:

- Hamiltonian `H = Σpᵢq̇ᵢ − L`
- Hamilton’s equations
- Phase space
- Poisson brackets
- Relation to quantum commutators
- Why Hamiltonian is often total energy but not always

## 3.5 Oscillations and waves

Must know:

- SHM
- Damped oscillator
- Driven oscillator
- Resonance
- Quality factor
- Coupled oscillators
- Normal modes
- Dispersion
- Group and phase velocity
- Standing waves

Required diagrams:

- Potential near equilibrium
- Damped oscillation
- Resonance curve
- Phase-space ellipse
- Standing-wave modes

---

# 4. ELECTROMAGNETIC THEORY

## 4.1 Electrostatics

Must know:

- Charge and Coulomb law
- Electric field and potential
- Superposition
- Gauss law
- Conductors and cavities
- Boundary conditions
- Capacitance and dielectrics
- Energy density
- Method of images
- Multipole expansion basics

Core equations:

- `∇ · E = ρ/ε₀`
- `∇ × E = 0`
- `E = −∇V`
- `U = 1/2 CV²`
- `u_E = 1/2 εE²`

## 4.2 Magnetostatics

Must know:

- Lorentz force
- Biot-Savart law
- Ampere law
- Vector potential
- Magnetic dipole
- Magnetic materials
- Boundary conditions
- Energy and inductance

## 4.3 Maxwell equations

Must know both integral and differential forms:

- Gauss electric
- Gauss magnetic
- Faraday induction
- Ampere-Maxwell law

Must explain:

- Displacement current
- Why electromagnetic waves exist
- Why waves are transverse in source-free vacuum
- Speed of light from ε₀ and μ₀
- Energy and momentum flow

## 4.4 Electromagnetic waves

Must know:

- Plane waves
- Polarization
- Poynting vector
- Radiation pressure
- Reflection and refraction
- Fresnel equations concept
- Total internal reflection
- Wave impedance
- Conductors and skin depth
- Dispersion and absorption

## 4.5 Antennas and propagation

Must know:

- Dipole radiation
- Radiation pattern
- Gain and directivity
- Effective aperture
- Polarization matching
- Friis transmission equation
- Free-space path loss
- Ionospheric effects
- Atmospheric attenuation

---

# 5. OPTICS AND PHOTONICS

## 5.1 Geometrical optics

Must know:

- Reflection and refraction
- Snell law
- Lens equation
- Mirror equation
- Magnification
- Aberrations
- Numerical aperture
- Fibre optics
- Total internal reflection

## 5.2 Wave optics

Must know:

- Coherence
- Superposition
- Young double slit
- Thin-film interference
- Newton rings
- Michelson interferometer
- Fabry-Perot interferometer
- Diffraction
- Single slit
- Grating
- Resolution
- Polarization
- Malus law
- Brewster angle
- Quarter- and half-wave plates

## 5.3 Lasers

Must know:

- Absorption, spontaneous emission, stimulated emission
- Einstein coefficients
- Population inversion
- Pumping
- Metastable states
- Optical cavity
- Threshold gain
- Coherence
- Linewidth
- Laser safety

## 5.4 Photonics and detectors

Must know:

- Photodiode
- Avalanche photodiode
- CCD and CMOS
- Quantum efficiency
- Dark current
- Noise equivalent power
- Responsivity
- Dynamic range
- Cooling
- Spectrometers
- Fibre communications

---

# 6. THERMODYNAMICS

## 6.1 Zeroth and first laws

Must know:

- Thermal equilibrium
- Temperature
- State functions versus path functions
- Heat versus work
- Internal energy
- Enthalpy
- Isothermal, adiabatic, isobaric, isochoric processes
- Reversible and irreversible work
- Open and closed systems

Core equations:

- `dU = δQ − δW`
- `H = U + PV`
- `C_P − C_V = R` for an ideal gas
- Ideal-gas equation

## 6.2 Second law and entropy

Must know:

- Kelvin-Planck and Clausius statements
- Carnot cycle
- Entropy definition
- Clausius inequality
- Entropy generation
- Reversibility
- Statistical meaning of entropy
- Heat engines and refrigerators
- Coefficient of performance

## 6.3 Thermodynamic potentials

Must know:

- Helmholtz free energy
- Gibbs free energy
- Enthalpy
- Natural variables
- Maxwell relations
- Chemical potential
- Phase equilibrium
- Stability criteria

## 6.4 Applications

- Phase transitions
- Clausius-Clapeyron equation
- Heat transfer basics
- Thermal management in spacecraft
- Synthesis temperature and phase formation
- Battery and materials thermodynamics

---

# 7. STATISTICAL MECHANICS

Must know:

- Microstate, macrostate, multiplicity
- Microcanonical, canonical, grand canonical ensembles
- Partition function
- Boltzmann factor
- Maxwell-Boltzmann distribution
- Bose-Einstein statistics
- Fermi-Dirac statistics
- Chemical potential
- Equipartition theorem
- Density of states
- Fermi energy
- Degenerate gas
- Fluctuations
- Thermodynamic limit

Required derivations:

- Entropy from multiplicity
- Canonical distribution
- Energy from partition function
- Ideal-gas partition function
- Fermi energy of free electron gas
- Low-temperature heat capacity concept

---

# 8. QUANTUM MECHANICS

## 8.1 Foundations

Must know:

- State vector and wavefunction
- Born interpretation
- Normalization
- Operators and observables
- Hermitian operators
- Eigenvalues and eigenstates
- Expectation values
- Commutators
- Uncertainty principle
- Time evolution
- Schrödinger equation

## 8.2 Standard systems

- Infinite square well
- Finite square well
- Harmonic oscillator
- Free particle
- Tunnelling
- Potential step and barrier
- Hydrogen atom
- Angular momentum
- Spin-1/2
- Identical particles

## 8.3 Deeper concepts

- Degeneracy
- Parity
- Stationary states
- Superposition
- Measurement
- Compatible observables
- Perturbation theory basics
- Variational principle
- WKB concept
- Selection rules

## 8.4 Interview traps

- A wavefunction is not simply a classical physical wave.
- Uncertainty is not merely poor instrument accuracy.
- Measurement probability is `|ψ|²`, not `ψ`.
- Energy eigenstates can be stationary while the wavefunction has a time phase.
- Tunnelling does not violate energy conservation.

---

# 9. ATOMIC AND MOLECULAR PHYSICS

Must know:

- Rutherford scattering
- Bohr model and limitations
- Hydrogen spectrum
- Quantum numbers
- Spin and orbital angular momentum
- Zeeman and Stark effects
- Fine and hyperfine structure
- Selection rules
- Molecular rotation and vibration
- Born-Oppenheimer approximation
- Molecular spectra
- Lasers and spectroscopy

Applications:

- Spectroscopic material characterization
- Remote sensing
- Astrophysical composition
- Laser systems
- Atomic clocks

---

# 10. SOLID STATE, CONDENSED MATTER, AND MATERIALS

This is the most important project-linked content area for the user.

## 10.1 Crystal structure

Must know:

- Lattice, basis, unit cell
- Bravais lattices
- Miller indices
- Packing fraction
- Coordination number
- Primitive and conventional cells
- Reciprocal lattice
- Brillouin zone

## 10.2 Diffraction

Must know:

- Bragg law
- Laue condition
- Reciprocal-space interpretation
- Peak position
- Peak intensity
- Peak width
- Crystallite size
- Strain broadening
- Instrument broadening
- Phase identification limitations

## 10.3 Band theory

Must know:

- Free electron model
- Nearly free electron idea
- Tight-binding idea
- Valence and conduction bands
- Direct and indirect band gaps
- Fermi level
- Intrinsic and extrinsic semiconductors
- Donors and acceptors
- Carrier concentration
- Mobility
- Hall effect

## 10.4 Defects and real materials

Must know:

- Vacancies
- Interstitials
- Substitutional defects
- Dislocations
- Grain boundaries
- Stacking faults
- Surface defects
- Diffusion
- Nucleation and growth
- Phase diagrams
- Grain size and properties

## 10.5 Magnetism and superconductivity

Must know:

- Diamagnetism
- Paramagnetism
- Ferromagnetism
- Antiferromagnetism
- Domains
- Hysteresis
- Exchange interaction
- Curie law
- Meissner effect
- Critical field and temperature

## 10.6 Characterization master list

For every technique, learn: principle, signal, sample requirement, output, resolution, calibration, limitation, and what claim it supports.

### XRD

- Crystal structure and phase
- Bragg law
- Rietveld/refinement concept
- Crystallite size versus particle size
- Peak broadening
- Preferred orientation

### SEM

- Electron beam and secondary/backscattered electrons
- Surface morphology
- Resolution and charging
- Coating
- Vacuum

### TEM

- Transmission and electron diffraction
- Nanostructure and lattice fringes
- Sample thickness and preparation

### EDS/EDX

- Characteristic X-rays
- Elemental composition
- Detection limits
- Quantification limitations

### AFM

- Tip-sample interaction
- Contact/tapping modes
- Surface topography
- Roughness

### Raman

- Inelastic scattering
- Vibrational fingerprints
- Laser wavelength
- Fluorescence and heating

### FTIR

- Molecular vibrations
- Functional groups
- Absorption bands
- Sample preparation

### UV-Vis

- Absorption and transmission
- Band gap estimation
- Beer-Lambert law
- Tauc plot limitations

### XPS

- Photoelectric effect
- Surface composition
- Chemical states
- Binding energy calibration

### TGA/DSC

- Mass loss
- Phase transitions
- Decomposition
- Endothermic/exothermic processes

### Electrical and magnetic measurements

- Four-probe method
- Contact resistance
- I-V curves
- Hall measurement
- VSM and hysteresis
- Temperature dependence

## Project defence requirements

The user must never say “XRD proves the material is good.” Instead:

> “XRD can support phase and crystallinity claims. I would combine it with composition, morphology, and property measurements before making a broader conclusion.”

---

# 11. NUCLEAR PHYSICS AND RADIATION

## 11.1 Nuclear structure

Must know:

- Nuclear size
- Nucleons
- Isotopes, isotones, isobars
- Nuclear force
- Binding energy
- Mass defect
- Semi-empirical mass formula
- Shell model
- Magic numbers
- Spin and parity

## 11.2 Radioactivity

Must know:

- Alpha decay
- Beta decay
- Gamma decay
- Decay constant
- Half-life
- Mean life
- Activity
- Decay chains
- Secular and transient equilibrium

Core equations:

- `N=N₀e^(−λt)`
- `A=λN`
- `T₁/₂=ln2/λ`

## 11.3 Nuclear reactions

Must know:

- Q-value
- Conservation laws
- Cross-section
- Threshold energy
- Compound nucleus
- Fission
- Fusion
- Neutron moderation
- Multiplication factor
- Criticality

## 11.4 Radiation interaction and safety

Must know:

- Alpha, beta, gamma, neutron interactions
- Ionization and excitation
- Attenuation
- Half-value layer
- Absorbed dose
- Equivalent dose
- Effective dose
- Exposure versus contamination
- Time, distance, shielding
- ALARA
- Detector principles

Never give unsafe experimental advice or suggest handling radioactive sources independently.

---

# 12. ELECTRONICS, INSTRUMENTATION, AND SENSORS

Must know:

- Diode and rectifier
- Zener diode
- BJT and MOSFET
- Biasing
- Amplifiers
- Op-amps
- Feedback
- Oscillators
- Filters
- ADC/DAC
- Sampling theorem
- Aliasing
- Noise
- Signal-to-noise ratio
- Grounding and shielding
- Sensors and transducers
- Calibration
- Dynamic range
- Resolution
- Sensitivity
- Linearity
- Hysteresis
- Response time
- Reliability

Applications:

- Satellite sensors
- Payload electronics
- Radar
- Detectors
- Materials characterization
- Space instrumentation

---

# 13. SPACE SCIENCE AND ORBITAL MECHANICS

## 13.1 Orbits

Must know:

- Two-body problem
- Kepler laws
- Orbital elements
- Circular and elliptical orbits
- Specific energy
- Specific angular momentum
- Vis-viva equation
- Escape velocity
- Inclination
- Eccentricity
- Perigee and apogee
- Geostationary orbit
- Sun-synchronous orbit
- Polar orbit

## 13.2 Transfers and operations

- Hohmann transfer
- Plane change
- Phasing orbit
- Rendezvous
- Docking
- Station keeping
- Perturbations
- Atmospheric drag
- J2 effect concept
- Attitude determination
- Attitude control
- Reaction wheels
- Magnetorquers
- Star sensors
- Sun sensors
- Gyroscopes

## 13.3 Spacecraft systems

- Structure
- Thermal control
- Power system
- Communication
- Command and data handling
- Payload
- Propulsion
- Guidance, navigation, and control
- Fault detection and recovery
- Radiation environment
- Vacuum and thermal cycling

## 13.4 Remote sensing

- Electromagnetic spectrum
- Spectral signatures
- Spatial, spectral, radiometric, temporal resolution
- Active and passive sensing
- Radar imaging
- Synthetic aperture radar concept
- Calibration
- Atmospheric correction
- Ground truth

## 13.5 Astronomy

- Celestial sphere and coordinates
- Magnitude and flux
- Blackbody radiation
- Wien law
- Stefan-Boltzmann law
- Spectral classification
- Doppler shift
- Stellar evolution
- HR diagram
- Telescopes
- Angular resolution
- Light gathering power
- Detectors
- Exoplanet methods
- X-ray and radio astronomy
- Solar physics
- Space-weather basics

---

# 14. DRDO-SPECIFIC APPLICATION CONTENT

Must know at interview-survival level:

- Radar range and Doppler
- Antenna gain and beamwidth
- Pulse compression concept
- Range and velocity resolution
- Electronic warfare concept
- Sensors and detection probability
- False alarm and missed detection
- Signal processing basics
- Optoelectronics
- Infrared detectors
- Materials under mechanical/thermal stress
- Reliability and environmental testing
- Systems engineering
- Requirements and verification
- Trade-offs: mass, cost, power, range, resolution, robustness

Answer framework:

> “I would first define the required measurement, identify the dominant noise and environmental constraints, choose a suitable sensor and signal chain, calibrate it, test it against controls, and quantify reliability before claiming performance.”

---

# 15. ISRO-SPECIFIC APPLICATION CONTENT

Must know conceptually:

- Launch vehicle stages
- Solid, liquid, and cryogenic propulsion basics
- Why staging helps
- Payload and orbit trade-offs
- Guidance and navigation
- Telemetry, tracking, and command
- Satellite bus and payload
- Thermal and radiation constraints
- Remote sensing
- Communication satellites
- Navigation systems
- Human-spaceflight safety
- Re-entry and heat shield concept
- Docking concept
- Space debris and collision avoidance
- Current mission awareness from official ISRO sources

Stable official source:

- ISRO missions: https://www.isro.gov.in/Mission.html

Current mission details must be refreshed before interview day.

---

# 16. BARC/DAE-SPECIFIC APPLICATION CONTENT

Must know conceptually:

- Nuclear reactor purpose
- Fission chain reaction
- Criticality
- Moderator
- Control rods
- Coolant
- Reactor kinetics basics
- Fuel cycle concept
- Radioisotopes
- Radiation detection
- Shielding
- Dosimetry
- Radiation protection
- Nuclear safety culture
- Waste-management concepts
- Materials under radiation
- Nuclear instrumentation
- OCES/DGFS facts only from current official notifications

Do not memorize stale recruitment numbers or dates. Verify official BARC/DAE sources immediately before applying or interviewing.

---

# 17. EXPERIMENTAL SCIENCE AND PROJECT MATURITY

Every interview candidate must know:

- How to formulate a hypothesis
- What a control is
- What variables are independent/dependent
- How to plan replicates
- Calibration
- Instrument drift
- Systematic and random error
- Uncertainty propagation
- Significant figures
- Reproducibility
- Repeatability
- Outliers
- Bias
- Data selection
- Negative results
- Research ethics
- Lab safety
- Scientific notebook practice

Project answer structure:

```text
Motivation → Objective → Method → Measurement → Evidence → Limitation → Next step
```

---

# 18. FORMULA AND CONSTANTS VAULT

Include, with units and conditions:

- Newton’s laws
- Work-energy
- Momentum and angular momentum
- SHM
- Wave equation
- Maxwell equations
- Coulomb and Biot-Savart laws
- Lens and grating equations
- Planck relation
- Schrödinger equation
- Uncertainty relation
- Thermodynamic identities
- Carnot efficiency
- Partition function relations
- Fermi energy
- Bragg law
- Hall coefficient
- Radioactive decay
- Binding energy
- Kepler laws
- Vis-viva
- Escape velocity
- Radar range
- Signal-to-noise ratio
- Error propagation

Every formula card must ask:

1. What does each symbol mean?
2. What are the units?
3. What assumptions are used?
4. What happens in a limiting case?
5. What physical experiment could test it?

---

# 19. REQUIRED DIAGRAM LIBRARY

The HTML should embed original SVG diagrams or canvas drawings for:

- Free-body diagrams
- Potential wells
- SHM phase space
- Electric field lines
- Gaussian surface
- Capacitor with dielectric
- Magnetic field around wire/solenoid
- EM wave with E, B, and propagation direction
- Fresnel reflection/refraction
- Thin-film path difference
- Double-slit intensity
- Single-slit diffraction
- Ray diagrams
- Laser cavity
- Crystal lattice
- Miller planes
- Reciprocal lattice
- XRD pattern with indexed peaks
- Band diagrams
- Semiconductor p-n junction
- Hysteresis loop
- Nuclear decay chain
- Reactor schematic at high level
- Detector geometry
- Orbital ellipse
- Hohmann transfer
- Geostationary orbit
- Satellite attitude axes
- Remote-sensing geometry
- Radar pulse and echo
- Telescope aperture and Airy disk
- Blackbody curves
- HR diagram
- Error bars and fit
- TGA/DSC curve
- Raman/FTIR spectrum

All diagrams must be original, labelled, high contrast, printable, and accompanied by “what to say while drawing.”

---

# 20. RESOURCE LIBRARY

Resources are supplements, not replacements for active answering.

## Free textbooks and references

- OpenStax University Physics: https://openstax.org/details/books/university-physics
- OpenStax Volume 1: https://openstax.org/books/university-physics-volume-1/pages/1-introduction
- Feynman Lectures: https://www.feynmanlectures.caltech.edu/
- HyperPhysics: http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html
- PhET simulations: https://phet.colorado.edu/

OpenStax University Physics is organised across mechanics/waves, thermodynamics/electricity/magnetism, and optics/modern physics, making it useful as a structured foundation. [OpenStax scope](https://openstax.org/books/university-physics-volume-1/pages/preface)

## University-level courses

- MIT OpenCourseWare Physics: https://ocw.mit.edu/search/?d=Physics
- MIT Classical Mechanics: https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/
- MIT Electricity and Magnetism: https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/
- MIT Quantum Physics: https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2013/
- NPTEL courses: https://nptel.ac.in/courses
- NPTEL physics catalogue: https://nptel.ac.in/courses/discipline/115

NPTEL currently lists courses in foundations of electrodynamics, wave optics, quantum mechanics, solid state physics, nuclear physics, atomic/molecular physics, thermodynamics, statistical mechanics, and scientific computing. [NPTEL catalogue](https://nptel.ac.in/courses)

## Video learning

The HTML should link to official or stable course pages rather than hard-code random YouTube videos. YouTube links can disappear or change. Use:

- NPTEL official channel/search: https://www.youtube.com/@nptelhrd
- MIT OpenCourseWare YouTube: https://www.youtube.com/@mitocw
- Khan Academy Physics: https://www.youtube.com/@khanacademy
- Fermilab: https://www.youtube.com/@Fermilab
- NASA: https://www.youtube.com/@NASA
- ISRO official: https://www.youtube.com/@isroofficial5866

Each video resource in the HTML must include:

- Topic
- Level
- What to watch for
- Approximate duration
- Whether it is conceptual or problem-solving
- Last checked date

## Official organization sources

- ISRO missions: https://www.isro.gov.in/Mission.html
- ISRO main site: https://www.isro.gov.in/
- BARC: https://www.barc.gov.in/
- DAE: https://dae.gov.in/
- DRDO: https://www.drdo.gov.in/
- RAC: https://rac.gov.in/
- CSIR: https://www.csir.res.in/
- CSIR-NIIST: https://www.niist.res.in/
- IIA: https://www.iiap.res.in/
- RRI: https://www.rri.res.in/
- IUCAA: https://www.iucaa.in/

Official sources must be preferred for recruitment, mission status, centre roles, and current programmes.

---

# 21. CONTENT STUDY ORDER FOR THIS USER

## Phase A — interview survival foundation

- Units and dimensions
- Vectors
- Mechanics
- Thermodynamics
- EM basics
- Optics basics
- Quantum foundations
- Solid-state basics
- Experimental uncertainty

## Phase B — declared subjects

Recommended declared subjects:

- Optics
- Thermodynamics
- Basic Electronics

Project-linked preparation:

- Solid State Physics
- Materials characterization
- Experimental methods

## Phase C — organization breadth

- ISRO space systems and missions
- DRDO radar/sensors/materials
- BARC nuclear/radiation/safety
- Astronomy and instrumentation
- Bengaluru private-space roles

## Phase D — deep board training

- Derive 50 results
- Complete 100 rapid questions
- Complete 30 project questions
- Complete three full boards
- Practise recovery after unknown questions

---

# 22. THE MINIMUM ANSWER STANDARD

For every technical answer, the user should aim for:

```text
Definition
→ governing principle
→ physical mechanism
→ equation or example
→ assumptions
→ limiting case
→ application or boundary
```

For every project answer:

```text
What problem?
→ what material/system?
→ what method?
→ what measurement?
→ what evidence?
→ what uncertainty?
→ what did I personally do?
→ what next?
```

For every current-affairs answer:

```text
Stable fact
→ current detail only if verified
→ relevance to the organization
→ honest uncertainty if needed
```

---

# 23. CONTENT BUILD REQUIREMENTS FOR THE HTML

The next HTML content build must add:

- A searchable Content Library
- Topic filters
- Difficulty filters
- Organization filters
- “Teach me” mode
- “Test me” mode
- “Explain aloud” mode
- “Draw this” mode
- “Derive this” mode
- Resource links
- Embedded SVG diagrams
- Formula cards
- Prerequisite graph
- Progress by topic
- Readiness gate per topic
- Offline copies of essential short notes
- External links clearly labelled as requiring internet

The content must be loaded in batches to keep the file usable. The full target is:

- 12 complete topic sheets
- 1,500 interview questions
- 250 trap patterns
- 50 derivations
- 800 flashcards
- 100 diagrams
- 100 resource links with verification dates

---

# FINAL CONTENT DOCTRINE

The app must not encourage passive reading. Every content page must end with:

1. Explain it in one sentence.
2. Derive or sketch it.
3. Give one physical example.
4. State one assumption.
5. State one limitation.
6. Answer one follow-up why.
7. Connect it to project, space, defence, nuclear science, or astronomy.

> The goal is not to know a textbook by heart. The goal is to understand enough that a panel can move from a basic question to a deep question without making you collapse.
