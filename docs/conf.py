# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup ---------------------------------------------------------------
# Add the parent directory (where the `blurt` package is located) to sys.path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'blurt'
author = 'Buddheshwar Nath Keshari'
release = '0.2.2'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
