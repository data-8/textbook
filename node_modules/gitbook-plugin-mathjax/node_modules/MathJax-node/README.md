# MathJax-node

This repository contains files that provide APIs to call MathJax from 
node.js programs.  There is an API for converting individual math 
expressions (in any of MathJax's input formats) into SVG images or MathML 
code, and there is an API for converting HTML snippets containing any of 
MathJax input formats into HTML snippets containing SVG or MathML.

See the comments in the individual files for more details.

The `bin` directory contains a collection of command-line programs for 
converting among MathJax's various formats.  These can be used as examples 
of calling the MathJax API.

Use

    npm install MathJax-node

to install MathJax-node and its dependencies.

These API's can produce PNG images, but that requires the
[Batik](http://xmlgraphics.apache.org/batik/download.html) library.  It 
should be installed in the `batik` directory.  See the README file in that 
directory for more details.

