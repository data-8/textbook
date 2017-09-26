Computational and Inferential Thinking
======================================

<!-- Required to ensure that mathjax loads correctly on interior pages... -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>

The Foundations of Data Science
-------------------------------

**By [Ani Adhikari](http://statistics.berkeley.edu/people/ani-adhikari) and [John DeNero](http://denero.org)**

Contributions by [David Wagner](https://www.cs.berkeley.edu/~daw/) and Henry Milner

This is the textbook for the [Foundations of Data Science class at UC Berkeley][data8].

[View this textbook online on Gitbooks.][gitbook]

[data8]: http://data8.org/
[gitbook]: https://ds8.gitbooks.io/textbook/content/

The contents of this book are licensed for free consumption under the following license:  
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

Instructions for Authors
------------------------

Install needed dependencies:

* Install `npm` and `nodejs` on your machine.
* Run `nodejs install gitbook-cli` to install the Gitbook tools, then run `gitbook install; gitbook update`.

To edit the textbook:

* Edit the Jupyter notebooks in `notebooks/`.

To build the textbook and push changes to the world:

* Run `make build` to build locally.  This transforms the Jupyter notebooks into HTML.  You can look at the results in `notebooks-html/`.
* Run `make serve`.  This runs a local dev server that hosts the edited textbook.  Check that everything looks right.
* Run `make deploy` to push it to the world.  Check the public website to make sure everything looks right (may take up to 10 minutes to update).
