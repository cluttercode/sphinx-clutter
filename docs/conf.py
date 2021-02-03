import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Sphinx Clutter Plugin'
copyright = '2021, Itay Donanhirsh'
author = 'Itay Donanhirsh'

extensions = ["sphinx_clutter"]

templates_path = []

exclude_patterns = ['_build']

html_theme = 'alabaster'

html_static_path = []
