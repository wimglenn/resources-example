"""Loading resources using stdlib importlib.resources APIs (Python 3.7+)
https://docs.python.org/3/library/importlib.resources.html

Note: `read_binary` and `read_text` functions demonstrated below were
deprecated in Python 3.11 (https://bugs.python.org/issue45514)

You may migrate to traversable APIs avail in stdlib for newer Python versions (3.9+):
https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
"""
import importlib.resources


def func():
    data = importlib.resources.read_binary("myapp.data_subpackage", "binfile.dat")
    text = importlib.resources.read_text("myapp.data_subpackage", "textfile.txt")
    print("data: " + repr(data))
    print("text: " + text)
