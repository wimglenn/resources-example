This project shows how to package data files within a Python distribution, and has some example code for reading the data files. To build this distribution, create a venv with setuptools, wheel, and pep517 installed, then execute the latter as a module:

.. code-block:: bash

   python -m pep517.build .

The distributions (an sdist .tar.gz and a bdist .whl) will be written to ./dist/ subdirectory. To test it out, install the distribution and run the console script ``resources-example``.

Here's a compatibility summary of the five approaches demonstrated:

+-------------+---------------------+------------+---------------+---------------+-------------------+
| Module      | Description         | In stdlib? | Works on Py2? | Works on Py3? | Works in zipfile? |
+=============+=====================+============+===============+===============+===================+
| example1.py | os.path.join        |     yes    |      yes      |      yes      |         no        |
+-------------+---------------------+------------+---------------+---------------+-------------------+
| example2.py | pkgutil             |     yes    |      yes      |      yes      |        yes        |
+-------------+---------------------+------------+---------------+---------------+-------------------+
| example3.py | pkg_resources       |     no     |      yes      |      yes      |        yes        |
+-------------+---------------------+------------+---------------+---------------+-------------------+
| example4.py | importlib.resources |     yes    |       no      |   yes (3.7+)  |        yes        |
+-------------+---------------------+------------+---------------+---------------+-------------------+
| example5.py | importlib_resources |     no     |      yes      |      yes      |        yes        |
+-------------+---------------------+------------+---------------+---------------+-------------------+

If you are interested in creating an executable zip from source, you can use stdlib `zipapp <https://docs.python.org/3/library/zipapp.html>`_ utility (Python 3.5+):

.. code-block:: bash

   python3 -m zipapp --compress /path/to/resources-example --main="myapp:main" --output=myapp.zip

And now you can run the zip directly with the interpreter (any Python version):

.. code-block:: bash

   python myapp.zip
