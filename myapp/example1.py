"""Loading resources by traversing relative paths.
The naive approach. Doesn't work if loading from a zipfile."""
import os


def func():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "data_subdir", "binfile.dat"), "rb") as f:
        data = f.read()
    with open(os.path.join(here, "data_subdir", "textfile.txt"), "rt") as f:
        text = f.read()
    print("data: " + repr(data))
    print("text: " + text)
