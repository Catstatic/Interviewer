#!/usr/bin/env python3
"""Zero-dependency schema and cross-reference validation for Mission Viva sources."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load(name: str):
    return json.loads((CONTENT / name).read_text())


def required(record: dict, keys: tuple[str, ...], label: str) -> None:
    missing = [key for key in keys if key not in record or record[key] in (None, "", [])]
    assert not missing, f"{label}: missing {missing}"


def unique(rows: list[dict], key: str, label: str) -> None:
    values = [row[key] for row in rows]
    assert len(values) == len(set(values)), f"{label}: duplicate {key}"


def https(url: str, label: str) -> None:
    parsed = urlparse(url)
    assert parsed.scheme == "https" and parsed.netloc, f"{label}: expected HTTPS URL"


def main() -> None:
    deep = load("deep-sheets.json")["topics"]
    assert len(deep) == 12
    deep_targets: set[tuple[str, str]] = set()
    for topic, sheet in deep.items():
        required(sheet, ("status", "reviewedOn", "oneMinuteCore", "prerequisites", "definitions", "equations", "derivations", "limitingCases", "experiments", "applications", "rapidQuestions", "intermediateQuestions", "deepQuestions", "numericals", "traps", "speak", "diagrams", "deriveIt", "flashcards", "resources", "readiness"), topic)
        assert sheet["status"] == "complete-v1"
        assert len(sheet["rapidQuestions"]) >= 30 and len(sheet["intermediateQuestions"]) >= 10
        assert len(sheet["deepQuestions"]) >= 5 and len(sheet["numericals"]) >= 5
        assert len(sheet["derivations"]) >= 3 and len(sheet["diagrams"]) >= 3
        for section in ("rapidQuestions", "intermediateQuestions", "deepQuestions", "numericals"):
            for item in sheet[section]:
                required(item, ("q",), f"{topic}/{section}")
                deep_targets.add((topic, item["q"]))
        for diagram in sheet["diagrams"]:
            required(diagram, ("title", "svg", "say"), f"{topic}/diagram")
            assert "<title" in diagram["svg"] and "<svg" in diagram["svg"]

    answers = load("answer-layers.json")["layers"]
    assert len(answers) == 225
    unique(answers, "id", "answers")
    unique(answers, "question", "answers")
    answer_targets = {(row["topic"], row["question"]) for row in answers}
    for row in answers:
        required(row, ("id", "topic", "question", "shortAnswer", "modelAnswer", "assumptions", "traps", "followUps", "reviewedOn", "status"), row.get("id", "answer"))
        assert row["status"] == "reviewed-full-v1" and len(row["assumptions"]) >= 2
        assert len(row["traps"]) >= 2 and len(row["followUps"]) == 5

    aliases = load("answer-aliases.json")["aliases"]
    assert len(aliases) == 101
    unique(aliases, "id", "aliases")
    unique(aliases, "question", "aliases")
    for row in aliases:
        required(row, ("id", "question", "targetType", "targetTopic", "targetQuestion", "rationale", "reviewedOn", "status"), row.get("id", "alias"))
        target = (row["targetTopic"], row["targetQuestion"])
        assert target in (answer_targets if row["targetType"] == "curated-full" else deep_targets), f"Unresolved alias {row['id']}"

    traps = load("trap-radar.json")["traps"]
    assert len(traps) == 250
    unique(traps, "id", "traps")
    unique(traps, "wrong", "traps")
    for row in traps:
        required(row, ("id", "category", "severity", "wrong", "why", "recovery", "followUp", "tags", "reviewedOn", "status"), row.get("id", "trap"))
        assert row["severity"] in {"medium", "high", "critical"}
        assert row["status"] == "reviewed-distinct-v1"

    cards = load("expanded-flashcards.json")["cards"]
    assert len(cards) == 658
    unique(cards, "id", "cards")
    unique(cards, "front", "cards")
    for row in cards:
        required(row, ("id", "topic", "type", "front", "back", "reviewedOn", "status"), row.get("id", "card"))
        assert row["status"] == "reviewed-stable-v1" and row["mayChange"] is False

    derivations = load("derivation-extensions.json")["derivations"]
    assert len(derivations) == 14
    unique(derivations, "id", "derivations")
    for row in derivations:
        required(row, ("id", "topic", "title", "assumptions", "steps", "interpretation", "unitCheck", "commonMistake", "panelInterruption", "summary"), row.get("id", "derivation"))
        assert len(row["steps"]) >= 5

    dossiers = load("organization-dossiers.json")["dossiers"]
    assert len(dossiers) == 24
    unique(dossiers, "id", "dossiers")
    for row in dossiers:
        required(row, ("id", "name", "type", "locationNote", "missionSummary", "stableFacts", "technicalFit", "interviewFocus", "whyFramework", "officialSources"), row.get("id", "dossier"))
        assert len(row["stableFacts"]) >= 3 and len(row["officialSources"]) >= 2
        for source in row["officialSources"]:
            required(source, ("label", "url", "confidence"), f"{row['id']}/source")
            https(source["url"], f"{row['id']}/source")
            assert source["verifiedOn"] is None or DATE_RE.match(source["verifiedOn"])
            assert isinstance(source["mayChange"], bool)

    resources = load("resource-extensions.json")["resources"]
    assert len(resources) == 22
    unique(resources, "id", "resources")
    unique(resources, "url", "resources")
    for row in resources:
        required(row, ("id", "title", "url", "scope", "topic", "type", "level", "expectedUse", "learningMode", "checkedOn"), row.get("id", "resource"))
        https(row["url"], row["id"])
        assert DATE_RE.match(row["checkedOn"])

    visuals = load("visual-extensions.json")["diagrams"]
    assert len(visuals) == 64
    unique(visuals, "id", "visuals")
    unique(visuals, "title", "visuals")
    unique(visuals, "svg", "visuals")
    for row in visuals:
        required(row, ("id", "topic", "title", "svg", "say", "checklist", "reviewedOn", "status"), row.get("id", "visual"))
        assert row["status"] == "reviewed-original-v1" and len(row["checklist"]) == 5
        assert "<title" in row["svg"] and "<svg" in row["svg"]

    print("Content validation passed: 12 deep sheets, 225 answers, 101 aliases, 250 traps, 658 expanded cards, 14 extension derivations, 24 dossiers, 22 resources, and 64 extension visuals.")


if __name__ == "__main__":
    main()
