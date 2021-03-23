# Computational and Inferential Thinking

This repository holds the Jupyter Book source for Computational and Inferential
Thinking: The Foundations of Data Science.

## How this repository is deployed to `inferentialthinking.com`

* The textbook at `inferentialthinking.com` is actually being served from this repository:

  https://github.com/inferentialthinking/inferentialthinking.github.io

  **You should not ever directly edit the inferentialthinking.github.io repository**
* Updates to the textbook should be made to the `main` branch of **this** repository (`github.com/data-8/texbook`).
* When you make a change to this repository and push it to the `data-8/textbook` `main`
  branch, these changes should automatically be copied to https://github.com/inferentialthinking/inferentialthinking.github.io.

## Building the text

To build locally, `pip install -r requirements.txt` and then `jupyter-book build .`

**Follow the build instructions on the Jupyter Book guide**. The guide has
information for how to use the Jupyter Book CLI to build this book. You can find
the [Jupyter Book build instructions here](https://jupyterbook.org/start/build.html).
