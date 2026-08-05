#!/usr/bin/env python3
"""
update.py — Scans participants/*/info.json and injects participant cards
into the main index.html between the PARTICIPANTS_START / PARTICIPANTS_END markers.

Usage:
    python update.py
"""

import os
import json
import re

PARTICIPANTS_DIR = os.path.join(os.path.dirname(__file__), "participants")
MAIN_HTML = os.path.join(os.path.dirname(__file__), "index.html")

START_MARKER = "<!-- PARTICIPANTS_START -->"
END_MARKER = "<!-- PARTICIPANTS_END -->"


def initials(name):
    parts = name.strip().split()
    return "".join(w[0] for w in parts if w)[:2].upper()


def make_card(folder, info):
    name = info.get("name", folder)
    roll_no = info.get("roll_no", "")
    photo = info.get("photo", "")
    href = f"participants/{folder}/index.html"

    if photo:
        avatar_html = (
            f'<div class="card-avatar">'
            f'<img src="{photo}" alt="{name}" '
            f'onerror="this.parentElement.textContent=\'{initials(name)}\'">'
            f'</div>'
        )
    else:
        avatar_html = f'<div class="card-avatar">{initials(name)}</div>'

    return (
        f'<a class="card" href="{href}">\n'
        f'  {avatar_html}\n'
        f'  <div class="card-name">{name}</div>\n'
        f'  <div class="card-roll">{roll_no}</div>\n'
        f'  <div class="card-arrow">View Profile &rarr;</div>\n'
        f'</a>'
    )


def main():
    if not os.path.isdir(PARTICIPANTS_DIR):
        print(f"ERROR: participants/ directory not found at {PARTICIPANTS_DIR}")
        return

    entries = []
    for folder in sorted(os.listdir(PARTICIPANTS_DIR)):
        folder_path = os.path.join(PARTICIPANTS_DIR, folder)
        info_path = os.path.join(folder_path, "info.json")

        if not os.path.isdir(folder_path):
            continue
        if not os.path.isfile(info_path):
            continue

        try:
            with open(info_path, encoding="utf-8") as f:
                info = json.load(f)
            entries.append((folder, info))
            print(f"  Found: {folder}  →  {info.get('name', '?')} ({info.get('roll_no', '?')})")
        except json.JSONDecodeError as e:
            print(f"  SKIP {folder}: invalid info.json — {e}")

    if not entries:
        cards_html = '    <div class="empty">No participants yet.</div>'
    else:
        cards_html = "\n".join(make_card(f, i) for f, i in entries)

    with open(MAIN_HTML, encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(
        rf"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )

    if not pattern.search(html):
        print("ERROR: Could not find PARTICIPANTS_START / PARTICIPANTS_END markers in index.html")
        return

    new_html = pattern.sub(
        f"{START_MARKER}\n{cards_html}\n{END_MARKER}",
        html,
    )

    with open(MAIN_HTML, "w", encoding="utf-8") as f:
        f.write(new_html)

    print(f"\nDone! {len(entries)} participant(s) written to index.html")


if __name__ == "__main__":
    main()
