#!/usr/bin/env python3
"""Inline reviewed answer-layer JSON into the self-contained Mission Viva HTML."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "answer-layers.json"
HTML = ROOT / "src" / "mission-viva.js"
START = "/* MV_ANSWER_LAYERS_START */"
END = "/* MV_ANSWER_LAYERS_END */"


def build_block() -> str:
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    assert data["schemaVersion"] == 1
    assert data["layers"]
    meta = {
        "schemaVersion": data["schemaVersion"],
        "reviewedOn": data["reviewedOn"],
        "source": "content/answer-layers.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    return (
        f"{START}const ANSWER_CONTENT_META="
        + json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        + ",CURATED_ANSWER_LAYERS="
        + json.dumps(data["layers"], ensure_ascii=False, separators=(",", ":"))
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
    print(f"Inlined {len(json.loads(SOURCE.read_text())['layers'])} reviewed answer layers into {HTML.name}")


if __name__ == "__main__":
    main()
