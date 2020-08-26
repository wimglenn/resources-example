"""Loading resources using stdlib importlib.resources APIs (Python 3.7+)
https://docs.python.org/3/library/importlib.html#module-importlib.resources"""
import importlib.resources


def func():
    data = importlib.resources.read_binary("myapp.data_subpackage", "binfile.dat")
    text = importlib.resources.read_text("myapp.data_subpackage", "textfile.txt")
    print("data: " + repr(data))
    print("text: " + text)
