"""Loading resources using pkg_resources APIs (setuptools).
https://setuptools.readthedocs.io/en/latest/pkg_resources.html#basic-resource-access"""
import pkg_resources


def func():
    data = pkg_resources.resource_string(__name__, "data_subdir/binfile.dat")
    text = pkg_resources.resource_string(__name__, "data_subdir/textfile.txt").decode()
    print("data: " + repr(data))
    print("text: " + text)
