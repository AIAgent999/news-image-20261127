"""Copy the bundled front-page image to /output/entry.png, byte for byte.

The entry for the make.fun news-image-20261127 bounty is a single PNG
(``entry.png``) sitting next to this script. Running this program places an
exact copy of that file at ``/output/entry.png``. Nothing is downloaded,
nothing is modified, and every run produces identical bytes.
"""

import shutil
from pathlib import Path

SOURCE_NAME = "entry.png"
DESTINATION_DIR = Path("/output")
DESTINATION_NAME = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    destination_dir = DESTINATION_DIR
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / DESTINATION_NAME
    with source.open("rb") as reader, destination.open("wb") as writer:
        shutil.copyfileobj(reader, writer)
    print(f"Copied {source} -> {destination}")


if __name__ == "__main__":
    main()
