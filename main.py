#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry.

Writes one line, a comment a developer left above fragile production
code, to /output/entry.txt (and stdout).
"""

ENTRY = "// getUserById() takes no id, hits no database, returns no user. The name is aspirational."


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
