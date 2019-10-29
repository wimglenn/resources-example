This project shows how to package data files within a Python distribution, and has some example code for reading the data files.

To build this distribution, create a venv with setuptools, wheel, and pep517 installed, then execute the latter as a module:

.. code-block:: bash

   python -m pep517.build .

The distributions (an sdist .tar.gz and a bdist .whl) will be written to ./dist/ subdirectory.

To test it out, install a distribution and run the console script ``resources-example``.

Accessing resources should work on Python 2 / Python 3, Linux, macOS, Windows... and all the approaches except for ``example1.py`` should still work when the package ``myapp`` has been compressed into a .zip
