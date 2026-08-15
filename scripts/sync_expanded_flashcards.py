#!/usr/bin/env python3
"""Inline the 658-card reviewed expansion into Mission Viva HTML."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "expanded-flashcards.json"
HTML = ROOT / "src" / "mission-viva.js"
START = "/* MV_EXPANDED_FLASHCARDS_START */"
END = "/* MV_EXPANDED_FLASHCARDS_END */"


def build_block() -> str:
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    assert data["schemaVersion"] == 1
    assert len(data["cards"]) == 658
    meta = {
        "schemaVersion": data["schemaVersion"],
        "reviewedOn": data["reviewedOn"],
        "source": "content/expanded-flashcards.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "targetRuntimeDeck": data["targetRuntimeDeck"],
        "typeCounts": data["typeCounts"],
    }
    return (
        f"{START}const FLASHCARD_CONTENT_META="
        + json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        + ",EXPANDED_FLASHCARDS="
        + json.dumps(data["cards"], ensure_ascii=False, separators=(",", ":"))
        + f";{END}"
    )


def main() -> None:
    html = HTML.read_text()
    block = build_block()
    if START in html:
        before, rest = html.split(START, 1)
        _, after = rest.split(END, 1)
        html = before + block + after
    else:
        anchor = "const FLASHCARDS=["
        if anchor not in html:
            raise SystemExit(f"Cannot find insertion anchor: {anchor}")
        html = html.replace(anchor, block + "\n" + anchor, 1)
    HTML.write_text(html)
    print(f"Inlined {len(json.loads(SOURCE.read_text())['cards'])} expansion flashcards into {HTML.name}")


if __name__ == "__main__":
    main()
