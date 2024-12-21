This project shows how to package data files within a Python distribution, and has some example code for reading the data files. To build this distribution, create a venv with build_ installed and then execute

.. code-block:: bash

   python -m build

The distributions (an sdist .tar.gz and a bdist .whl) will be written to ./dist/ subdirectory. To test it out, install the distribution and run the console script ``resources-example``.

Here's a compatibility summary of the five approaches demonstrated:

+-------------+-----------------------+------------+---------------+---------------+-------------------+---------------------+
| Module      | Description           | In stdlib? | Works on Py2? | Works on Py3? | Works in zipfile? | Run as script? [*]_ |
+=============+=======================+============+===============+===============+===================+=====================+
| example1.py | os.path.join          |     yes    |      yes      |      yes      |         no        |       yes           |
+-------------+-----------------------+------------+---------------+---------------+-------------------+---------------------+
| example2.py | pkgutil               |     yes    |      yes      |      yes      |        yes        |        no           |
+-------------+-----------------------+------------+---------------+---------------+-------------------+---------------------+
| example3.py | pkg_resources         |     no     |      yes      |  deprecated   |        yes        |       yes           |
+-------------+-----------------------+------------+---------------+---------------+-------------------+---------------------+
| example4.py | importlib.resources.  | deprecated |       no      |   yes (3.7+)  |        yes        |       yes           |
|             | read_binary/read_text |            |               |               |                   |                     |
+-------------+-----------------------+------------+---------------+---------------+-------------------+---------------------+
| example5.py | importlib.resources.  | yes (3.9+) |      yes [*]_ |      yes      |        yes        |       yes           |
|             | files                 |            |               |               |                   |                     |
+-------------+-----------------------+------------+---------------+---------------+-------------------+---------------------+

If you are interested in creating an executable zip from source, you can use stdlib `zipapp <https://docs.python.org/3/library/zipapp.html>`_ utility (Python 3.5+):

.. code-block:: bash

   python3 -m zipapp --compress /path/to/resources-example --main="myapp:main" --output=myapp.zip

If this command is slow or the .zip is surprisingly large, make sure don't have any stray subdirs in the source path beforehand (e.g. ``.venv``, ``.git``, ``.idea``).

Now you can run the zip directly with the interpreter (any Python version):

.. code-block:: bash

   python myapp.zip

.. _build: https://pypi.org/project/build/

.. [*] "Run as script" means executing the submodule directly, e.g. ``python myapp/example2.py``. Note that Guido considers this `an anti-pattern <https://mail.python.org/pipermail/python-3000/2007-April/006793.html>`_.
.. [*] The same APIs are available in 2.7 by using an `importlib_resources <https://pypi.org/project/importlib-resources/3.3.1/>`_ backport.
