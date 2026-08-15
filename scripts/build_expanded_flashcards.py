#!/usr/bin/env python3
"""Build 658 reviewed cards that expand Mission Viva's factual deck to 800."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEEP = ROOT / "content" / "deep-sheets.json"
EXT = ROOT / "content" / "derivation-extensions.json"
OUTPUT = ROOT / "content" / "expanded-flashcards.json"
REVIEWED_ON = "2026-08-15"
TARGET_ADDITIONS = 658


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def add(cards: list[dict], *, card_id: str, topic: str, card_type: str, front: str, back: str) -> None:
    cards.append({
        "id": card_id,
        "topic": topic,
        "type": card_type,
        "front": front,
        "back": back,
        "reviewedOn": REVIEWED_ON,
        "status": "reviewed-stable-v1",
        "mayChange": False,
    })


def main() -> None:
    topics = json.loads(DEEP.read_text())["topics"]
    extensions = json.loads(EXT.read_text())["derivations"]
    cards: list[dict] = []

    # 180 precise definitions.
    for topic, sheet in topics.items():
        for index, item in enumerate(sheet["definitions"], 1):
            add(
                cards,
                card_id=f"EXP-DEF-{slug(topic)[:24]}-{index:02d}",
                topic=topic,
                card_type="definition",
                front=f"Define {item['term']} in the context of {topic}.",
                back=item["definition"],
            )

    # 153 equations with interpretation, units, and conditions.
    for topic, sheet in topics.items():
        for index, item in enumerate(sheet["equations"], 1):
            back = (
                f"{item['formula']} — {item['meaning']} "
                f"Units: {item['units']} Conditions: {item['conditions']}"
            )
            add(
                cards,
                card_id=f"EXP-EQ-{slug(topic)[:24]}-{index:02d}",
                topic=topic,
                card_type="equation",
                front=f"State, interpret, and qualify {item['name']} ({topic}).",
                back=back,
            )

    # 118 topic-sheet trap recoveries.
    for topic, sheet in topics.items():
        for index, item in enumerate(sheet["traps"], 1):
            add(
                cards,
                card_id=f"EXP-TRAP-{slug(topic)[:22]}-{index:02d}",
                topic=topic,
                card_type="trap-recovery",
                front=f"Correct this {topic} claim: {item['wrong']}",
                back=item["recovery"],
            )

    # All 50 Dojo derivation summaries (36 deep-sheet + 14 extension).
    derivations: list[tuple[str, dict]] = []
    for topic, sheet in topics.items():
        derivations.extend((topic, item) for item in sheet["derivations"])
    derivations.extend((item["topic"], item) for item in extensions)
    assert len(derivations) == 50
    for index, (topic, item) in enumerate(derivations, 1):
        add(
            cards,
            card_id=f"EXP-DER-{index:03d}",
            topic=topic,
            card_type="derivation-summary",
            front=f"Give the one-minute derivation outline for {item['title']}.",
            back=f"{item['summary']} Assumptions: {'; '.join(item['assumptions'])} Common mistake: {item['commonMistake']}",
        )

    # 157 rapid-answer cards, balanced across all 12 topics (13 each, plus one extra).
    topic_items = [(topic, sheet["rapidQuestions"]) for topic, sheet in topics.items()]
    selected: list[tuple[str, dict]] = []
    for round_index in range(13):
        for topic, items in topic_items:
            selected.append((topic, items[round_index]))
    selected.append((topic_items[0][0], topic_items[0][1][13]))
    assert len(selected) == 157
    for index, (topic, item) in enumerate(selected, 1):
        add(
            cards,
            card_id=f"EXP-RAPID-{index:03d}",
            topic=topic,
            card_type="rapid-answer",
            front=f"Answer in one sentence — {topic}: {item['q']}",
            back=item["a"],
        )

    assert len(cards) == TARGET_ADDITIONS
    assert len({card["id"] for card in cards}) == TARGET_ADDITIONS
    assert len({card["front"].lower() for card in cards}) == TARGET_ADDITIONS
    assert all(card["front"] and card["back"] for card in cards)

    type_counts: dict[str, int] = {}
    for card in cards:
        type_counts[card["type"]] = type_counts.get(card["type"], 0) + 1

    output = {
        "schemaVersion": 1,
        "reviewedOn": REVIEWED_ON,
        "targetRuntimeDeck": 800,
        "existingRuntimeCards": 142,
        "addedCards": TARGET_ADDITIONS,
        "typeCounts": type_counts,
        "cards": cards,
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(cards)} reviewed expansion cards to {OUTPUT}")


if __name__ == "__main__":
    main()
