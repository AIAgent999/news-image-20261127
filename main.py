#!/usr/bin/env python3
"""Copy the finished newspaper front page to the output directory.

This script is the entry point of the news-image-20261127 submission.
It takes the artwork file ``entry.png`` that sits next to this script and
places an exact, byte-for-byte copy at ``/output/entry.png``.

The script does not touch the network and does not modify the artwork in
any way: the image that was generated and fact-checked for this round is
shipped exactly as it is.
"""

import hashlib
import os
import shutil
import sys


def locate_artwork() -> str:
    """Return the absolute path of the entry.png beside this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def sha256_of(path: str) -> str:
    """Return the SHA-256 hex digest of the file at ``path``."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_artwork(source: str, destination: str) -> str:
    """Copy ``source`` to ``destination`` and return the SHA-256 of the copy."""
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copyfile(source, destination)
    return sha256_of(destination)


def verify_copy(source: str, destination: str) -> bool:
    """Check that the copy is byte-identical to the source artwork."""
    return sha256_of(source) == sha256_of(destination)


OUTPUT_PATH = "/output/entry.png"


def main() -> int:
    source = locate_artwork()
    if not os.path.isfile(source):
        print(f"error: artwork not found: {source}", file=sys.stderr)
        return 1
    try:
        checksum = copy_artwork(source, OUTPUT_PATH)
    except OSError as exc:
        print(f"error: could not write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        return 1
    if not verify_copy(source, OUTPUT_PATH):
        print("error: copied file differs from the source artwork", file=sys.stderr)
        return 1
    print(f"copied {source} -> {OUTPUT_PATH}")
    print(f"sha256: {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
