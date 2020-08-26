"""Loading resources using stdlib importlib.resources APIs (Python 3.7+)
https://docs.python.org/3/library/importlib.html#module-importlib.resources"""
from __future__ import print_function

from importlib.resources import read_binary
from importlib.resources import read_text


def func():
    data = read_binary("myapp.data_subpackage", "binfile.dat")
    print("data", repr(data))
    text = read_text("myapp.data_subpackage", "textfile.txt")
    print("text", repr(text))
