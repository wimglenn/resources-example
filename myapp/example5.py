"""Loading resources using importlib_resources APIs.
https://importlib-resources.readthedocs.io/en/latest/

Note, the PyPI packaging importlib_resources is only required for Python <= 3.8
In Python 3.9+, the same APIs are available directly in stdlib importlib.resources:
https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
"""
import importlib_resources


def func():
    my_resources = importlib_resources.files("myapp") / "data_subdir"
    data = (my_resources / "binfile.dat").read_bytes()
    text = (my_resources / "textfile.txt").read_text()
    print("data: " + repr(data))
    print("text: " + text)
