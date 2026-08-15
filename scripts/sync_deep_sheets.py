#!/usr/bin/env python3
"""Inline reviewed deep-sheet JSON into the self-contained Mission Viva HTML."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "deep-sheets.json"
HTML = ROOT / "src" / "mission-viva.js"
START = "/* MV_DEEP_SHEETS_START */"
END = "/* MV_DEEP_SHEETS_END */"


def build_block() -> str:
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    topics = data["topics"]
    assert data["schemaVersion"] == 1
    assert topics, "At least one deep sheet is required"
    digest = hashlib.sha256(raw).hexdigest()
    meta = {
        "schemaVersion": data["schemaVersion"],
        "reviewedOn": data["reviewedOn"],
        "source": "content/deep-sheets.json",
        "sha256": digest,
    }
    return (
        f"{START}const DEEP_CONTENT_META="
        + json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        + ",DEEP_SHEETS="
        + json.dumps(topics, ensure_ascii=False, separators=(",", ":"))
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
        anchor = "const FULL_SHEETS="
        if anchor not in html:
            raise SystemExit(f"Cannot find insertion anchor: {anchor}")
        html = html.replace(anchor, block + "\n" + anchor, 1)
    HTML.write_text(html)
    print(f"Inlined {len(json.loads(SOURCE.read_text())['topics'])} deep sheets into {HTML.name}")


if __name__ == "__main__":
    main()
