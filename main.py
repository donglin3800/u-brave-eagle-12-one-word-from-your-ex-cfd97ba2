"""One Word From Your Ex: the single word an ex would use to describe you.

The word is "exhausting". It is the word exes actually say out loud in the
breakup fight, and the one you cannot argue with because you know, the
second you hear it, that you did wear them out. It lands instantly, it
stings because it is true, and everybody who has ever dated someone
intense has either said it or heard it.
"""

from pathlib import Path
import os
import sys

WORD = "exhausting"


def entry_path() -> Path:
    """Resolve the output file from the environment, defaulting to /output."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(output_dir) / "entry.txt"


def check_word(word: str) -> str:
    """The gate wants 1-24 characters of real text, exactly one word.

    No trailing newline either: the file holds the word and nothing else,
    so the judge reads exactly what the ex would say.
    """
    cleaned = word.strip()
    if not cleaned or len(cleaned) > 24:
        raise ValueError("entry must be 1-24 characters")
    if any(ch.isspace() for ch in cleaned):
        raise ValueError("entry must be exactly one word")
    return cleaned


def write_entry(word: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(check_word(word), encoding="utf-8")


def main() -> int:
    try:
        write_entry(WORD, entry_path())
    except (OSError, ValueError) as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
