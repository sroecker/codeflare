#
# Copyright 2021 IBM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('../../codeflare/'))
sys.path.insert(0, os.path.abspath('../../'))
import sphinx_rtd_theme
from recommonmark.transform import AutoStructify

master_doc = 'index'

# -- Project information -----------------------------------------------------

project = 'CodeFlare'
copyright = '2021, CodeFlare Team'
author = 'CodeFlare Team'

_version_py = os.path.join('..', '..', 'codeflare', '_version.py')
version_ns = {}

with open(_version_py, mode='r') as version_file:
    exec(version_file.read(), version_ns)

# The short X.Y version.
version = version_ns['__version__'][:6]
# The full version, including alpha/beta/rc tags.
release = version_ns['__version__']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "recommonmark",
    "sphinx_markdown_tables",
    "versionwarning.extension",
    "sphinx.ext.todo", 
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.autosummary"
]

source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext'
}

numpydoc_show_class_members = False 

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_logo = 'images/codeflare_logo.svg'

html_theme_options = {
    'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "custom.css"
]

# -- Options for version warning

# sphinx-version-warning config
versionwarning_messages = {
    "latest": (
        "This document is for the development version. "
    )}

# Show warning at top of page
versionwarning_body_selector = "div.document"
versionwarning_banner_title = ""