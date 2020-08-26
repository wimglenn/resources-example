"""Loading resources using importlib_resources APIs.
https://importlib-resources.readthedocs.io/en/latest/"""
from __future__ import print_function

import importlib_resources


def func():
    my_resources = importlib_resources.files("myapp") / "data_subdir"
    data = (my_resources / "binfile.dat").read_bytes()
    print("data", repr(data))
    text = (my_resources / "textfile.txt").read_text()
    print("text", repr(text))
