# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MBTA offline prod'
copyright = '2023, ML'
author = 'morgan.lethuillier@ligo.org'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False
html_show_copyright = False
html_show_sourcelink = False


# -- Options for EPUB output
epub_show_urls = 'footnote'
