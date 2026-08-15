#!/usr/bin/env python3
"""Inline reviewed Resource Library extensions into Mission Viva HTML."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "content" / "resource-extensions.json"
HTML = ROOT / "src" / "mission-viva.js"
START = "/* MV_RESOURCE_EXTENSIONS_START */"
END = "/* MV_RESOURCE_EXTENSIONS_END */"


def build_block() -> str:
    raw = SOURCE.read_bytes()
    data = json.loads(raw)
    assert data["schemaVersion"] == 1
    resources = data["resources"]
    assert len(resources) == 22
    assert len({item["id"] for item in resources}) == len(resources)
    assert len({item["url"] for item in resources}) == len(resources)
    assert all(item["checkedOn"] and item["scope"] and item["expectedUse"] for item in resources)
    meta = {
        "schemaVersion": data["schemaVersion"],
        "reviewedOn": data["reviewedOn"],
        "source": "content/resource-extensions.json",
        "sha256": hashlib.sha256(raw).hexdigest(),
    }
    return (
        f"{START}const RESOURCE_CONTENT_META="
        + json.dumps(meta, ensure_ascii=False, separators=(",", ":"))
        + ",RESOURCE_EXTENSIONS="
        + json.dumps(resources, ensure_ascii=False, separators=(",", ":"))
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
        anchor = "function allResources(){"
        if anchor not in html:
            raise SystemExit(f"Cannot find insertion anchor: {anchor}")
        html = html.replace(anchor, block + "\n" + anchor, 1)
    HTML.write_text(html)
    print(f"Inlined {len(json.loads(SOURCE.read_text())['resources'])} resource extensions into {HTML.name}")


if __name__ == "__main__":
    main()
