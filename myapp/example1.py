"""Loading resources by traversing relative paths.
The naive approach. Doesn't work if loading from a zipfile."""
from __future__ import print_function

try:
    from pathlib import Path
except ImportError:
    # Python 2.x backport
    from pathlib2 import Path


def func():
    resource_path = Path(__file__).parent / "data_subdir"
    data = resource_path.joinpath("binfile.dat").read_bytes()
    print("data", repr(data))
    text = resource_path.joinpath("textfile.txt").read_text()
    print("text", repr(text))
