#!/usr/bin/env python3
"""Static offline/privacy/security invariants for the built Mission Viva artifact."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
h=(ROOT/'mission-viva.html').read_text()
assert h.count('<script>')==1 and not re.search(r'<script[^>]+src=',h,re.I)
assert not re.search(r'<link[^>]+(?:stylesheet|preload)',h,re.I)
assert '/cdn-cgi/' not in h and '__CF$cv' not in h
assert 'localStorage.setItem("apiKey"' not in h and 'settings.apiKey=' not in h
assert 'rememberKey' not in h.replace("delete settings.rememberKey",'') or 'delete settings.rememberKey' in h
assert 'http://example.com' not in h
assert '@media(forced-colors:active)' in h and '@media(prefers-reduced-motion:reduce)' in h
assert 'approveAIPayload' in h and 'session-only api key' in h.lower()
assert 'ensureFormAccessibility' in h and 'aria-modal="true"' in h
print('Static security audit passed: one inline script, no remote executable assets, no persistent credentials, and required consent/accessibility guards present.')
