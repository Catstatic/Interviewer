#!/usr/bin/env python3
"""Build human-reviewed semantic aliases from bank wording to deep-sheet answers."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "content" / "answer-aliases.json"
REVIEWED_ON = "2026-08-15"

PAIRS = [
    ("What is a Hohmann transfer?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "What is Hohmann transfer?"),
    ("What is a cross section?", "Nuclear Physics and Radiation Protection", "What is cross section?"),
    ("Secondary versus backscattered electrons?", "Materials Characterization", "SEM secondary versus backscattered electrons?"),
    ("Why do boundary conditions quantize modes?", "Mathematical Foundations, Data, and Uncertainty", "How do boundary conditions quantize modes?"),
    ("What is an effective potential?", "Classical Mechanics and Oscillations", "What is effective potential?"),
    ("How does doping change conductivity?", "Solid State Physics", "Why does doping change conductivity?"),
    ("Why does shielding depend on radiation type?", "Nuclear Physics and Radiation Protection", "Why does shielding depend on radiation?"),
    ("What is a Q-value?", "Nuclear Physics and Radiation Protection", "What is Q value?"),
    ("Why must the sample be thin?", "Materials Characterization", "Why must a TEM sample be thin?"),
    ("What is the Poynting vector?", "Electromagnetic Theory", "What is Poynting vector?"),
    ("What is Brewster angle?", "Optics and Lasers", "What is the Brewster angle?"),
    ("What causes charging?", "Materials Characterization", "What causes XPS charging?"),
    ("What does peak intensity mean?", "Solid State Physics", "What does peak intensity depend on?"),
    ("Why is binding energy per nucleon useful?", "Nuclear Physics and Radiation Protection", "Why binding energy per nucleon?"),
    ("What is quantum efficiency?", "Optics and Lasers", "What is detector quantum efficiency?"),
    ("Why is electric potential useful?", "Electromagnetic Theory", "When is electric potential globally useful?"),
    ("What is the Hall effect used for?", "Solid State Physics", "What is the Hall effect?"),
    ("What is ground truth?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Why ground truth?"),
    ("What evidence would strengthen a phase claim?", "Solid State Physics", "What evidence supports an intended phase?"),
    ("What is attitude determination versus attitude control?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Attitude determination versus control?"),
    ("Why is a laser beam highly directional?", "Optics and Lasers", "Why is a laser directional?"),
    ("What is a nuclear cross-section?", "Nuclear Physics and Radiation Protection", "What is cross section?"),
    ("Can XRD alone prove phase purity? Why not?", "Materials Characterization", "Can XRD prove phase purity?"),
    ("What does peak position mean?", "Materials Characterization", "What does XRD peak position indicate?"),
    ("Direct versus indirect transition?", "Solid State Physics", "Direct versus indirect band gap?"),
    ("What is feedback?", "Basic Electronics and Instrumentation", "What is negative feedback?"),
    ("Why use a sun-synchronous orbit?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Why sun-synchronous?"),
    ("What would you do if a safety procedure was unclear?", "Nuclear Physics and Radiation Protection", "How would you respond if a radiation procedure is unclear?"),
    ("What is resonance physically?", "Classical Mechanics and Oscillations", "What is resonance?"),
    ("Why does grain size matter?", "Solid State Physics", "Why do grain boundaries matter?"),
    ("Why is a moderator used?", "Nuclear Physics and Radiation Protection", "What is moderator?"),
    ("Why does total internal reflection require two conditions?", "Optics and Lasers", "Two conditions for total internal reflection?"),
    ("Why is spacecraft thermal control necessary?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Why thermal control in vacuum?"),
    ("What is the difference between Fraunhofer and Fresnel diffraction?", "Optics and Lasers", "Fresnel versus Fraunhofer diffraction?"),
    ("Explain ALARA.", "Nuclear Physics and Radiation Protection", "What is ALARA?"),
    ("Why are control rods effective?", "Nuclear Physics and Radiation Protection", "What do control rods do conceptually?"),
    ("What are the main spacecraft subsystems?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Main spacecraft subsystems?"),
    ("What is a geostationary orbit?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Requirements for geostationary orbit?"),
    ("What is a state function?", "Thermodynamics", "State function versus path function?"),
    ("What is phase equilibrium?", "Thermodynamics", "What is phase coexistence?"),
    ("What is the difference between accuracy and precision?", "Materials Characterization", "Accuracy versus precision?"),
    ("What is the time constant of an RC circuit?", "Basic Electronics and Instrumentation", "What is a time constant?"),
    ("Why are normal modes useful?", "Classical Mechanics and Oscillations", "What is a normal mode?"),
    ("What is the physical meaning of an expectation value?", "Quantum Mechanics", "What is expectation value?"),
    ("Why does a particle in a box have nonzero ground energy?", "Quantum Mechanics", "Why is ground-state energy nonzero in a box/oscillator?"),
    ("What is a fluctuation?", "Statistical Mechanics", "What is an equilibrium fluctuation?"),
    ("Why does reciprocal space simplify diffraction?", "Solid State Physics", "What is reciprocal space physically useful for?"),
    ("Why do defects affect conductivity?", "Solid State Physics", "Why can a defect increase or decrease conductivity?"),
    ("What is a neutron moderator?", "Nuclear Physics and Radiation Protection", "What is moderator?"),
    ("Why does an amplifier need biasing?", "Basic Electronics and Instrumentation", "Why does a transistor need bias?"),
    ("Why must bound-state wavefunctions be normalizable?", "Quantum Mechanics", "Why normalize ψ?"),
    ("What is a systematic error?", "Mathematical Foundations, Data, and Uncertainty", "Random versus systematic uncertainty?"),
    ("Why use a blank measurement?", "Materials Characterization", "Why run a blank?"),
    ("What is the difference between activity and dose?", "Nuclear Physics and Radiation Protection", "Activity versus absorbed dose?"),
    ("How would you separate correlation from causation?", "Mathematical Foundations, Data, and Uncertainty", "Correlation versus causation?"),
    ("What determines orbital period?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Kepler’s third law?"),
    ("Why does a star sensor help attitude determination?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "Why star sensor?"),
    ("What is half-life?", "Nuclear Physics and Radiation Protection", "Half-life versus mean life?"),
    ("How do control rods work?", "Nuclear Physics and Radiation Protection", "What do control rods do conceptually?"),
    ("What is background subtraction?", "Nuclear Physics and Radiation Protection", "Why subtract background?"),
    ("How do you validate remote-sensing output?", "Orbital Mechanics, Spacecraft Systems, and Remote Sensing", "How would you prove a remote-sensing retrieval is physically meaningful?")
]

CURATED_PAIRS = [
    ("How do you report uncertainty?", "How do you communicate uncertainty?"),
    ("What is Doppler radar measuring?", "What does Doppler radar measure?"),
    ("What is the difference between a satellite payload and a satellite bus?", "What is the difference between bus and payload?"),
    ("Why are launch vehicles staged?", "Why is staging used in launch vehicles?"),
    ("Why are redundancy and fault detection important in space?", "Why is redundancy important in space?"),
    ("What would you contribute as a physics graduate?", "What could you contribute in your first six months?"),
    ("How would you distinguish exposure from contamination?", "Exposure versus contamination?"),
    ("What determines radar range resolution?", "What determines range resolution?"),
    ("Explain your project to a non-specialist.", "How would you explain your project to a non-specialist?"),
    ("Why ISRO?", "Why do you want to work in ISRO?"),
    ("What does national service mean to you in a scientific organization?", "Why do you want a mission-driven organization?"),
    ("Why BARC/DAE?", "Why do you want BARC?"),
    ("What does criticality mean?", "What does criticality mean in a reactor?"),
    ("How do you handle confidential technical work?", "How do you handle confidential information?"),
    ("Why should BARC select you?", "Why should we select you as a beginner?"),
    ("Why DRDO?", "Why do you want DRDO?"),
    ("Why astronomy?", "Why are you interested in astronomy?"),
    ("How would you respond to a model-data disagreement?", "How would you respond if your model disagrees with data?"),
    ("What is the main research question?", "What is a good research question?"),
    ("What did you personally do?", "What exactly did you do personally?"),
    ("How would you explain the project simply?", "How would you explain your project to a non-specialist?"),
    ("How can a band gap be estimated?", "What is a band gap and how can it be estimated experimentally?"),
    ("How would you calibrate an instrument?", "How do you calibrate a sensor?"),
    ("How would you calibrate the instrument?", "How do you calibrate a sensor?"),
    ("What role does temperature play in formation?", "Why does synthesis temperature affect phase formation?"),
    ("What makes a detector space-qualified?", "What makes a detector suitable for space?"),
    ("What is selectivity?", "What makes a sensor selective?"),
    ("What is filtering?", "What is a filter?"),
    ("What is a control test?", "What makes a good control experiment?"),
    ("How does temperature affect phase formation?", "Why does synthesis temperature affect phase formation?"),
    ("What if a repeated measurement drifts?", "Why repeat a measurement?"),
    ("How do temperature and time affect phase formation?", "Why does synthesis temperature affect phase formation?"),
    ("How would you repeat the measurement?", "Why repeat a measurement?"),
    ("How can spectroscopy reveal composition?", "How can spectroscopy reveal stellar composition?"),
    ("How does spectroscopy reveal composition?", "How can spectroscopy reveal stellar composition?"),
    ("What limits a telescope’s resolution?", "What is angular resolution?"),
    ("What limits angular resolution?", "What is angular resolution?"),
    ("How does diffraction connect aperture to resolution?", "What is angular resolution?"),
    ("What causes a spectral line?", "What determines the spectral lines of an atom?"),
    ("What is the difference between laboratory and flight testing?", "What is the difference between a prototype and a flight-ready component?")
]


def main() -> None:
    deep = json.loads((ROOT / "content" / "deep-sheets.json").read_text())["topics"]
    target_questions = {
        (topic, item["q"])
        for topic, sheet in deep.items()
        for section in ("rapidQuestions", "intermediateQuestions", "deepQuestions", "numericals")
        for item in sheet[section]
    }
    curated = json.loads((ROOT / "content" / "answer-layers.json").read_text())["layers"]
    curated_targets = {item["question"]: item for item in curated}
    assert len(PAIRS) == 61
    assert len(CURATED_PAIRS) == 40
    all_sources = [source.lower() for source, _, _ in PAIRS] + [source.lower() for source, _ in CURATED_PAIRS]
    assert len(set(all_sources)) == len(all_sources)
    for _, topic, target in PAIRS:
        assert (topic, target) in target_questions, (topic, target)
    for _, target in CURATED_PAIRS:
        assert target in curated_targets, target

    aliases = []
    for source, topic, target in PAIRS:
        aliases.append({
            "id": f"ALIAS-{len(aliases)+1:03d}",
            "question": source,
            "targetType": "deep-sheet",
            "targetTopic": topic,
            "targetQuestion": target,
            "rationale": "Human-reviewed semantic equivalence: the wording asks the same core concept under the target answer's stated assumptions.",
            "reviewedOn": REVIEWED_ON,
            "status": "reviewed-semantic-alias-v1"
        })
    for source, target in CURATED_PAIRS:
        layer = curated_targets[target]
        aliases.append({
            "id": f"ALIAS-{len(aliases)+1:03d}",
            "question": source,
            "targetType": "curated-full",
            "targetTopic": layer["topic"],
            "targetQuestion": target,
            "rationale": "Human-reviewed semantic equivalence: this alternate wording requests the same scientific or professional answer as the named reviewed full layer.",
            "reviewedOn": REVIEWED_ON,
            "status": "reviewed-semantic-alias-v1"
        })

    OUTPUT.write_text(json.dumps({
        "schemaVersion": 1,
        "reviewedOn": REVIEWED_ON,
        "aliases": aliases
    }, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(aliases)} reviewed answer aliases to {OUTPUT}")


if __name__ == "__main__":
    main()
