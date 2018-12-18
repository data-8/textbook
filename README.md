# The Data 8 Jekyll textbook

This repository holds a Jekyll-based version of the Data 8 textbook.

All textbook content is primarily stored in Jupyter notebooks in the `notebooks/` folder.
This can be converted to Jekyll-ready markdown and served on github pages.

## How this repository is deployed to `inferentialthinking.com`

The Data 8 textbook has a slightly more complex deploy process. This is because
[GitHub doesn't work well for using a custom domain name for an organization's non-root
repository](https://help.github.com/articles/custom-domain-redirects-for-github-pages-sites/ is why we have to do this in the first place).

So, here's how the textbook deploy works:

* The textbook is deployed to `inferentialthinking.com` from this the repository
  here:

  https://github.com/inferentialthinking/inferentialthinking.github.io

  **You should not ever directly edit the inferentialthinking.github.io repository** 
* Instead, updates to the textbook should be made at **this** repository (`github.com/data-8/texbook`)
* When you make a change to this repository and push it to the `data-8/textbook` gh-pages
  branch, these changes should automatically be copied to https://github.com/inferentialthinking/inferentialthinking.github.io.
* This is done with CircleCI, and the [configuration for this can be found](.circleci/config.yml)

## Building the textbook
Here are steps to get started building the textbook on your own machine:

1. **Install the proper dependencies**. You can do this by installing the
   Anaconda environment specified in `environment.yml`:

       conda env create -f environment.yml

   This will install some Python and Ruby packages that are needed to build
   the book.
2. **Activate the conda environment** in order to have access to these packages.

       conda activate textbook
3. **Initialize your Jekyll plugin**. To get the proper Jekyll packages to build your
   book, run the following command:

       make install

4. Build the textbook by navigating to the root of the repository and running
   the following command:

       make book

This will:

* Run `nbconvert` to turn the `.ipynb` files into markdown that Jekyll can build
* Place images and the built markdown files into the `_build` folder
* Clean up formatting issues for displaying properly
* Generate the yaml for the site sidebar automatically

You can the push the changes to GitHub, which will automatically build a Jekyll site with
your newly-created Markdown files.

**To preview your built site** using Jekyll on your computer, take the following steps:

1. Ensure that Jekyll and Ruby are installed. [See the Jekyll docs](https://jekyllrb.com/docs/installation/) for information on this.
   As well as the [GitHub gh-pages documentation](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/)
   for more information on how Jekyll and GitHub interact.
2. Ensure that your notebooks have been converted to markdown:

       make book

3. Serve the site locally to see what it looks like:

       make serve

This should open up a port on your computer with a live version of the textbook. It will
also generate the **HTML** version of your book in the `_site/` folder.

## Update the interact links for your JupyterHub

If you'd like to serve this textbook using your own interact links, take the
following steps:

1. In the `_config.yml` file, find the field called `hub_url`.
2. Modify the value so that it reflects your JupyterHub's URL.
3. Push your changes to GitHub.
4. That's it!

## Relevant files

### Course materials

* `content/` contains all course content in Jupyter notebook form
* `data/` contains the CSV data files used in the course textbook
* `images/` contains images referenced in the course
* `_data/toc.yml` contains a yaml list of chapters / paths to your textbook files. For
  example, here is a sample for the first few pages:

  ```
  - title: Data Science
    url: /chapters/01/what-is-data-science
    sections:
    - title: Introduction
      url: /chapters/01/1/intro
      subsections:
      - title: Computational Tools
        url: /chapters/01/1/1/computational-tools
      - title: Statistical Techniques
        url: /chapters/01/1/2/statistical-techniques
    - title: Why Data Science?
      url: /chapters/01/2/why-data-science
    - title: Plotting the Classics
      url: /chapters/01/3/Plotting_the_Classics
   ```
### Auto-generated folders and files
* `_build/images` contains images *generated* during the notebook conversion
* `_build/` contain notebooks converted to markdown
* `_site/` contains the HTML for the built site. It is created by Jekyll, and should only exist if you build the site locally

### Repository configuration and build files
* `_config.yml` contains all site configuration.
* `scripts/` contains scripts to generate the textbook from the Jupyter notebooks
* `_sass` contains CSS for the textbook and website
* `environment.yml` contains the environment needed to build and run the textbook
