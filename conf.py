# -*- coding: utf-8 -*-

import sys, os
import cloud_sptheme as csp

extensions = ['sphinx.ext.todo']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Introduction to Virtual Machines'
copyright = u'2014, Roie R. Black'
version = '1.0.2'
release = '1.0.2'
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build','_unpublished','**/.git','**/_meta.rst','**/_code']
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'cloud'
html_theme_path = [csp.get_theme_dir()]
html_title = "Introduction to Virtual Machines"
html_short_title = "VMdemo"
html_logo = 'ACClogo.png'
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -- Options for LaTeX output --------------------------------------------------
latex_paper_size = 'letter'
latex_font_size = '12pt'
latex_documents = [
  ('index', 'PoP.tex', u'Introduction to Virtual Machines',
   u'Roie R. Black', 'manual'),
]
latex_logo = 'ACClogo.png'
# Additional stuff for the LaTeX preamble.
latex_preamble = ''

