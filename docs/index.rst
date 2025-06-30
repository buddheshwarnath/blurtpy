.. blurtpy documentation master file

Welcome to blurtpy's documentation!
===================================

**blurtpy** is an offline, cross-platform Python package for text-to-speech (TTS) and sound notifications.  
100% local, privacy-friendly, and works without internet. Perfect for secure, air-gapped, or privacy-conscious environments.

Features
--------
- Offline text-to-speech (TTS) and sound alerts
- No internet required, privacy-first, no cloud
- Cross-platform: macOS, Linux, Windows
- Global functions, decorators, context managers, and class-based API
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

Offline & Privacy
=================
- All features work 100% offline—no internet required
- No data is sent to the cloud; all processing is local
- Ideal for privacy, security, and air-gapped systems

FAQ
===
**Does blurtpy require an internet connection?**
  No, all features work offline.

**Is my data private?**
  Yes, nothing is sent to the cloud.

**Can I use blurtpy in secure or air-gapped environments?**
  Absolutely! blurtpy is designed for privacy and offline use.

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
