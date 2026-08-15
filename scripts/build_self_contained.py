#!/usr/bin/env python3
"""Build the single-file offline Mission Viva deliverable from maintainable sources."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "src" / "mission-viva.template.html"
STYLE = ROOT / "src" / "mission-viva.css"
SCRIPT = ROOT / "src" / "mission-viva.js"
OUTPUT = ROOT / "mission-viva.html"
STYLE_TOKEN = "/* MV_STYLE_BUNDLE */"
SCRIPT_TOKEN = "/* MV_SCRIPT_BUNDLE */"


def build() -> str:
    template = TEMPLATE.read_text()
    assert template.count(STYLE_TOKEN) == 1
    assert template.count(SCRIPT_TOKEN) == 1
    style = STYLE.read_text()
    script = SCRIPT.read_text()
    assert "</style>" not in style.lower()
    assert "</script>" not in script.lower()
    return template.replace(STYLE_TOKEN, style).replace(SCRIPT_TOKEN, script)


def main() -> None:
    output = build()
    OUTPUT.write_text(output)
    print(f"Built {OUTPUT.name} from src/ ({len(output):,} characters)")


if __name__ == "__main__":
    main()
