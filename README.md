# The Data 8 Jekyll textbook

This repository holds a Jekyll-based version of the Data 8 textbook.

All textbook content is primarily stored in Jupyter notebooks in the `notebooks/` folder.
This can be converted to Jekyll-ready markdown and served on github pages.

## Hosting the textbook at `inferentialthinking.com`

This repository is **not** being hosted at `inferentialthinking.com`. The repository
for that site is located here:

https://github.com/inferentialthinking/inferentialthinking.github.io

This repository should be treated as the **master** repository, and any changes
here should be pulled into the `inferentialthinking` repository. When they are
pushed to the master branch of
[the inferentialthinking repo](https://github.com/inferentialthinking/inferentialthinking.github.io),
the website will be updated.

The easiest way to do this is to set up a "remote" git connection. Take the
following steps:

1. **Clone the `inferentialthinking` repository** and `cd` into it:

   ```
   git clone https://github.com/inferentialthinking/inferentialthinking.github.io
   cd interentialthinking.github.io
   ```

2. Add the `data-8/textbook` repository as a remote.

   ```
   git remote add textbook https://github.com/data-8/textbook
   ```

3. Ensure you are on the `master` branch of `inferentialthinking.github.io`
4. Pull in the latest changes to the textbook:

   ```
   git pull textbook gh-pages
   ```

5. Push the updated repository to github:

   ```
   git push origin master
   ```

This will update your local copy with the latest version of the textbook in
the `data-8` organization, then push it to the `inferentialthinking` organization
where it'll be hosted online.

## Building the textbook
Here are steps to get started:

1. **Install the proper dependencies**. You can do this by installing the
   Anaconda environment specified in `environment.yml`:

       conda env create -f environment.yml

2. Once this is finished, activate the environment

       conda activate textbook

3. Ensure that a `SUMMARY.md` file exists in the root of the repository. This contains
   a markdown list of bullet points and links. Each item corresponds to a chapter in the
   textbook, and is used to build the table of contents in the sidebar.

   > If you **do not** have a `SUMMARY.md` file made for this textbook, you may create one
     by hand, or generate one from the folders/files in `notebooks/` by running the following
     script:
   >
   >    python scripts/generate_summary_from_folders.py

3. Build the textbook by navigating to the root of the repository and running
   the following command:

       make textbook

This will:

* Run `nbconvert` to turn the `.ipynb` files into markdown
* Replace relative image file paths with a `{{ site.baseurl }}` base for Jekyll
* Clean up formatting issues for displaying properly
* Generate the yaml for the site sidebar automatically

You can the push the changes to GitHub, which will automatically build a Jekyll site with
your newly-created Markdown files.

**To preview your built site** using Jekyll on your computer, take the following steps:

1. Ensure that Jekyll and Ruby are installed. [See the Jekyll docs](https://jekyllrb.com/docs/installation/) for information on this.
   As well as the [GitHub gh-pages documentation](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)
   for more information on how Jekyll and GitHub interact.
2. Ensure that your notebooks have been converted to markdown:

       make textbook

3. Run the Jekyll site preview command:

       bundle exec jekyll serve

This should open up a port on your computer with a live version of the textbook.

## Update the interact links for your JupyterHub

If you'd like to serve this textbook using your own interact links, take the
following steps:

1. In the `_config.yml` file, find the field called `hub_url`.
2. Modify the value so that it reflects your JupyterHub's URL.
3. Push your changes to GitHub.
4. That's it!

## Relevant files

### Course materials

* `notebooks/` contains all course content in Jupyter notebook form
* `data/` contains the CSV data files used in the course textbook
* `images/` contains images referenced in the course
* `SUMMARY.md` contains a markdown list of chapters / paths to your textbook files. For
  example, here is a sample from the Data 8 textbook:

  ```
  * [1. Data Science](notebooks/01/what-is-data-science.md)
    * [1.1 Introduction](notebooks/01/1/intro.md)
      * [1.1.1 Computational Tools](notebooks/01/1/1/computational-tools.md)
    * [1.2 Why Data Science?](notebooks/01/2/why-data-science.md)
  * [2. Causality and Experiments](notebooks/02/causality-and-experiments.md)
    * [2.1 John Snow and the Broad Street Pump](notebooks/02/1/observation-and-visualization-john-snow-and-the-broad-street-pump.md)
    * [2.2 Snow’s “Grand Experiment”](notebooks/02/2/snow-s-grand-experiment.md)
   ```
### Auto-generated folders and files
* `images/chapters` contains images *generated* during the notebook conversion
* `_chapters/` contain notebooks converted to markdown
* `_site/` contains the HTML for the built site. It is created by Jekyll, and should only exist if you build the site locally

### Repository configuration and build files
* `_config.yml` contains all site configuration.
* `_data/navigation.yml` contains site navigation as well as auto-generated sidebar yaml
* `scripts/` contains scripts to generate the textbook from the Jupyter notebooks
* `assets/css` contains CSS for the textbook and website
* `environment.yml` contains the environment needed to build the textbook
