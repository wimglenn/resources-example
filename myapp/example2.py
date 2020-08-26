"""Loading resources using stdlib pkgutil APIs.
https://docs.python.org/3/library/pkgutil.html"""
import pkgutil


def func():
    data = pkgutil.get_data(__name__, "data_subdir/binfile.dat")
    text = pkgutil.get_data(__name__, "data_subdir/textfile.txt").decode()
    print("data: " + repr(data))
    print("text: " + text)
