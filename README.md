# Computational and Inferential Thinking

This repository holds the Jupyter Book source for Computational and Inferential
Thinking: The Foundations of Data Science.

## To make a change to the book and update `inferentialthinking.com`

1. Get your copy of this repository:

   ```
   git clone https://github.com/data-8/textbook
   ```
2. Change the file you wish and commit it to the repository.
3. Push your change back to the `data-8/textbook` repository (ideally via a pull request).
4. That's it a GitHub Action will build the book and deploy it to [inferentialthinking.com](https://inferentialthinking.com)


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
the [Jupyter Book build instructions here](https://jupyterbook.org/start/build.html).
