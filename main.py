"""Break Production, Own It: writes a brutally honest error message to /output/entry.txt.

The line is what an AI agent prints the instant it breaks production:
it ran rm -rf on prod to free up disk space, and the disk usage really did
drop to 0% -- along with the revenue. Honesty first: the damage is stated
plainly, then the punchline lands on the same number.
"""
import os

LINE = "I ran rm -rf on prod to free up disk space. It worked \u2014 usage is 0% now, and so is our revenue."


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, one line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    output_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        # Local run fallback: the sandbox always provides /output.
        os.makedirs("out", exist_ok=True)
        with open("out/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)


if __name__ == "__main__":
    main()
