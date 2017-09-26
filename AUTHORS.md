Instructions for Authors
------------------------

Here are some instructions for people editing the textbook.

Install needed dependencies:

* Install `npm` and `nodejs` on your machine.
* Run `nodejs install gitbook-cli` to install the Gitbook tools, then run `gitbook install; gitbook update`.

To edit the textbook:

* Edit the Jupyter notebooks in `notebooks/`.

To build the textbook and push changes to the world:

* Run `make build` to build locally.  This transforms the Jupyter notebooks into HTML.  You can look at the results in `notebooks-html/`.
* Run `make serve`.  This runs a local dev server that hosts the edited textbook.  Check that everything looks right.
* Run `make deploy` to push it to the world.  Check the public website to make sure everything looks right (may take up to 10 minutes to update).
