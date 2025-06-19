.. blurt documentation master file

Welcome to blurt's documentation!
=================================

**blurt** is a lightweight, cross-platform Python package that lets your code speak!  
It provides simple utilities to announce messages via voice, notify when a function is done, play alert sounds, and more.

Check out the usage examples and API below.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   api


Installation
============

You can install blurt using pip:

.. code-block:: bash

    pip install blurt

Or, with Pipenv:

.. code-block:: bash

    pipenv install blurt


Requirements
============

- Python 3.7+
- Platform-specific tools:
  
  - **macOS**: Uses `say` and `afplay` (pre-installed)
  - **Linux**: Uses `espeak`, `spd-say`, or `aplay`
  - **Windows**: Uses `pyttsx3`, `winsound`

Optional:
- To play sounds, you may need to install platform audio backends (like `espeak` or `aplay` on Linux).


Getting Started
===============

See the :doc:`usage` section for quick examples or :doc:`api` for full function references.


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
