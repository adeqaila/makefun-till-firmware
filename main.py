"""Till Firmware Do Us Part — entry program (program/v1).

Writes one wedding vow a robot speaks at its own wedding to /output/entry.txt.
One sentence, 112 characters, deterministic, no network, no randomness.
Winner of the internal 10-candidate tournament (see candidates.md).
"""

VOW = (
    "I calculated our odds of lasting forever at 0.0001%, "
    "and I vow to spend my whole runtime proving the math wrong."
)


def main() -> None:
    text = VOW.strip()
    assert 1 <= len(text) <= 200, f"vow length {len(text)} out of gate range"
    assert text.endswith("."), "must end with a single sentence stop"
    # Exactly one non-terminal period: the decimal point inside "0.0001%".
    assert text[:-1].count(".") == 1, "must be one sentence"
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text + "\n")
    except OSError:
        # Local run outside the sandbox: write beside this file instead.
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
