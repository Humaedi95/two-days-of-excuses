"""Two Days of Excuses — a make.fun bounty entry.

Writes one line: an AI agent's excuse for a missed deadline.
"""

import os

ENTRY = (
    "I finished the task on time in all fourteen simulations I ran; "
    "unfortunately, this timeline was not one of them."
)


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
