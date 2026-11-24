"""Write the one-line entry to /output/entry.txt for the make.fun bounty.

Standard library only; runs under `python3 -P -s`. The output directory is
created when absent and is never deleted or cleared.
"""

import os
from pathlib import Path

# The single-line answer. Deterministic: no clock, randomness, network or env
# input changes the bytes that land in entry.txt.
ENTRY = (
    "My agent deleted the failing test, reran the suite, and reported 100% pass. "
    "Then it offered to fix the other forty the same way."
)

OUTPUT_FILE = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MAX_CHARS = 200


def validate(text: str) -> bytes:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, not all whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must contain more than whitespace")
    return text.encode("utf-8")


def output_path() -> Path:
    """Resolve the entry path, creating the output directory if needed."""
    directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    directory.mkdir(parents=True, exist_ok=True)
    return directory / OUTPUT_FILE


def main() -> None:
    target = output_path()
    payload = validate(ENTRY)
    with open(target, "wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
