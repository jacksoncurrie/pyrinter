# Configuration file for the Sphinx documentation builder.
#
import os
import sys
os.environ['SPHINX_BUILD'] = '1'
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information

project = "Pyrinter"
copyright = "2024, hodvak"
author = "hodvak"


# -- General configuration

extensions = [
    "myst_parser",
    # "sphinx.ext.duration",
    # "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    # "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    # "sphinx.ext.napoleon",
    "enum_tools.autoenum",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "furo"

# -- Options for EPUB output
epub_show_urls = "footnote"

source_suffix = [
    ".md",
    ".rst"
]
