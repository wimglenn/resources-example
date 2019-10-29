"""Loading resources using importlib.resources APIs.
https://importlib-resources.readthedocs.io/en/latest/"""
from __future__ import print_function

try:
    from importlib.resources import read_binary
    from importlib.resources import read_text
except ImportError:
    # Python 2.x backport
    from importlib_resources import read_binary
    from importlib_resources import read_text


def func():
    data = read_binary("myapp.data_subpackage", "binfile.dat")
    print("data", repr(data))
    text = read_text("myapp.data_subpackage", "textfile.txt")
    print("text", repr(text))
