#!/usr/bin/env python3
"""Copy the repo's entry.png to the make.fun output directory.

Uses MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
