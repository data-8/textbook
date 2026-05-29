# Computational and Inferential Thinking

[![Jupyter Book (via myst) GitHub Pages Deploy](https://github.com/data-8/textbook/actions/workflows/deploy-jb2.yml/badge.svg)](https://github.com/data-8/textbook/actions/workflows/deploy-jb2.yml) [![Accessibility Checks](https://github.com/data-8/textbook/actions/workflows/a11y.yml/badge.svg)](https://github.com/data-8/textbook/actions/workflows/a11y.yml)

This repository holds the Jupyter Book source for Computational and Inferential
Thinking: The Foundations of Data Science.

## To make a change to the book and update `inferentialthinking.com`

1. Get your copy of this repository:

   ```
   git clone https://github.com/data-8/textbook
   ```
2. Change the file you wish and commit it to the repository.
3. Push your change back to the `data-8/textbook` repository (ideally via a pull request). If you edit or run a cell with matplotlib output, be sure to read the [following section, Alt text for matplotlib outputs](#alt-text-for-matplotlib-outputs).
4. That's it! A GitHub Action will build the book and deploy it to [inferentialthinking.com](https://inferentialthinking.com)

### Alt text for matplotlib outputs
Alt text has been manually added for matplotlib outputs because there isn't a great built in way to set these. If you edit or run a cell with matplotlib output, the alt text may be overwritten. **When making edits, it is your responsibility to ensure that the previously added alt text remains present.**

To add alt text for a matplotlib output, you will edit the cell JSON. With the edited notebook open in VSCode, select "More Actions" (the three dots) in the cell menu and choose "Edit Cell Tags (JSON)" to open a new tab with the raw notebook file. Once you've identified the JSON corresponding to the cell, find outputs.data.text/plain which will have a default value like "<Figure size 432x432 with 1 Axes>" from matplotlib. The outputs.data.text/plain value is what will become the alt text for the plot in the deployed book, so you should update this value to a quality alt text description of the plot. If the plot already existed in the textbook, you should look at what alt text was there previously by searching [pull requests](https://github.com/data-8/textbook/pulls?q=is%3Apr+) for "Ch N Better Alt Text" (N being the chapter number you're working on) and use that alt text if it is still appropriate.

## How this repository is deployed to `inferentialthinking.com`

* The textbook at `inferentialthinking.com` is actually being served from this repository:

  https://github.com/inferentialthinking/inferentialthinking.github.io

  **You should not ever directly edit the inferentialthinking.github.io repository**
* When you make a change to this repository and push it to the `data-8/textbook` `main`
  branch, the book's HTML will automatically be pushed to https://github.com/inferentialthinking/inferentialthinking.github.io.
* This process is handled by [this GitHub Action](.github/workflows/deploy.yml)

## Build and preview the text locally

To build locally, `pip install -r requirements.txt` and then `jupyter-book build .`

**Follow the build instructions on the Jupyter Book guide**. The guide has
information for how to use the Jupyter Book CLI to build this book. You can find
the [Jupyter Book build instructions here](https://jupyterbook.org/stable/get-started/build-websites/).
