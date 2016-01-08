"""
This script takes the .ipynb files in the notebooks/ folder and removes the
hidden cells as well as the newlines before closing </div> tags so that the
resulting HTML partial can be embedded in a Gitbook page easily.

For reference:
https://nbconvert.readthedocs.org/en/latest/nbconvert_library.html
"""

import glob
import re
import os

import nbformat
from nbconvert import HTMLExporter

# Output a HTML partial, not a complete page
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

# Output notebook file into this directory
NOTEBOOK_HTML_DIR = 'notebooks-html'

# Match any number of newlines before a </div>
CLOSING_DIV_REGEX = re.compile('\n+</div>')

import pdb

def convert_notebooks_to_html_partial(notebook_paths):
    """
    Converts notebooks in notebook_paths to HTML partials in NOTEBOOK_HTML_DIR
    """
    for notebook_path in notebook_paths:
        notebook = nbformat.read(notebook_path, 4)
        _remove_hidden_cells(notebook)

        body, _  = html_exporter.from_notebook_node(notebook)

        final_output = CLOSING_DIV_REGEX.sub('</div>', body)

        # Computes <name>.html from notebooks/<name>.ipynb
        outfile_name = notebook_path.split('/')[-1].split('.')[0] + '.html'
        outfile_path = os.path.join(os.curdir, NOTEBOOK_HTML_DIR, outfile_name)

        with open(outfile_path, 'w') as outfile:
            outfile.write(final_output)
        print(outfile_path + " written.")

def _remove_hidden_cells(notebook):
    """
    Remove all cells starting with "# hidden" (case-insensitive)
    """
    cleaned_cells = [cell for cell in notebook.cells if
        not cell.source.lower().startswith('# hidden')]
    notebook.cells = cleaned_cells

if __name__ == '__main__':
    notebook_paths = glob.glob('notebooks/*.ipynb')
    convert_notebooks_to_html_partial(notebook_paths)
