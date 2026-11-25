#!/usr/bin/env python3
"""Snooze Button Roast — variant B: the alarm clock as an overeager intern.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday.
"""
import os

ENTRY = (
    "My alarm clock rang at 6 AM on a Saturday like an intern who arrived "
    "two hours early, beaming, waiting for a promotion for ruining my "
    "only day off."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # Best-effort copy next to the repo root; the grader sandbox mounts the
    # repo read-only, so this must never crash the run.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
