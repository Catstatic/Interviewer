#!/usr/bin/env python3
"""Inline original Visual Library extensions into Mission Viva HTML."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "visual-extensions.json"
HTML = ROOT / "src" / "mission-viva.js"
START = "/* MV_VISUAL_EXTENSIONS_START */"
END = "/* MV_VISUAL_EXTENSIONS_END */"


def build_block() -> str:
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    diagrams = data["diagrams"]
    assert data["schemaVersion"] == 1
    assert len(diagrams) == 64
    assert len({item["id"] for item in diagrams}) == 64
    assert len({item["title"].lower() for item in diagrams}) == 64
    assert len({item["svg"] for item in diagrams}) == 64
    assert all(item["status"] == "reviewed-original-v1" and len(item["checklist"]) == 5 for item in diagrams)
    meta = {
        "schemaVersion": data["schemaVersion"],
        "reviewedOn": data["reviewedOn"],
        "source": "content/visual-extensions.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    return (
        f"{START}const VISUAL_CONTENT_META="
        + json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        + ",VISUAL_EXTENSIONS="
        + json.dumps(diagrams, ensure_ascii=False, separators=(",", ":"))
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
        anchor = "function allVisuals(){"
        if anchor not in html:
            raise SystemExit(f"Cannot find insertion anchor: {anchor}")
        html = html.replace(anchor, block + "\n" + anchor, 1)
    HTML.write_text(html)
    print(f"Inlined {len(json.loads(SOURCE.read_text())['diagrams'])} visual extensions into {HTML.name}")


if __name__ == "__main__":
    main()
