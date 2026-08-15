#!/usr/bin/env python3
"""Inline source-backed organization dossiers into Mission Viva HTML."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "organization-dossiers.json"
HTML = ROOT / "src" / "mission-viva.js"
START = "/* MV_ORG_DOSSIERS_START */"
END = "/* MV_ORG_DOSSIERS_END */"


def build_block() -> str:
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    assert data["schemaVersion"] == 1
    assert data["dossiers"]
    meta = {
        "schemaVersion": data["schemaVersion"],
        "reviewedOn": data["reviewedOn"],
        "source": "content/organization-dossiers.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    return (
        f"{START}const ORG_CONTENT_META="
        + json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        + ",VERIFIED_DOSSIERS="
        + json.dumps(data["dossiers"], ensure_ascii=False, separators=(",", ":"))
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
        anchor = "const DOSSIERS="
        if anchor not in html:
            raise SystemExit(f"Cannot find insertion anchor: {anchor}")
        html = html.replace(anchor, block + "\n" + anchor, 1)
    HTML.write_text(html)
    print(f"Inlined {len(json.loads(SOURCE.read_text())['dossiers'])} organization dossiers into {HTML.name}")


if __name__ == "__main__":
    main()
