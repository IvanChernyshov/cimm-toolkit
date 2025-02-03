# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'cimm-toolkit'
copyright = '2025, Ivan Chernyshov, Julia Razlivina'
author = 'Ivan Chernyshov, Julia Razlivina'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'myst_parser'
]

#templates_path = ['_templates']
#exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
#html_css_files = []
#html_js_files = []


# -- Logo ----------------------------------------------------------

html_theme_options = {
    'logo_only': False,
}
html_logo = '_images/logo/logo.svg'
html_favicon = '_images/logo/favicon.svg'


# -- Options for exts ----------------------------------------------

# myst-nb
nb_execution_mode = 'off'

