"""Loading resources using importlib_resources APIs.
https://importlib-resources.readthedocs.io/en/latest/"""
import importlib_resources


def func():
    my_resources = importlib_resources.files("myapp") / "data_subdir"
    data = (my_resources / "binfile.dat").read_bytes()
    text = (my_resources / "textfile.txt").read_text()
    print("data: " + repr(data))
    print("text: " + text)
