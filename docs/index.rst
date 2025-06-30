.. blurtpy documentation master file

Welcome to blurtpy's documentation!
===================================

**blurtpy** is a cross-platform Python package that lets your code speak, beep, and notify! It provides simple global functions, decorators, context managers, and a class-based API for voice and sound notifications, with full configuration and platform support.

Features
--------
- Speak messages aloud (TTS) on macOS, Linux, and Windows
- Play system beeps and custom sound files
- Decorators and context managers for easy notifications
- Class-based and global APIs
- Full configuration: rate, volume, voice, pitch, language
- Mute mode and environment variable support
- Fully tested (CI, Docker, cross-platform)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   configuration
   api
   platform
   testing

Installation
============

Install with pip:

.. code-block:: bash

    pip install blurtpy

Or with Pipenv:

.. code-block:: bash

    pipenv install blurtpy

Requirements
============

- Python 3.7+
- Platform-specific tools:
  - **macOS**: Uses `say` and `afplay` (pre-installed)
  - **Linux**: Uses `espeak`, `spd-say`, or `aplay`
  - **Windows**: Uses `pyttsx3`, `winsound`

See :doc:`platform` for more details.

Getting Started
===============

See the :doc:`usage` section for quick examples, or :doc:`api` for the full API reference.


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
