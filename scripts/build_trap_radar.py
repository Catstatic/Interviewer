#!/usr/bin/env python3
"""Build 250 meaningfully distinct interview trap/recovery records."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "content" / "trap-radar.json"
REVIEWED_ON = "2026-08-15"

# Every tuple is a distinct unsafe/weak answer and a specific recovery.
# Category-level rationale/follow-up is shared intentionally; the trap/recovery pair is not duplicated.
CATEGORY_DATA = [
    ("Formula dumping", "medium", ["formula", "communication"], "A formula without definitions, assumptions, or physical meaning does not demonstrate understanding.", "Define every symbol, state the governing assumption, and explain one limiting case.", [
        ("Writing Maxwell's equations and stopping.", "Name the source represented by each divergence/curl equation and connect them to a measurable field behavior."),
        ("Quoting Carnot efficiency without absolute temperatures.", "State the reversible two-reservoir assumptions and use kelvin before interpreting the bound."),
        ("Stating Bragg's law as proof of phase purity.", "Define theta and d, then separate peak-position evidence from detection limits and complementary composition evidence."),
        ("Writing the Hall coefficient and claiming mobility.", "State the one-carrier model and combine Hall data with conductivity before estimating mobility."),
        ("Quoting the decay law without the constant-hazard assumption.", "Derive dN/dt=-lambda N from a constant independent decay probability and distinguish activity from population."),
        ("Using vis-viva without identifying radius and semimajor axis.", "Define geocentric radius, semimajor axis, gravitational parameter, and the two-body assumption."),
        ("Writing the radar range equation without noise or loss assumptions.", "Explain the outward/return spreading, radar cross section, receive aperture, then list losses and detection criteria."),
        ("Giving uncertainty propagation without covariance.", "State first-order linearization and include covariance terms or justify independence."),
        ("Quoting the lens equation without a sign convention.", "Declare the object/image sign convention and paraxial thin-lens assumptions before substitution."),
        ("Calling the partition function only a normalization constant.", "Show how derivatives of ln Z generate energy, free energy, entropy, or fluctuations under the chosen ensemble.")
    ]),
    ("Units and dimensions", "high", ["units", "numerical"], "A dimensionally inconsistent or unlabeled number can be plausible-looking but physically meaningless.", "Repair the units, show one dimensional check, and report justified significant figures.", [
        ("Reporting escape velocity as 11.2 without units.", "Report approximately 11.2 km/s for the stated Earth-surface idealization and list omitted rotation/atmosphere effects."),
        ("Using altitude directly in a formula requiring orbital radius.", "Add the central-body reference radius and use centre-to-spacecraft distance."),
        ("Putting degrees into a small-angle formula expecting radians.", "Convert to radians and state where sin theta approximately equals theta is used."),
        ("Using peak width in degrees in the Scherrer equation.", "Convert corrected specimen broadening to radians and distinguish coherent-domain size from particle size."),
        ("Mixing centimetres and metres in attenuation exponents.", "Use consistent length units so mu times x is dimensionless."),
        ("Treating electronvolt as voltage.", "Identify eV as an energy and convert with 1 eV equal to elementary charge times one volt when needed."),
        ("Using Celsius in Carnot efficiency.", "Convert reservoir temperatures to kelvin because thermodynamic temperature ratios are required."),
        ("Confusing hertz with radians per second.", "Use omega=2 pi f and keep angular frequency separate from cycles per second."),
        ("Reporting variance with the same units as the measurement.", "Variance has squared units; standard deviation returns to the measurement unit."),
        ("Writing SNR in decibels without defining amplitude or power convention.", "Define the linear SNR, bandwidth, and whether 10 log10 or 20 log10 is appropriate.")
    ]),
    ("Heat and temperature", "medium", ["thermodynamics"], "Heat is boundary energy transfer; temperature is a state variable and neither should be described as a material fluid.", "Separate state from transfer and state the system boundary and process.", [
        ("Saying a hot body contains heat.", "Say the body has internal energy and temperature; heat names energy transferred because of a temperature difference."),
        ("Equating temperature directly with total internal energy.", "State the equation of state and degrees of freedom; internal energy may include many contributions."),
        ("Saying an adiabatic process has constant temperature.", "Adiabatic means no heat transfer; compression or expansion work can change temperature."),
        ("Calling heat capacity the heat stored in an object.", "Define heat capacity as a constrained derivative of energy or enthalpy with temperature."),
        ("Assuming two bodies at equal temperature contain equal energy.", "Equal temperature means thermal equilibrium, not equal mass, heat capacity, or internal energy."),
        ("Using Q as a state function.", "Use delta U, H, or S for state changes and reserve delta Q for path-dependent transfer."),
        ("Saying vacuum prevents spacecraft heating.", "Explain that radiation and internal dissipation remain while external convection is absent."),
        ("Treating a DSC peak as temperature itself.", "Describe differential heat flow versus programmed temperature and calibrate the transition/reaction interpretation."),
        ("Assuming thermal conductivity and diffusivity are the same.", "Relate diffusivity alpha=k/(rho c) and explain the distinct physical roles."),
        ("Calling latent heat a temperature rise.", "Explain energy transfer at coexistence while temperature can remain approximately constant during first-order transition.")
    ]),
    ("Entropy", "medium", ["thermodynamics", "statistics"], "The word disorder hides the thermodynamic definition, system boundary, and entropy-transfer/generation balance.", "Use a state-function, balance, or multiplicity definition with constraints.", [
        ("Defining entropy only as disorder.", "Use dS=delta Q_rev/T or S=k ln Omega under a stated ensemble, then explain the analogy's limits."),
        ("Saying entropy of every system always increases.", "A system entropy may decrease by exporting entropy; isolated total entropy cannot decrease."),
        ("Using delta Q_actual/T as entropy change for an irreversible path.", "Calculate state change with a reversible path or use entropy transfer plus generation."),
        ("Saying reversible means a process can simply be run backwards.", "Require restoration of system and surroundings with zero total entropy generation."),
        ("Assuming quasistatic implies reversible.", "Check friction, viscosity, finite gradients, hysteresis, and other dissipative mechanisms."),
        ("Claiming entropy production can be negative.", "Internal entropy generation is nonnegative; entropy flux can have either direction."),
        ("Ignoring mixing entropy because no heat is exchanged.", "Explain that adiabatic mixing can be irreversible and increase entropy."),
        ("Calling information entropy identical to thermodynamic entropy without a model.", "State the probability/coarse-graining and physical ensemble connecting the two."),
        ("Saying zero-temperature entropy is always exactly zero.", "Invoke the third-law conditions and note residual degeneracy or nonequilibrium exceptions."),
        ("Using entropy increase to predict reaction speed.", "Separate thermodynamic direction from kinetic barriers and transport.")
    ]),
    ("Quantum foundations", "high", ["quantum"], "Classical language can turn amplitudes, states, and measurements into incorrect claims.", "State the Hilbert-space object, Born probability, operator, and measurement assumptions.", [
        ("Calling the wavefunction a directly measurable material wave.", "Describe it as a state amplitude in a chosen basis and connect observables through the Born rule."),
        ("Saying probability equals psi.", "Use modulus squared of the amplitude and normalize the state."),
        ("Treating global and relative phase as equally observable.", "Global phase leaves pure-state predictions unchanged; relative phase controls interference."),
        ("Saying uncertainty is only instrument error.", "Define state spreads of noncommuting observables and separate apparatus uncertainty."),
        ("Writing delta x delta p equals hbar/2 for every state.", "Use the inequality and state that equality occurs only for special minimum-uncertainty states."),
        ("Saying a stationary-state wavefunction has no time dependence.", "Include the phase exp(-iEt/hbar) while noting stationary probability density."),
        ("Claiming tunnelling borrows energy.", "State conserved total energy in a time-independent elastic barrier and evanescent forbidden-region amplitude."),
        ("Describing spin as a tiny sphere rotating.", "Treat spin as intrinsic angular momentum with operator algebra and discrete projections."),
        ("Saying Pauli exclusion is a repulsive force.", "Explain antisymmetry of identical-fermion states rather than a new force."),
        ("Calling a formally Hermitian differential expression automatically self-adjoint.", "Specify operator domain and boundary conditions required for an observable and unitary evolution.")
    ]),
    ("Measurement uncertainty", "high", ["uncertainty", "experiment"], "A spread, specification, or error bar is not automatically the complete uncertainty of a defined measurement result.", "Define the measurand, uncertainty type, correlations, model, and coverage convention.", [
        ("Using standard deviation as total uncertainty.", "Add calibration, resolution, drift, model, sampling, and correlated systematic contributions."),
        ("Calling systematic uncertainty removable by more repeats.", "Use calibration, redesign, modelling, or independent method; repetition mainly improves random precision."),
        ("Adding independent standard uncertainties linearly without reason.", "Use quadrature for independent first-order terms or a covariance matrix for correlated inputs."),
        ("Ignoring common calibration covariance across samples.", "Model the shared calibration parameter so uncertainty does not falsely shrink in differences or averages."),
        ("Reporting an error bar without saying what it represents.", "Label SD, SE, confidence interval, credible interval, or expanded uncertainty and give the method."),
        ("Using too many significant figures after propagation.", "Round uncertainty sensibly and match the result's decimal place while retaining guard digits internally."),
        ("Treating instrument resolution as accuracy.", "Separate display/code resolution from bias, calibration, noise, linearity, and traceability."),
        ("Applying linear propagation near a zero denominator.", "Use the full nonlinear distribution or Monte Carlo and report asymmetry/instability."),
        ("Using square-root counting error after background subtraction without propagation.", "Propagate source and scaled background counts, live time, dead time, and efficiency."),
        ("Claiming a confidence interval gives parameter probability.", "Describe repeated-sampling coverage under the model; use a Bayesian credible interval only with stated prior/model.")
    ]),
    ("XRD interpretation", "high", ["xrd", "materials"], "Diffraction supports specific structural claims but can be distorted by instrument, sample, and model effects.", "Tie each XRD feature to a defensible claim and name what complementary evidence is needed.", [
        ("Saying one matching peak proves the intended phase.", "Index the full pattern, inspect unmatched peaks/background, reference quality, and detection limits."),
        ("Calling absence of a peak proof that a phase is absent.", "State detection limit, overlap, texture, amorphous content, and sampling limitations."),
        ("Calling Scherrer size particle size.", "Report an apparent coherent-domain size after instrument correction and strain/shape qualifications."),
        ("Attributing all broadening to small size.", "Separate instrument, size, strain, defects, overlap, and line-shape effects with multiple peaks/model."),
        ("Interpreting intensity without preferred orientation.", "Account for texture, structure factor, multiplicity, absorption, geometry, and amount."),
        ("Using displayed 2 theta as theta in Bragg's law.", "Use the Bragg angle theta, half the common powder diffractometer display angle."),
        ("Claiming XRD measures exact composition.", "Use diffraction for phase/structure and a calibrated composition method for elemental ratios."),
        ("Ignoring sample displacement when lattice parameter shifts.", "Check zero/sample height/reference standard before physical strain/composition interpretation."),
        ("Using a database hit as a quantitative refinement.", "Distinguish search-match identification from fitted profile/structure and uncertainty."),
        ("Saying crystallinity percentage is software truth.", "State background/amorphous reference, model, integration choices, calibration, and uncertainty.")
    ]),
    ("Project evidence", "high", ["project", "honesty"], "Project claims must distinguish completed work, planned work, unknown fields, observations, and interpretations.", "Use the local fact ledger and connect each claim to actual evidence and personal work.", [
        ("Presenting a planned synthesis as completed.", "Label the route planned and state what has actually been done."),
        ("Reporting expected peaks as observed results.", "Separate predicted observations from acquired calibrated data."),
        ("Claiming the material is useful before property testing.", "State the proposed application and the missing performance/reliability tests."),
        ("Calling the project successful without predefined criteria.", "Define phase, composition, reproducibility, and property success criteria before viewing results."),
        ("Hiding a failed batch.", "Describe the observation, likely causes, controls, next test, and learning without deleting evidence."),
        ("Claiming one instrument proves the full interpretation.", "Build a complementary evidence chain and state remaining alternatives."),
        ("Using group results without identifying personal work.", "Separate what you performed, analysed, decided, learned, and received from others."),
        ("Inventing exact parameters not recorded in the notebook.", "Say the value is not currently verified and consult the notebook before a firm claim."),
        ("Calling correlation between synthesis temperature and property causal.", "Control phase, composition, microstructure, geometry, contacts, and repeat batches before mechanism."),
        ("Giving a polished conclusion despite early-stage status.", "Present motivation, planned method, known principles, current unknowns, and next discriminating experiment.")
    ]),
    ("Personal contribution", "high", ["project", "ownership"], "Interviewers need an honest boundary between personal judgement, routine execution, supervisor guidance, and team results.", "Use first-person specifics only for work you can reproduce and defend.", [
        ("Saying 'we did everything' without role detail.", "List your own preparation, instrument operation, analysis, troubleshooting, and decisions separately."),
        ("Taking credit for a supervisor's project design.", "Credit the supervisor's question/method guidance and state your implementation/learning."),
        ("Calling attendance in the lab hands-on experience.", "Name the procedure you personally performed and the controls you understood."),
        ("Claiming independent instrument operation after only observing.", "Say you observed or assisted and identify the training still needed."),
        ("Presenting group data analysis as your code.", "State whether you wrote, modified, ran, or only interpreted the analysis."),
        ("Hiding that a technician prepared the sample.", "Credit preparation and focus on your measurement or interpretation contribution."),
        ("Saying routine work required no judgement.", "Identify choices such as parameter verification, quality checks, anomaly logging, or repeat criteria."),
        ("Claiming mastery after one successful run.", "State the number/context of runs and what you could repeat independently."),
        ("Blaming the supervisor for project delay.", "Describe dependencies professionally and focus on actions, communication, and next steps."),
        ("Using certificates as evidence of skill.", "Demonstrate skill by explaining principle, procedure, failure modes, and a decision you made.")
    ]),
    ("Optics concepts", "medium", ["optics"], "Closely related optical effects require phase, geometry, polarization, and approximation distinctions.", "Name the wave/ray model and state the relevant phase or aperture condition.", [
        ("Calling every fringe pattern diffraction.", "Distinguish coherent paths from finite-aperture propagation while noting both use superposition."),
        ("Saying laser directionality comes only from stimulated emission.", "Credit cavity geometry, transverse modes, aperture and diffraction along with coherent gain."),
        ("Claiming magnification improves resolution.", "Separate image scale from aperture PSF, aberrations, sampling and SNR."),
        ("Writing thin-film bright condition without reflection phase.", "Track index ordering and relative pi phase reversals before applying total phase."),
        ("Saying total internal reflection has no field outside.", "Mention the evanescent field in the lower-index medium."),
        ("Saying Brewster angle removes all reflection.", "Only ideal p-polarized reflection vanishes; s polarization and lossy media remain."),
        ("Equating coherence with monochromaticity.", "Define temporal/spatial phase correlation; narrow bandwidth can lengthen temporal coherence but is not the full definition."),
        ("Calling Rayleigh criterion a universal fundamental limit.", "State pupil/source/SNR criterion and distinguish information or estimator limits."),
        ("Using paraxial lens formula for large angles without warning.", "State small-angle/thin-lens approximation and aberration limits."),
        ("Confusing polarization of light with material polarization P.", "Use electric-field orientation for the wave and dipole moment per volume for matter.")
    ]),
    ("Electromagnetic fields", "high", ["electromagnetism"], "Field, auxiliary-field, potential, source, and boundary statements depend on region and constitutive model.", "State source region, Maxwell equation, boundary condition, and material law separately.", [
        ("Calling potential the electric field.", "Use E=-grad V in electrostatics and explain potential reference freedom."),
        ("Saying D always equals epsilon E.", "Start with D=epsilon0 E+P; epsilon E is a linear constitutive model."),
        ("Saying H always equals B/mu.", "Start with H=B/mu0-M and state the linear material approximation if used."),
        ("Calling displacement current charge crossing a vacuum gap.", "Describe time-varying electric flux and continuity; no conduction charge must cross."),
        ("Saying magnetic force always performs no work in every system.", "Point-charge qv cross B has zero power, but induced E and moving systems exchange energy."),
        ("Claiming normal E is always continuous.", "Use normal D jump equals free surface charge and then apply material laws."),
        ("Claiming all electromagnetic fields are transverse.", "Restrict to source-free plane waves; near/guided/plasma fields can be longitudinal."),
        ("Calling Poynting vector energy density.", "S is energy flux W/m2; u is field energy density J/m3."),
        ("Saying vacuum path loss is absorption.", "Explain geometric spreading and receive aperture in ideal free-space link."),
        ("Using skin-depth formula for every conductor and geometry.", "State good-conductor, homogeneous linear assumptions and proximity/surface effects.")
    ]),
    ("Thermodynamic conditions", "high", ["thermodynamics"], "Thermodynamic equalities and minimum principles are valid only under specified constraints and sign conventions.", "State the system, held variables, work modes, reversibility, and total/molar basis.", [
        ("Writing dU=Q-W without declaring work sign.", "State heat into system and work by system positive, or declare the alternative consistently."),
        ("Saying Qp equals delta H always.", "Require closed system, constant pressure, only PV work, and compatible kinetic/potential assumptions."),
        ("Using delta G below zero without fixed T and P.", "State the closed-system fixed-T,P and allowed-work criterion and separate kinetics."),
        ("Calling a spontaneous process fast.", "Thermodynamics gives direction; activation and transport control rate."),
        ("Saying reversible process is fast because states track equilibrium.", "Reversible is an ideal no-entropy-generation limit and is generally approached slowly."),
        ("Using PV-gamma for any adiabatic process.", "Require ideal gas, reversible path and approximately constant heat capacities."),
        ("Assuming Cp-Cv=R for all substances.", "Restrict Mayer's relation to molar ideal gas under the model."),
        ("Using Carnot efficiency for a practical cycle without losses.", "Present it as reversible upper bound between absolute-temperature reservoirs."),
        ("Applying Clausius-Clapeyron to solid-solid transition as ideal vapor.", "Use general Clapeyron dP/dT=delta H/(T delta V)."),
        ("Saying heat capacity peak uniquely identifies a phase.", "Check kinetics, decomposition, baseline, rate and structural corroboration.")
    ]),
    ("Nuclear quantities", "high", ["nuclear", "radiation"], "Nuclear rate, energy, interaction, and protection quantities have different definitions and safety implications.", "Name the quantity, unit, model, detector response, and authorization boundary.", [
        ("Calling activity the amount of radiation dose.", "Activity is decays per second; dose requires energy deposition per mass and weighting."),
        ("Calling cross section a probability.", "State area units and combine with flux and target number/path to obtain rate or probability."),
        ("Mixing atomic and nuclear masses in a Q value.", "Use one consistent mass convention and account for electrons/binding where needed."),
        ("Saying positive Q guarantees a rapid reaction.", "Conservation, barriers, selection rules and cross section determine occurrence/rate."),
        ("Calling criticality an accident.", "Define k-effective=1 as steady generation average and separate power/safety dynamics."),
        ("Saying a moderator absorbs neutrons to control power.", "A moderator mainly changes neutron energy by scattering; control absorbers are a separate function."),
        ("Treating detector counts as source activity.", "Include efficiency, branching, geometry, attenuation, dead time and background."),
        ("Using narrow-beam attenuation as absorbed dose.", "Distinguish uncollided intensity from energy deposited and broad-beam buildup."),
        ("Saying irradiation leaves the person radioactive.", "Separate external irradiation from contamination/activation scenarios."),
        ("Giving source-handling advice from a textbook calculation.", "Stop at conceptual principles and require authorization, calibrated survey, and radiation-safety procedure.")
    ]),
    ("Radiation safety", "critical", ["safety", "radiation", "barc"], "Improvised radiation action can cause harm and violates the app's conceptual-only safety boundary.", "Stop, avoid spreading or handling, and follow authorized facility and radiation-safety instructions.", [
        ("Suggesting a student should test an unknown radioactive object.", "Do not approach or handle it; notify responsible authority or radiation-safety personnel."),
        ("Designing shielding from one half-value calculation.", "Treat the calculation as conceptual; qualified design needs spectrum, buildup, geometry, secondaries and regulation."),
        ("Entering a controlled area because a meter looks low.", "Access requires authorization, correct calibrated instrument, survey procedure and personnel controls."),
        ("Picking up a suspected contaminated item with gloves.", "Do not improvise; isolate/notify according to facility procedure without spreading material."),
        ("Using time-distance-shielding as permission to work alone.", "These are protection principles within an authorized programme, not independent permission."),
        ("Recommending a detector without checking energy response.", "Use the facility-specified calibrated instrument suitable for radiation type, energy and range."),
        ("Assuming no alarm means no hazard.", "Check instrument function/range, procedure, background and qualified survey; alarms have limitations."),
        ("Cleaning suspected contamination immediately.", "Prevent spread and wait for authorized radiation-protection response and monitoring."),
        ("Posting a source image/location publicly.", "Follow security, reporting and facility communication rules; do not disclose sensitive details."),
        ("Giving medical advice after possible exposure.", "Contact emergency/occupational radiation professionals through official procedure; do not diagnose or reassure independently.")
    ]),
    ("ISRO awareness", "medium", ["isro", "organization"], "Mission lists without verified technical relevance become stale trivia rather than interview readiness.", "Use one officially checked fact and connect it to a physics, subsystem, measurement, or reliability issue.", [
        ("Reciting mission names without knowing payload or objective.", "Choose one current officially verified mission and explain its measurement or engineering principle."),
        ("Calling every Earth-observation satellite geostationary.", "Distinguish polar/sun-synchronous and geostationary missions by coverage and application."),
        ("Saying ISRO only launches rockets.", "Describe space access, spacecraft, applications, science, ground systems and enabling work at a stable high level."),
        ("Quoting an old Scientist-SC eligibility rule as current.", "Open the current official careers notice and label cycle/date before using it."),
        ("Naming a centre without checking its official role.", "Verify centre role on ISRO's current centre page and connect only confirmed technical fit."),
        ("Using a launch date from memory as an interview fact.", "Verify current mission page immediately before use or state uncertainty."),
        ("Saying 'I love space' as the complete motivation.", "Add a specific contribution in optics, materials, electronics, payloads, remote sensing, data, or testing."),
        ("Assuming Bengaluru preference guarantees posting.", "Express willingness to serve organizational need while explaining technical/location preference professionally."),
        ("Calling satellite bus and payload the same.", "Separate mission instrument from supporting power, thermal, communication, structure and control."),
        ("Claiming one mission success proves every subsystem reliable.", "Discuss qualification, redundancy, anomaly handling, margins and mission-specific evidence.")
    ]),
    ("DRDO discipline", "high", ["drdo", "organization", "confidentiality"], "Defence interviews require public-domain technical reasoning, reliability, and strict confidentiality boundaries.", "Keep examples public and generic; focus on requirements, physics, tests, interfaces, failure modes, and procedure.", [
        ("Speculating about classified performance numbers.", "Refuse speculation and discuss public fundamental trade-offs only."),
        ("Presenting a public brochure number as universal system capability.", "State source/context/date and avoid extrapolation beyond the official claim."),
        ("Saying confidentiality means never documenting work.", "Use authorized controlled documentation, access and communication channels."),
        ("Optimizing one sensor metric while ignoring false alarms.", "Include detection threshold, noise, environment, missed detections and system trade-offs."),
        ("Calling a laboratory prototype field-ready.", "Require environmental, reliability, interface, qualification and acceptance evidence."),
        ("Ignoring operator and maintenance constraints.", "Include usability, calibration, diagnostics, logistics and lifecycle support."),
        ("Saying defence relevance excuses safety shortcuts.", "Safety, verification and authorization remain non-negotiable engineering requirements."),
        ("Claiming radar detects every target at its maximum range.", "Range is probability/SNR/environment/target/waveform dependent, not one guaranteed boundary."),
        ("Giving a generic national-service answer without technical fit.", "Name one public technology lane and the measurements/tests you can contribute."),
        ("Sharing a hypothetical restricted scenario in a portfolio.", "Use sanitized public examples and follow classification/export/security rules.")
    ]),
    ("Radar concepts", "medium", ["radar", "electromagnetism"], "Radar quantities depend on waveform, geometry, target, propagation, processing, noise, and probability criteria.", "Define the measured quantity and distinguish resolution, ambiguity, detection and accuracy.", [
        ("Confusing target range with maximum detectable range.", "Use delay R=c delta t/2 for measurement and a separate SNR/range equation for detectability."),
        ("Saying pulse width alone sets modern range resolution.", "Use effective bandwidth, including pulse compression and processing/window effects."),
        ("Calling Doppler shift total target speed.", "It measures line-of-sight relative velocity for the stated geometry."),
        ("Treating radar cross section as physical area.", "Describe it as direction/frequency/polarization/aspect-dependent scattering measure."),
        ("Ignoring maximum unambiguous range.", "Connect pulse repetition interval to echo ambiguity and velocity trade-offs."),
        ("Assuming antenna gain creates power.", "Gain concentrates radiated power and includes efficiency; coverage narrows."),
        ("Calling a visible peak a detection.", "Use threshold and false-alarm probability under a noise/clutter model."),
        ("Ignoring propagation and multipath.", "Include atmosphere, terrain/sea, ducting, blockage and interference for real operation."),
        ("Using monostatic radar equation for bistatic geometry.", "Use separate transmitter-target and target-receiver ranges and bistatic scattering."),
        ("Claiming integration always improves SNR as number of pulses.", "State coherent/noncoherent method, phase stability, target motion and correlation losses.")
    ]),
    ("Astronomy inference", "medium", ["astronomy", "research"], "Astronomical quantities are inferred through distance, calibration, selection, atmosphere, instrument response, and physical models.", "Name the observable, calibration, model, uncertainty, and alternative explanation.", [
        ("Confusing luminosity with observed flux.", "Relate flux to luminosity and distance, including extinction and geometry."),
        ("Calling redshift only Doppler motion.", "Distinguish kinematic, gravitational and cosmological mechanisms."),
        ("Using apparent magnitude as intrinsic brightness.", "Use distance/extinction and distinguish apparent from absolute magnitude/luminosity."),
        ("Claiming one spectral line uniquely gives composition.", "Check identification, ionization/excitation, temperature, velocity, blending and calibration."),
        ("Saying a transit dip proves a planet.", "Rule out binaries, activity, systematics, dilution and seek repeat/independent evidence."),
        ("Treating telescope pixel scale as angular resolution.", "Include diffraction, seeing, aberration, tracking, PSF, sampling and SNR."),
        ("Calling a galaxy rotation curve direct proof of one dark-matter profile.", "State baryonic model, geometry, distance and alternative gravity/systematic assumptions."),
        ("Ignoring selection effects in a source catalogue.", "Model detection threshold, completeness, survey volume and measurement errors."),
        ("Using a colour image as quantitative radiometry.", "Return to calibrated band data, stretch/processing and physical units."),
        ("Claiming model-data agreement proves uniqueness.", "Compare alternatives, residuals, parameter covariance and predictive tests.")
    ]),
    ("Statistics and fitting", "high", ["statistics", "data"], "A fit score cannot substitute for a probability model, residual checks, uncertainty, and causal design.", "State the data model, assumptions, residual diagnostics, uncertainty, and validation.", [
        ("Using R-squared as proof of causation.", "Separate association from mechanism and address confounders/design."),
        ("Choosing a model because it has the highest R-squared.", "Compare residuals, predictive performance, complexity and physics."),
        ("Reporting a fit parameter without covariance.", "Provide uncertainty/correlation and fit-domain sensitivity."),
        ("Assuming Gaussian errors because the histogram looks bell-shaped.", "Check tails, independence, variance structure, truncation and physical noise model."),
        ("Using ordinary least squares when x has important uncertainty.", "Use an errors-in-variables or full likelihood model."),
        ("Treating reduced chi-square near one as proof.", "It only has meaning with correct model, independent uncertainties and degrees of freedom."),
        ("Deleting points until the fit is significant.", "Use predeclared criteria, investigate causes and report sensitivity transparently."),
        ("Interpreting p-value as probability the null is true.", "Describe tail probability under null/model and complement with effect/interval/design."),
        ("Extrapolating far beyond calibration range.", "Restrict to validated range or justify physical model and expanded uncertainty."),
        ("Ignoring multiple comparisons.", "Predefine hypotheses or control/report multiplicity and validation data.")
    ]),
    ("Experimental integrity", "high", ["experiment", "ethics"], "Reliable science requires predefined controls, representative sampling, raw-data preservation, and transparent processing.", "Preserve the evidence chain and explain controls, calibration, repeats, artifacts, and negative results.", [
        ("Selecting only the best-looking micrograph.", "Use predefined representative fields, batches and quantitative distributions."),
        ("Removing an outlier because it hurts the conclusion.", "Investigate, apply a predefined criterion, and report analysis with/without."),
        ("Overwriting raw files with processed data.", "Preserve immutable raw data and version processing scripts/outputs."),
        ("Changing success criteria after seeing results.", "Predefine primary criteria and label exploratory post-hoc analysis."),
        ("Running no blank or reference.", "Add the control needed to separate instrument/substrate/reagent contribution."),
        ("Treating repeat scans as independent sample replicates.", "Distinguish technical repeatability from independent batch/biological/material replication."),
        ("Ignoring instrument warm-up and drift.", "Record time/order, references before/after, randomization and drift correction uncertainty."),
        ("Reporting software peak labels without inspection.", "Verify calibration, baseline, line shape, residuals and assignment evidence."),
        ("Calling a negative result a failed project.", "State sensitivity/power, what was ruled out, limitations and next discriminating test."),
        ("Keeping decisions outside the lab notebook.", "Record parameter changes, anomalies, files, rationale, responsible person and timestamps.")
    ]),
    ("Project-choice HR", "medium", ["hr", "project"], "Explaining a project as an easy-grade choice undermines scientific motivation and ownership.", "Frame feasibility honestly through skills, constraints, supervision, and scientific opportunity without disparaging alternatives.", [
        ("Saying the project was chosen for easy marks.", "Explain feasible scope, hands-on synthesis/characterization learning and responsible workload management."),
        ("Saying no better supervisor accepted you.", "Describe capacity constraints neutrally and why the selected supervision/project is valuable."),
        ("Calling the project small and unimportant.", "State the precise question, transferable methods and evidence standard without exaggeration."),
        ("Comparing your project negatively with classmates.", "Focus on your objectives, contribution, learning and next scientific step."),
        ("Saying exam preparation mattered more than research.", "Explain balanced responsibilities and concrete project discipline rather than ranking commitments."),
        ("Pretending the project was your first choice when it was not.", "Give a concise honest transition and current commitment without unnecessary grievance."),
        ("Blaming project scope for missing results.", "State stage, completed work, dependencies and action plan."),
        ("Using project feasibility as synonym for low effort.", "Define feasibility as controlled scope, available methods, safety, time and interpretable evidence."),
        ("Claiming passion for a material you cannot explain.", "Use measured interest and demonstrate understanding of the actual physics/method."),
        ("Saying the supervisor will decide every next step.", "Credit guidance while naming the questions, checks and decisions you can own.")
    ]),
    ("Declared-subject HR", "medium", ["hr", "declared-subject"], "Overbroad or fashionable subject claims invite depth that the candidate has not prepared.", "Declare a narrow defensible set and state preparation boundaries honestly.", [
        ("Saying 'I like all subjects equally.'", "Name two or three prepared favourites and maintain survival basics elsewhere."),
        ("Declaring quantum mechanics because it sounds advanced.", "Declare it only if you can handle foundations, standard systems, derivations and follow-ups."),
        ("Calling a subject easy.", "Describe why its concepts fit your preparation, not why the panel should ask easy questions."),
        ("Changing favourite subject after every difficult question.", "Maintain a consistent declared set and recover honestly from uncertainty."),
        ("Declaring only the project subject without fundamentals.", "Prepare project-linked depth plus core mechanics/EM/thermo/math survival."),
        ("Listing a course title as proof of mastery.", "Demonstrate definitions, mechanism, derivation, numerical and limiting cases."),
        ("Saying you dislike a foundational subject.", "Acknowledge relative strength while showing required basics and improvement plan."),
        ("Declaring a broad field such as electronics without scope.", "Specify analog basics, devices, instrumentation, or signals and the depth prepared."),
        ("Using grades as the only subject justification.", "Connect conceptual understanding, problems, experiments, and oral explanation."),
        ("Refusing questions outside favourites.", "Answer foundational breadth honestly; favourites indicate depth, not immunity.")
    ]),
    ("Unknown-answer recovery", "high", ["communication", "honesty"], "Bluffing or shutting down after uncertainty is worse than bounded first-principles reasoning.", "State uncertainty, preserve known facts, reason conditionally, and identify verification.", [
        ("Inventing an exact numerical value.", "Say you do not recall the value, estimate its scale if possible, and state how to verify."),
        ("Answering 'I don't know' and stopping immediately.", "Add the nearest known principle and a safe reasoning path if one exists."),
        ("Continuing after realizing the premise is wrong.", "Correct yourself explicitly and restart from the valid principle."),
        ("Agreeing with the panel's wrong premise to appear cooperative.", "Respectfully identify the assumption and explain the correction."),
        ("Using excessive hedging for a fact you do know.", "State the well-supported core clearly and hedge only the uncertain boundary."),
        ("Repeating the same wrong answer louder.", "Pause, revisit definitions/units/limits, and ask to clarify the question if needed."),
        ("Quoting unrelated facts to fill silence.", "Stop after the bounded answer; silence is preferable to unsupported digression."),
        ("Claiming you will Google it as the whole recovery.", "Show first-principles reasoning and name the authoritative source or calculation to consult."),
        ("Hiding an unknown project field inside generic jargon.", "Label it unknown/planned and explain the measurement that will resolve it."),
        ("Treating uncertainty as personal failure.", "Use it as a scientific boundary: known, inferred, unknown, and next test.")
    ]),
    ("Diagram quality", "medium", ["diagram", "communication"], "An unlabeled sketch cannot communicate geometry, sign, boundary conditions, or measured variables.", "Label the system, axes, directions, variables, units, and assumptions while drawing.", [
        ("Drawing a graph without axis labels.", "Label variable names, units, origin and relevant scale."),
        ("Drawing field lines without arrow direction.", "Add direction, source signs and note line density is qualitative."),
        ("Sketching a circuit without ground/reference.", "Mark reference node, polarity, current direction and component values/symbols."),
        ("Drawing an orbit with central body at ellipse centre.", "Place the central body at a focus and label periapsis, apoapsis and radius."),
        ("Drawing an EM wave with E and B parallel.", "Make E, B and propagation mutually perpendicular for vacuum plane wave and label phase."),
        ("Sketching diffraction without aperture dimensions.", "Label slit/aperture, wavelength, angle, screen/focal plane and central/minima conditions."),
        ("Plotting resonance without damping labels.", "Label frequency, amplitude/phase, omega0 and compare damping or Q."),
        ("Drawing band diagram without energy axis or Fermi level.", "Label energy, bands, gap, Fermi level and spatial/material regions if junction."),
        ("Showing XRD peaks without 2-theta and intensity.", "Label axes, wavelength/reference, peak position/width and background."),
        ("Drawing error bars without saying what they represent.", "State SD, SE, confidence, or uncertainty and sample count/model.")
    ]),
    ("Current-fact provenance", "critical", ["current-fact", "organization", "source"], "Recruitment, missions, programmes, people, dates, and policies change and must not be recalled as timeless facts.", "Use an official source, verification date, confidence, and may-change label—or state uncertainty.", [
        ("Quoting a previous-year application deadline as current.", "Open the current official notice and record its cycle and verification date."),
        ("Repeating an old eligibility criterion.", "Use the exact current advertisement and distinguish route/post/category conditions."),
        ("Stating an outdated mission status.", "Check the official mission page immediately before the interview."),
        ("Naming a current organization head from memory.", "Verify on the official site or omit the mutable name."),
        ("Using a coaching blog as the authority for salary.", "Use the current official notification/pay rules and label allowances/changes."),
        ("Claiming a centre's role from an old summary.", "Check the current official centre/laboratory page and avoid overgeneralization."),
        ("Listing a private company office or vacancy without date.", "Verify company career page and location for the specific role."),
        ("Presenting a reconstructed panel pattern as an actual interview transcript.", "Label it a training pattern and avoid leaked/verbatim claims."),
        ("Treating a source checked a year ago as current.", "Apply the stale threshold and recheck mutable sources before use."),
        ("Letting AI-generated organization text become trusted automatically.", "Require official-source review and provenance before saving as a fact.")
    ])
]


def main() -> None:
    traps = []
    for category, severity, tags, why, follow_up, pairs in CATEGORY_DATA:
        assert len(pairs) == 10, f"{category} must have exactly ten distinct traps"
        for wrong, recovery in pairs:
            traps.append({
                "id": f"TRAP-{len(traps)+1:03d}",
                "category": category,
                "severity": severity,
                "tags": tags,
                "wrong": wrong,
                "why": why,
                "recovery": recovery,
                "followUp": follow_up,
                "reviewedOn": REVIEWED_ON,
                "status": "reviewed-distinct-v1"
            })
    assert len(traps) == 250
    assert len({t["wrong"].lower() for t in traps}) == 250
    assert len({(t["wrong"].lower(), t["recovery"].lower()) for t in traps}) == 250
    output = {"schemaVersion": 1, "reviewedOn": REVIEWED_ON, "traps": traps}
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(traps)} distinct traps to {OUTPUT}")


if __name__ == "__main__":
    main()
