#!/usr/bin/env python3
"""Build 64 original, concept-specific SVG references for the Visual Library."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "content" / "visual-extensions.json"
REVIEWED_ON = "2026-08-15"

# Every entry is a distinct scientific communication task. Reused rendering grammar is
# intentional (board consistency); titles, relationships, labels, scripts, and checks differ.
DIAGRAMS = [
    # Solid state — 5
    ("Solid State Physics", "Direct and reciprocal lattice mapping", "flow", ["direct vectors aᵢ", "Fourier phase", "reciprocal vectors bᵢ", "Bragg vector G"], "Start with real-space translations. Reciprocal vectors encode phase periodicity, and diffraction selects scattering-vector changes equal to reciprocal-lattice vectors."),
    ("Solid State Physics", "Point, line, and planar crystal defects", "compare", [("point", "vacancy / interstitial"), ("line", "dislocation"), ("planar", "grain boundary")], "Classify defects by dimensionality, then connect each to strain, diffusion, scattering, and the property being measured."),
    ("Solid State Physics", "Hall-bar geometry and sign convention", "setup", [("current I",100,160),("sample",300,160),("B ⊙",300,65),("Hall V_H",500,160)], [(0,1),(1,3),(2,1)], "Define current, magnetic-field direction, charge sign, and voltage leads before interpreting the Hall sign; multiband materials require a richer model."),
    ("Solid State Physics", "Acoustic and optical phonon branches", "graph", ("wavevector k", "frequency ω", [([(.05,.05),(.25,.25),(.5,.48),(.75,.66),(.95,.72)], "acoustic"),([(.05,.78),(.25,.80),(.5,.82),(.75,.83),(.95,.84)], "optical")]), "Acoustic frequency tends to zero at long wavelength, while an optical branch can remain finite when the basis has relative motion."),
    ("Solid State Physics", "Magnetic hysteresis quantities", "graph", ("field H", "magnetization M", [([(.05,.45),(.15,.2),(.35,.12),(.75,.18),(.94,.43),(.82,.78),(.62,.88),(.22,.82),(.05,.55)], "loop")]), "Mark saturation, remanence, coercive field, sweep direction, and background. A loop alone does not prove intrinsic ferromagnetism."),
    # Materials — 5
    ("Materials Characterization", "Raman and infrared selection-rule comparison", "compare", [("Raman", "polarizability change"), ("FTIR", "dipole-moment change"), ("both", "frequency + symmetry + geometry")], "Both probe vibrational evidence, but their selection rules and artifacts differ; agreement is complementary rather than automatic molecular proof."),
    ("Materials Characterization", "UV–Vis signal-to-gap inference", "flow", ["dark + reference", "T / R signal", "optical model", "absorption α", "edge fit + uncertainty"], "A detector signal becomes a gap estimate only through reference, geometry, thickness, scattering, transition model, fit range, and uncertainty."),
    ("Materials Characterization", "XPS photoelectron energy balance", "setup", [("photon hν",90,80),("surface",285,160),("electron E_K",470,80),("analyser Φ",520,230)], [(0,1),(1,2),(2,3)], "Use energy conservation E_B equals photon energy minus kinetic energy and analyser work-function term; then state charge referencing and surface sensitivity."),
    ("Materials Characterization", "TGA and DSC complementary traces", "graph", ("temperature T", "normalized signal", [([(.05,.82),(.35,.82),(.48,.58),(.65,.58),(.76,.3),(.95,.3)], "mass"),([(.05,.5),(.35,.5),(.47,.16),(.58,.5),(.75,.85),(.86,.5),(.95,.5)], "heat flow")]), "TGA tracks mass while DSC tracks differential heat flow. Align temperature, atmosphere, rate, baseline, and thermal history before assigning events."),
    ("Materials Characterization", "Claim–evidence matrix for a material", "flow", ["structure: XRD", "composition: EDS/XPS", "morphology: microscopy", "property: functional test", "claim boundary"], "Each technique supports a different clause of a material claim; finish by naming detection limits, sampling scale, and unresolved alternatives."),
    # Optics — 5
    ("Optics and Lasers", "Young double-slit geometry and fringe scale", "setup", [("source",70,160),("slits d",230,160),("screen L",550,160),("point y",550,80)], [(0,1),(1,2),(1,3)], "Label slit separation, screen distance, observation coordinate, path difference, and the small-angle condition before writing fringe spacing."),
    ("Optics and Lasers", "Polarizer and wave-plate axes", "setup", [("linear E",80,160),("polarizer P",220,160),("λ/4 axes",370,160),("ellipse",540,160)], [(0,1),(1,2),(2,3)], "Track amplitudes along fast and slow axes and their relative phase; a quarter-wave plate gives circular output only for equal components and the required phase delay."),
    ("Optics and Lasers", "Fibre acceptance cone and numerical aperture", "setup", [("acceptance cone",100,160),("core n₁",300,150),("cladding n₂",300,230),("guided ray",520,160)], [(0,1),(1,3)], "Apply refraction at the entrance and total internal reflection at the core–cladding boundary, stating n_core greater than n_clad and the external medium."),
    ("Optics and Lasers", "Airy pattern and Rayleigh separation", "graph", ("image angle", "intensity", [([(.05,.06),(.15,.1),(.23,.22),(.32,.82),(.40,.22),(.48,.08),(.56,.05)], "source A"),([(.32,.05),(.40,.08),(.48,.22),(.57,.82),(.65,.22),(.74,.1),(.84,.06)], "source B")]), "A finite circular aperture creates point-spread functions; Rayleigh is a stated criterion, while aberration, sampling, and signal-to-noise also matter."),
    ("Optics and Lasers", "Photodiode measurement chain", "flow", ["photon flux", "absorption + η", "photocurrent", "transimpedance", "ADC + calibration"], "Follow photons to charge and voltage. Responsivity, dark current, shot/electronic noise, bandwidth, saturation, and calibration set the usable measurement."),
    # Thermodynamics — 5
    ("Thermodynamics", "Isothermal and adiabatic P–V paths", "graph", ("volume V", "pressure P", [([(.12,.88),(.25,.63),(.45,.4),(.7,.25),(.92,.18)], "isothermal"),([(.12,.88),(.25,.55),(.45,.29),(.7,.14),(.92,.08)], "adiabatic")]), "For expansion from one state, the reversible adiabatic pressure drops faster than the isothermal path; area under a stated path is boundary work."),
    ("Thermodynamics", "T–S heat-transfer view of a cycle", "graph", ("entropy S", "temperature T", [([(.2,.25),(.2,.78),(.78,.78),(.78,.25),(.2,.25)], "reversible cycle")]), "On a reversible path, area under T dS is heat. Label direction and reservoirs before interpreting enclosed area as net work for a cycle."),
    ("Thermodynamics", "Binary phase diagram reading", "graph", ("composition x_B", "temperature T", [([(.05,.82),(.3,.65),(.5,.5),(.7,.65),(.95,.82)], "liquidus"),([(.05,.82),(.3,.42),(.5,.3),(.7,.42),(.95,.82)], "solidus")]), "Read phase fields, tie line, and phase fractions at a stated overall composition; do not infer kinetics or microstructure from equilibrium boundaries alone."),
    ("Thermodynamics", "Gibbs free-energy competition", "graph", ("order parameter / composition", "G", [([(.05,.75),(.25,.35),(.5,.22),(.75,.35),(.95,.75)], "phase α"),([(.05,.48),(.25,.32),(.5,.4),(.75,.32),(.95,.48)], "phase β")]), "Stable equilibrium minimizes the appropriate potential under stated constraints; tangent constructions and barriers must not be confused with rate."),
    ("Thermodynamics", "Spacecraft thermal-resistance network", "flow", ["solar / albedo", "surface absorption", "conduction paths", "component node", "radiation to space"], "Write an energy balance at each thermal node with properties, view factors, contact resistance, internal power, transient heat capacity, and boundary uncertainty."),
    # Electronics — 6
    ("Basic Electronics and Instrumentation", "RC charging transient and time constant", "graph", ("time t / RC", "capacitor voltage V_C/V", [([(.05,.02),(.2,.38),(.35,.62),(.55,.82),(.75,.92),(.95,.97)], "charging"),([(.05,.98),(.2,.62),(.35,.38),(.55,.18),(.75,.08),(.95,.03)], "discharging")]), "At one time constant charging reaches about sixty-three percent and discharging falls to about thirty-seven percent under a first-order Thevenin model."),
    ("Basic Electronics and Instrumentation", "Diode I–V operating regions", "graph", ("diode voltage V_D", "current I_D", [([(.05,.35),(.42,.42),(.53,.45),(.62,.5),(.72,.62),(.82,.82),(.93,.98)], "forward/reverse")]), "Mark reverse leakage, breakdown caution, forward exponential region, series resistance, temperature dependence, and the actual operating load line."),
    ("Basic Electronics and Instrumentation", "Transistor bias point and load line", "graph", ("collector voltage V_CE", "collector current I_C", [([(.08,.88),(.92,.1)], "load line"),([(.12,.15),(.3,.42),(.5,.58),(.72,.66),(.9,.69)], "output curve")]), "Bias chooses a quiescent point with gain and headroom. Show cutoff, active region, saturation, thermal drift, and signal excursion."),
    ("Basic Electronics and Instrumentation", "First-order low-pass Bode magnitude", "graph", ("log frequency", "gain dB", [([(.05,.85),(.35,.84),(.5,.78),(.65,.55),(.8,.3),(.95,.08)], "magnitude")]), "Mark the minus-three-decibel corner and the asymptotic roll-off; component tolerances, loading, op-amp bandwidth, and alias control affect the real response."),
    ("Basic Electronics and Instrumentation", "Sampling and alias folding", "graph", ("frequency", "spectral amplitude", [([(.08,.05),(.2,.75),(.32,.05),(.68,.05),(.8,.75),(.92,.05)], "replicas"),([(.45,.05),(.5,.6),(.55,.05)], "aliased component")]), "Sampling replicates spectra around multiples of the sampling frequency; frequencies above Nyquist can fold unless analog filtering and bandwidth assumptions hold."),
    ("Basic Electronics and Instrumentation", "Ground, shield, and differential signal path", "setup", [("sensor",80,140),("twisted pair",250,140),("differential input",450,140),("shield → chassis",270,245)], [(0,1),(1,2),(3,2)], "Separate signal return, protective/chassis connection, and cable shield. Draw the intended current path and identify where a ground loop or capacitive pickup can enter."),
    # Math/data — 5
    ("Mathematical Foundations, Data, and Uncertainty", "Gauss and Stokes orientation map", "compare", [("Gauss", "volume ↔ closed-surface flux"), ("Stokes", "surface ↔ boundary circulation"), ("orientation", "outward normal / right hand")], "State the region, boundary, orientation, smoothness, and singularities; the integral theorems connect local derivatives to global measurements."),
    ("Mathematical Foundations, Data, and Uncertainty", "Time-domain pulse and Fourier bandwidth", "compare", [("short pulse", "broad frequency content"), ("long pulse", "narrow frequency content"), ("finite window", "leakage / resolution")], "A function and its transform describe the same signal in conjugate domains; finite duration and sampling introduce resolution and aliasing qualifications."),
    ("Mathematical Foundations, Data, and Uncertainty", "Uncertainty-budget dependency tree", "flow", ["measurand", "calibration", "repeatability", "environment/model", "covariance → combined u"], "List contributors with units and sensitivity coefficients, include covariance, and state whether the reported interval is standard or expanded uncertainty."),
    ("Mathematical Foundations, Data, and Uncertainty", "Dimensional scaling and nondimensional groups", "flow", ["variables + units", "dimension matrix", "null-space groups Π", "regime comparison", "experiment collapse"], "Dimensional analysis constrains form and organizes regimes but cannot determine every numerical constant or replace governing physics."),
    ("Mathematical Foundations, Data, and Uncertainty", "Eigenvectors as invariant directions", "setup", [("input vector",100,160),("linear map A",300,160),("λv",510,160),("other direction rotates",300,60)], [(0,1),(1,2),(3,1)], "An eigenvector keeps its direction under a linear map up to scaling; basis completeness, degeneracy, conditioning, and physical inner product still matter."),
    # Mechanics — 5
    ("Classical Mechanics and Oscillations", "Rotating-frame acceleration terms", "flow", ["inertial acceleration", "relative acceleration", "Coriolis 2Ω×v", "centrifugal Ω×(Ω×r)", "Euler dΩ/dt×r"], "Define the rotating origin and angular velocity first, then add translational, Coriolis, centrifugal, and Euler terms with signs consistent with the chosen equation."),
    ("Classical Mechanics and Oscillations", "Torque and angular-momentum balance", "setup", [("origin O",90,230),("position r",250,150),("force F",420,70),("torque r×F",500,220)], [(0,1),(1,2),(1,3)], "Angular momentum and torque require a specified origin and frame. Only the force component perpendicular to position contributes to torque."),
    ("Classical Mechanics and Oscillations", "Underdamped, critical, and overdamped response", "graph", ("time", "displacement", [([(.05,.8),(.18,.3),(.3,.6),(.42,.42),(.56,.52),(.72,.47),(.93,.5)], "underdamped"),([(.05,.8),(.22,.58),(.42,.51),(.7,.5),(.95,.5)], "critical"),([(.05,.8),(.25,.7),(.5,.62),(.75,.56),(.95,.53)], "overdamped")]), "Compare overshoot and settling, state the damping ratio, and distinguish critical fastest non-oscillatory return from maximum decay rate in every metric."),
    ("Classical Mechanics and Oscillations", "Two-mass normal-mode patterns", "compare", [("in-phase", "masses move together"), ("out-of-phase", "masses oppose"), ("mode", "fixed amplitude ratio")], "Normal modes are eigenvectors of the coupled linear system. A general motion is a superposition, and symmetry/mass differences change the patterns."),
    ("Classical Mechanics and Oscillations", "Oscillator phase portrait", "graph", ("position x", "velocity v", [([(.1,.5),(.18,.75),(.38,.9),(.62,.9),(.82,.75),(.9,.5),(.82,.25),(.62,.1),(.38,.1),(.18,.25),(.1,.5)], "conservative orbit"),([(.18,.5),(.25,.68),(.43,.76),(.62,.68),(.68,.5),(.6,.38),(.46,.34),(.36,.42),(.38,.52),(.48,.56)], "damped spiral")]), "Closed contours represent conserved-energy oscillation; damping spirals inward. Axes, units, direction, and autonomous-model assumptions are essential."),
    # EM — 5
    ("Electromagnetic Theory", "Gaussian pillbox across an interface", "setup", [("medium 1",160,80),("surface σ",320,160),("medium 2",160,250),("pillbox",480,160)], [(0,1),(2,1),(1,3)], "Shrink a pillbox across the interface to isolate normal flux; state whether the boundary source is free or total charge and which field, E or D, is used."),
    ("Electromagnetic Theory", "Ampère loop through a solenoid", "setup", [("turns nI",130,160),("inside path ℓ",320,105),("outside return",320,235),("B axial",520,105)], [(0,1),(1,3),(2,0)], "The ideal long-solenoid result follows because the inside segment is aligned with nearly uniform field while the outside contribution is neglected."),
    ("Electromagnetic Theory", "Wave reflection and transmission at an interface", "setup", [("incident kᵢ",90,210),("interface",320,160),("reflected kᵣ",110,70),("transmitted kₜ",520,90)], [(0,1),(1,2),(1,3)], "Tangential phase matching gives angle relations; boundary conditions and impedance set amplitudes, polarization dependence, power flow, and possible total internal reflection."),
    ("Electromagnetic Theory", "Skin-depth field decay in a conductor", "graph", ("depth z / δ", "field amplitude", [([(.05,.95),(.2,.68),(.35,.48),(.5,.33),(.68,.2),(.85,.12),(.95,.08)], "exp(−z/δ)")]), "Field amplitude decays exponentially with depth in a good conductor approximation; frequency, conductivity, permeability, phase lag, and geometry define its limits."),
    ("Electromagnetic Theory", "Antenna pattern and link geometry", "setup", [("transmitter G_t",80,160),("range R",300,160),("receiver A_e",520,160),("off-axis loss",300,65)], [(0,1),(1,2),(3,2)], "A link budget combines transmitted power, gain, range spreading, polarization, effective aperture, losses, noise, bandwidth, and required margin."),
    # Quantum — 5
    ("Quantum Mechanics", "Wavefunction, amplitude, and probability density", "compare", [("ψ", "complex amplitude + phase"), ("|ψ|²", "probability density"), ("∫|ψ|² dx", "normalization = 1")], "The wavefunction is not itself a probability; relative phase affects interference, while measurement probabilities come from normalized modulus squared."),
    ("Quantum Mechanics", "Finite-well bound and evanescent tails", "graph", ("position x", "energy / ψ", [([(.08,.78),(.28,.78),(.28,.22),(.72,.22),(.72,.78),(.92,.78)], "potential"),([(.08,.5),(.2,.44),(.3,.35),(.5,.62),(.7,.35),(.8,.44),(.92,.5)], "bound ψ")]), "Finite barriers allow evanescent tails. Apply continuity conditions, distinguish wavefunction from energy, and state parity and normalization."),
    ("Quantum Mechanics", "Spin measurement on a Bloch sphere", "setup", [("state n",320,70),("Bloch centre",320,170),("+z outcome",500,80),("−z outcome",500,245)], [(1,0),(0,2),(1,3)], "A pure spin-half state defines a Bloch direction; measurement along z gives two outcomes with probabilities set by projection, not a pre-existing classical arrow component."),
    ("Quantum Mechanics", "Operator measurement and state update", "flow", ["prepared |ψ⟩", "observable A", "outcome a_n", "projected component", "repeat / new basis"], "Separate ensemble probabilities, individual outcome, and post-measurement state. Degeneracy and the measurement model determine the exact update rule."),
    ("Quantum Mechanics", "Perturbative level shifts and mixing", "compare", [("unperturbed", "Eₙ, basis |n⟩"), ("weak V", "diagonal shift"), ("near degeneracy", "mixing / diagonalize subspace")], "First-order shifts are expectation values only in the appropriate nondegenerate case; near degeneracy requires diagonalizing the perturbation in the relevant subspace."),
    # Statistical mechanics — 5
    ("Statistical Mechanics", "Microstates grouped into a macrostate", "flow", ["many configurations", "same E,V,N", "multiplicity Ω", "entropy k ln Ω", "equilibrium weighting"], "A macrostate fixes coarse constraints while many microstates realize it; entropy depends on the stated counting and ensemble."),
    ("Statistical Mechanics", "Boltzmann weights across energy levels", "graph", ("energy E", "probability p", [([(.08,.92),(.25,.7),(.42,.5),(.6,.34),(.78,.22),(.94,.14)], "e^(−βE)")]), "Canonical probabilities decrease with energy but include degeneracy and normalization. Temperature changes the slope; the partition function generates averages."),
    ("Statistical Mechanics", "Finite-system fluctuation distribution", "graph", ("observable X", "probability density", [([(.05,.05),(.18,.12),(.3,.38),(.42,.75),(.5,.92),(.58,.75),(.7,.38),(.82,.12),(.95,.05)], "near-Gaussian")]), "Fluctuations describe a distribution around an ensemble mean, not instrument error. Width scales with susceptibility and system size under stated conditions."),
    ("Statistical Mechanics", "Density of states by dimensionality", "graph", ("energy E", "density g(E)", [([(.05,.2),(.2,.35),(.4,.5),(.65,.65),(.95,.8)], "3D ∝ √E"),([(.05,.48),(.95,.48)], "2D constant"),([(.05,.9),(.15,.72),(.35,.55),(.65,.43),(.95,.36)], "1D ∝ 1/√E")]), "Density of states follows dispersion and dimensionality; combine it with occupation to calculate particles, energy, and response."),
    ("Statistical Mechanics", "Classical and quantum heat-capacity limits", "graph", ("temperature T", "heat capacity C", [([(.05,.08),(.2,.25),(.4,.55),(.65,.78),(.95,.88)], "quantum mode"),([(.05,.88),(.95,.88)], "classical limit")]), "Quantum modes freeze out when level spacing exceeds thermal energy and approach equipartition only in the appropriate high-temperature limit."),
    # Nuclear — 5
    ("Nuclear Physics and Radiation Protection", "Exponential decay and half-life markers", "graph", ("time t / T₁/₂", "N/N₀", [([(.05,.95),(.2,.7),(.38,.5),(.58,.32),(.78,.2),(.95,.13)], "decay")]), "Each half-life halves the expected surviving population. Individual nuclei remain stochastic, and measured counts also include efficiency, background, and dead time."),
    ("Nuclear Physics and Radiation Protection", "Alpha, beta, gamma, and neutron interactions", "compare", [("α", "dense ionization / short range"), ("β", "ionization + bremsstrahlung"), ("γ", "photon interactions"), ("n", "nuclear scattering / capture")], "Interaction physics differs by radiation and energy; shielding and detection therefore require material, spectrum, geometry, and approved safety analysis."),
    ("Nuclear Physics and Radiation Protection", "Radiation detector pulse chain", "flow", ["energy deposition", "charge / light", "preamplifier", "shaping + ADC", "spectrum + calibration"], "A source does not directly produce a spectrum. Include interaction probability, efficiency, gain, resolution, background, dead time, and calibration."),
    ("Nuclear Physics and Radiation Protection", "Narrow-beam attenuation geometry", "setup", [("source I₀",80,160),("absorber μx",300,160),("detector I",530,160),("scatter rejected",300,60)], [(0,1),(1,2),(1,3)], "The exponential narrow-beam law tracks uncollided intensity under a defined geometry; buildup, broad spectra, secondary radiation, and real shielding need qualified analysis."),
    ("Nuclear Physics and Radiation Protection", "Liquid-drop energy competition", "compare", [("volume", "binding grows with A"), ("surface", "under-bound surface nucleons"), ("Coulomb", "proton repulsion"), ("asymmetry + pairing", "composition / even–odd")], "The semi-empirical terms explain broad mass trends but shell structure and microscopic dynamics remain; use consistent mass conventions in Q values."),
    # Space — 6
    ("Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Specific orbital energy and conic type", "compare", [("ε < 0", "ellipse / circle"), ("ε = 0", "parabolic escape boundary"), ("ε > 0", "hyperbola")], "Classify conics using specific energy under the two-body model, then state how angular momentum sets shape and real perturbations alter the trajectory."),
    ("Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Spacecraft subsystem interface map", "flow", ["payload need", "power + thermal", "ADCS + structure", "C&DH + communications", "FDIR + operations"], "A subsystem cannot be optimized alone. Trace mass, power, heat, data, pointing, timing, contamination, reliability, and test interfaces."),
    ("Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Attitude sensors, estimator, and actuators", "flow", ["stars / Sun / field / gyro", "calibrated sensors", "state estimator", "control law", "wheels / rods / thrusters"], "Determination estimates orientation and rates; control commands actuators. Include frames, sensor biases, observability, momentum management, saturation, and safe mode."),
    ("Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Rocket staging and inert-mass removal", "flow", ["stage 1 burn", "empty hardware", "separation", "stage 2 ignition", "payload injection"], "Staging improves effective mass ratio by discarding inert hardware, at the cost of separation, ignition, structural, guidance, reliability, and integration risk."),
    ("Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Active and passive remote-sensing chains", "compare", [("passive", "Sun/thermal source → target → sensor"), ("active", "transmitter → target → return"), ("both", "calibration + atmosphere + validation")], "Active and passive systems differ in illumination and observables but both require geometry, calibration, processing models, ground truth, and uncertainty."),
    ("Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "SAR range and azimuth geometry", "setup", [("platform velocity",90,70),("slant range",300,145),("ground swath",520,235),("synthetic aperture",220,55)], [(0,1),(1,2),(0,3)], "Range comes from delay and bandwidth; azimuth resolution comes from coherent motion processing. State side-looking geometry, Doppler history, speckle, and calibration."),
    # Role extensions — 2
    ("Astronomy and Astrophysics", "Hertzsprung–Russell diagram reasoning", "graph", ("temperature decreasing →", "luminosity", [([(.12,.85),(.25,.72),(.4,.55),(.58,.4),(.78,.25),(.92,.14)], "main sequence"),([(.18,.92),(.3,.86),(.42,.8)], "giants"),([(.68,.22),(.82,.16),(.92,.1)], "white dwarfs")]), "State the axis conventions: temperature often decreases to the right and luminosity is logarithmic. Regions organize stellar states but do not alone provide an evolutionary track for one star."),
    ("Radar and Microwave Systems", "Pulsed-radar delay and Doppler observables", "setup", [("transmit pulse",80,160),("target",320,160),("echo delay 2R/c",520,100),("phase change → v_r",520,225)], [(0,1),(1,2),(1,3)], "Delay measures slant range and coherent phase evolution measures radial velocity. Distinguish resolution, accuracy, ambiguity, maximum range, clutter, and signal-to-noise."),
]


def svg_base(body: str) -> str:
    return (
        '<svg viewBox="0 0 640 320" role="img" xmlns="http://www.w3.org/2000/svg" '
        'style="max-width:100%;background:#fff;border:1px solid #94a3b8">'
        '<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#0f766e"/></marker></defs>'
        '<rect width="640" height="320" fill="#fff"/>' + body + '</svg>'
    )


def render(kind: str, spec) -> str:
    esc = html.escape
    if kind == "flow":
        labels = spec
        width = 104
        gap = (590 - len(labels) * width) / max(1, len(labels) - 1)
        parts = []
        for i, label in enumerate(labels):
            x = 25 + i * (width + gap)
            parts.append(f'<rect x="{x:.1f}" y="118" width="{width}" height="78" rx="8" fill="#e0f2fe" stroke="#0f172a"/>')
            words = label.split()
            lines = [" ".join(words[j:j+3]) for j in range(0, len(words), 3)][:3]
            for j, line in enumerate(lines):
                parts.append(f'<text x="{x+width/2:.1f}" y="{145+j*17}" text-anchor="middle" font-size="12" fill="#0f172a">{esc(line)}</text>')
            if i < len(labels)-1:
                parts.append(f'<line x1="{x+width:.1f}" y1="157" x2="{x+width+gap-5:.1f}" y2="157" stroke="#0f766e" stroke-width="3" marker-end="url(#arrow)"/>')
        return svg_base("".join(parts))
    if kind == "compare":
        cols = spec
        w = 580 / len(cols)
        parts = []
        for i, (title, detail) in enumerate(cols):
            x = 30 + i*w
            parts.append(f'<rect x="{x:.1f}" y="75" width="{w-12:.1f}" height="170" rx="10" fill="{("#ecfeff" if i%2==0 else "#fef3c7")}" stroke="#0f172a"/>')
            parts.append(f'<text x="{x+(w-12)/2:.1f}" y="115" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">{esc(title)}</text>')
            words = detail.split()
            lines = [" ".join(words[j:j+3]) for j in range(0,len(words),3)][:5]
            for j,line in enumerate(lines):parts.append(f'<text x="{x+(w-12)/2:.1f}" y="150" text-anchor="middle" font-size="12" fill="#334155"><tspan x="{x+(w-12)/2:.1f}" dy="{j*17}">{esc(line)}</tspan></text>')
        return svg_base("".join(parts))
    if kind == "setup":
        nodes, edges = spec
        parts=[]
        for a,b in edges:
            x1,y1=nodes[a][1],nodes[a][2];x2,y2=nodes[b][1],nodes[b][2]
            parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0f766e" stroke-width="3" marker-end="url(#arrow)"/>')
        for label,x,y in nodes:
            parts.append(f'<rect x="{x-58}" y="{y-25}" width="116" height="50" rx="8" fill="#e0f2fe" stroke="#0f172a"/>')
            words=label.split();lines=[" ".join(words[j:j+3]) for j in range(0,len(words),3)][:2]
            for j,line in enumerate(lines):parts.append(f'<text x="{x}" y="{y-2+j*16}" text-anchor="middle" font-size="12" fill="#0f172a">{esc(line)}</text>')
        return svg_base("".join(parts))
    if kind == "graph":
        xlabel,ylabel,curves=spec
        parts=['<line x1="75" y1="270" x2="600" y2="270" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>','<line x1="75" y1="270" x2="75" y2="35" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>',f'<text x="590" y="300" text-anchor="end" font-size="13" fill="#0f172a">{esc(xlabel)}</text>',f'<text x="22" y="40" font-size="13" fill="#0f172a">{esc(ylabel)}</text>']
        colors=['#0f766e','#b45309','#7c3aed','#be123c']
        for i,(points,label) in enumerate(curves):
            coords=" ".join(f'{75+x*525:.1f},{270-y*225:.1f}' for x,y in points)
            parts.append(f'<polyline points="{coords}" fill="none" stroke="{colors[i%len(colors)]}" stroke-width="3"/>')
            lx=470;ly=48+i*21
            parts.append(f'<line x1="{lx}" y1="{ly-4}" x2="{lx+25}" y2="{ly-4}" stroke="{colors[i%len(colors)]}" stroke-width="3"/><text x="{lx+32}" y="{ly}" font-size="12" fill="#0f172a">{esc(label)}</text>')
        return svg_base("".join(parts))
    raise ValueError(kind)


def main() -> None:
    assert len(DIAGRAMS) == 64, len(DIAGRAMS)
    assert len({row[1].lower() for row in DIAGRAMS}) == 64
    records=[]
    for i,row in enumerate(DIAGRAMS,1):
        if len(row) == 6:
            topic,title,kind,nodes,edges,say = row
            spec = (nodes, edges)
        else:
            topic,title,kind,spec,say = row
        svg = render(kind, spec).replace('>', f'><title>{html.escape(title)}</title>', 1)
        records.append({
            "id":f"VIS-EXT-{i:03d}","topic":topic,"title":title,"kind":kind,
            "svg":svg,"say":say,
            "checklist":["Axes, frames, or system boundary are explicit where applicable.","Every arrow and variable has a physical meaning.","Units, scale, sign, or direction convention is stated.","The governing relation and its assumptions are spoken.","One limitation or falsification check is named."],
            "reviewedOn":REVIEWED_ON,"status":"reviewed-original-v1"
        })
    assert len({r["svg"] for r in records}) == 64
    OUTPUT.write_text(json.dumps({"schemaVersion":1,"reviewedOn":REVIEWED_ON,"diagrams":records},ensure_ascii=False,indent=2)+"\n")
    print(f"Wrote {len(records)} original visual references to {OUTPUT}")

if __name__ == "__main__":
    main()
