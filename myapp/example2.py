"""Loading resources using stdlib pkgutil APIs.
https://docs.python.org/3/library/pkgutil.html"""
from __future__ import print_function

import pkgutil


def func():
    data = pkgutil.get_data(__name__, "data_subdir/binfile.dat")
    print("data", repr(data))
    text = pkgutil.get_data(__name__, "data_subdir/textfile.txt").decode()
    print("text", repr(text))
