# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SereneeOsman Guidance'
copyright = '2024, Serenee Osman'
author = 'Serenee Osman'
release = '0.0.1'

language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx.ext.autosummary',
    'sphinxcontrib.bibtex',
    'rst2pdf.pdfbuilder',
    'sphinx_simplepdf',
    'sphinx.ext.imgconverter'
]
pdf_documents = [('index', u'YourProjectNameDocumentation', u'Your Project Name Documentation', u'Your Name')]

bibtex_bibfiles = ['refs.bib']

# Configuration for sphinx-copybutton
copybutton_prompt_text = ">>> "  # Customize the text shown before copied code
copybutton_prompt_is_regexp = True  # Set to True if the prompt is a regular expression
copybutton_only_copy_prompt_lines = True  # Set to True if you want only prompt lines to be copied


# Add syntax highlighting style
pygments_style = 'sphinx'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_title = 'SereneeOsman Guidance'

html_static_path = ['_static']

html_css_files = [
    'custom.css',
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"   
]

latex_engine = 'xelatex'  # Use XeLaTeX for better font support if available

latex_elements = {
    'preamble': r'''
        \usepackage{fontspec}
        \setmainfont{DejaVu Serif}  % Use a font that supports your characters
    ''',
}

html_context = {
    'display_github': True,
    'github_user': 'sereneeosman',
    'github_repo': 'sereneeosman_doc',
    'github_version': 'main',
    'conf_py_path': '/docs/source',

}






