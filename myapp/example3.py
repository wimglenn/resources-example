"""Loading resources using pkg_resources APIs (setuptools).
https://setuptools.readthedocs.io/en/latest/pkg_resources.html#basic-resource-access"""
from __future__ import print_function

from pkg_resources import resource_string as load


def func():
    data = load(__name__, "data_subdir/binfile.dat")
    print("data", repr(data))
    text = load(__name__, "data_subdir/textfile.txt").decode()
    print("text", repr(text))
