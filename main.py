#!/usr/bin/env python3
"""One-line entry for 'The Meeting That Should Have Been an Email'."""

from pathlib import Path

ENTRY = "The meeting's only decision was to send an email explaining why we needed the meeting."

def main():
    # One line, no setup, punch lands on the final word ("meeting").
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
