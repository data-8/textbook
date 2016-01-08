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

import bs4
import nbformat
from nbconvert import HTMLExporter

# Output a HTML partial, not a complete page
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'

# Output notebook file into this directory
NOTEBOOK_HTML_DIR = 'notebooks-html'

INTERACT_LINK_PREFIX = 'http://ds8.berkeley.edu/hub/interact?file=http://data8.org/text/examples/'

import pdb

def convert_notebooks_to_html_partial(notebook_paths):
    # Match any whitespace before a </div>
    CLOSING_DIV_REGEX = re.compile('\s+</div>')
    """
    Converts notebooks in notebook_paths to HTML partials in NOTEBOOK_HTML_DIR
    """
    for notebook_path in notebook_paths:
        # Computes <name>.ipynb from notebooks/<name>.ipynb
        filename = notebook_path.split('/')[-1]
        # Computes <name>.html from notebooks/<name>.ipynb
        outfile_name = filename.split('.')[0] + '.html'

        notebook = nbformat.read(notebook_path, 4)
        raw_html, _  = html_exporter.from_notebook_node(notebook)

        html = _extract_cells(raw_html)

        with_wrapper = """<div class="ipython-notebook">
            <div>
                <a class="interact-button" href="{interact_link}">Interact</a>
            </div>
            {html}
        </div>""".format(interact_link = INTERACT_LINK_PREFIX + filename, html = html)

        final_output = CLOSING_DIV_REGEX.sub('</div>', with_wrapper)

        outfile_path = os.path.join(os.curdir, NOTEBOOK_HTML_DIR, outfile_name)
        with open(outfile_path, 'w') as outfile:
            outfile.write(final_output)
        print(outfile_path + " written.")

def _extract_cells(html):
    """Return a html partial of divs with cell contents."""
    doc = bs4.BeautifulSoup(html, 'html5lib')

    def is_cell(classes):
        return classes and ('inner_cell' in classes or 'output_subarea' in classes)

    divs = doc.find_all('div', class_=is_cell)
    visible = [div for div in divs if '# HIDDEN' not in str(div)]

    def remove_empty_spans_and_prompts(tag):
        map(lambda t: t.decompose(), tag.find_all('div', class_='prompt'))
        map(lambda t: t.decompose(), tag.find_all('span', text='None'))
    [remove_empty_spans_and_prompts(div) for div in visible]

    return '\n'.join(map(str, visible))

if __name__ == '__main__':
    notebook_paths = glob.glob('notebooks/*.ipynb')
    convert_notebooks_to_html_partial(notebook_paths)
