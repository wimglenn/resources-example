"""An example project demonstrating various ways to access data files in Python package"""
from __future__ import print_function

__author__ = "Wim Glenn"
__version__ = "0.1"


import importlib
import sys


def main():
    print("Python version:", sys.version)
    print("-" * 80)
    for i in [1, 2, 3, 4]:
        modname = "myapp.example{}".format(i)
        try:
            mod = importlib.import_module(modname)
            print(mod.__doc__)
            mod.func()
        except Exception as err:
            print("FAILED:", repr(err))
        print("-" * 80)
