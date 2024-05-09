Sphinx and HTML Web Publishing
=========================

Introduction
--------------

This guide will detail the steps for setting up **Sphinx using pip**, **creating documentation**, and **publishing HTML** file on GitHub Pages.


What is sphinx
-----------------

`Sphinx <https://www.sphinx-doc.org/en/master/>`_ is a documentation generation tool that allows you to create high-quality documentation for Python projects and other programming languages. 
It enables you to write documentation in reStructuredText or Markdown formats and then generates various output formats such as HTML, PDF, ePub, and more. Sphinx is widely used in the software development community to create well-structured and easily navigable documentation for projects. 
Additionally, Sphinx can parse and render NumPy docstrings, making it an extension of the NumPy docstring format and thus particularly suited for documenting Python libraries and scientific computing projects.

Doc String format
-------------------
``NumPy docstring`` and ``Google docstring`` are two major types of docstrings commonly used in Python programming, particularly in the context of writing documentation for functions, classes, and modules.


**NumPy Docstring Style:** (`Documentation <https://numpydoc.readthedocs.io/en/latest/format.html#overview>`_)
This style is often used in the scientific computing and data analysis community, especially when documenting functions and classes related to ``NumPy`` and ``SciPy`` libraries. 
NumPy docstrings typically follow a specific format, including sections such as Parameters, Returns, Examples, and Notes. 
This format aims to provide detailed information about the purpose, inputs, outputs, and usage examples of the documented function or class.

**Google Docstring Style:** (`Documentation <https://google.github.io/styleguide/pyguide.html>`_)
The Google docstring style is a more general-purpose style used for documenting Python code across various projects.
It is based on conventions developed within Google and has gained popularity due to its simplicity and readability.
Google docstrings typically include a one-line summary, followed by a more detailed description, and sections like Args, Returns, Raises, Examples, etc.
This style doesn't mandate any specific markup language but is often written in plain text or reStructuredText.
Google docstrings focus on providing clear and concise documentation that is easy to read and understand.

What is pip
-----------------
`pip <https://pypi.org/project/pip/>`_ is the package installer for Python. It's a command-line tool that allows you to install, upgrade, and manage Python packages from the Python Package Index (PyPI) and other package indexes. 
With pip, you can easily install libraries and frameworks developed by the Python community, enabling you to extend Python's functionality for various tasks such as web development, data analysis, machine learning, and more.

Getting Started
------------------

Setting up GitHub
-----------------


Install pip
------------

**Using cmd**
First, ensure you have Python installed on your system. pip comes bundled with Python by default from Python 3.4 onwards. 
You can check if Python is installed by running ``python --version`` or ``python3 --version`` in your terminal or command prompt.
If Python is installed, you can check if pip is already installed by running ``pip --version`` or ``pip3 --version`` in your terminal or command prompt.
If pip is not installed or you have an older version, you can install or upgrade it using the appropriate command based on your Python version:

For Python 2.x:

.. code-block:: python
	sudo apt-get install python-pip

For Python 3.x:

.. code-block:: python
	sudo apt-get install python3-pip

If you're using macOS or Windows, you can download the appropriate Python installer from the `official Python website <https://www.python.org/downloads/>`_ which should come with pip.
After installation, you can verify that pip is installed correctly by running ``pip --version`` or ``pip3 --version`` again.

** Using ``Conda`` package manager **

* Activate your Conda environment: Before installing packages with pip, it's recommended to activate your Conda environment to ensure that the packages are installed within the environment.
.. code-block:: python
	conda activate your_environment_name

* Install pip into your Conda environment (if not already installed): In most cases, Conda environments come with pip pre-installed. However, if it's not installed or you want to ensure you have the latest version, you can install it using Conda.
.. code-block:: python
	conda install pip
	
or with ``conda`` via conda-forge:

.. code-block:: python
conda install -c conda-forge pip

(``-c conda-forge``: This specifies the channel from which to install the package. Channels are locations where packages are stored and can be accessed. ``conda-forge`` is a popular community channel for Conda packages maintained by the community.)

* Use pip to install the desired packages: Once pip is installed within your Conda environment, you can use it just like you would in a regular Python environment.
.. code-block:: python
	pip install package_name

Explore available packages on `PyPI  <https://pypi.org/>`_

Install sphinx
---------------
To install Sphinx using pip, you can use the following command:

.. code-block:: python
	pip install sphinx
	
or with ``conda`` via conda-forge:

.. code-block:: python
conda install -c conda-forge sphinx is this corrrect
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
--------------------------------------------------------------------
copy button
conda install -c conda-forge sphinx-copybutton
