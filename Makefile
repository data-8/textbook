.PHONY: help notebooks stage deploy

BLUE=\033[0;34m
NOCOLOR=\033[0m

STAGING_BOOK_URL=https://ds8.gitbooks.io/staging-computational-and-inferential-thinking/content/
BOOK_URL=https://ds8.gitbooks.io/textbook/content/

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  notebooks     to convert the notebooks to HTML for embedding."
	@echo "  stage         to deploy the book to the staging Gitbook."
	@echo "  deploy        to deploy the book to Gitbooks."

notebooks:
	@echo "${BLUE}Converting notebooks to HTML.${NOCOLOR}"
	@echo "${BLUE}=============================${NOCOLOR}"

	python convert_notebooks_to_html_partial.py

	@echo ""
	@echo "${BLUE}    Done, output is in notebooks-html${NOCOLOR}"

stage:
	git pull
	make notebooks
	git add -A
	git commit -m "Build notebooks"
	@echo "${BLUE}Deploying staging book to Gitbook.${NOCOLOR}"
	@echo "${BLUE}=========================${NOCOLOR}"
	git push origin staging
	@echo ""
	@echo "${BLUE}    Done, see book at ${STAGING_BOOK_URL}.${NOCOLOR}"

deploy:
	git pull
	make notebooks
	git add -A
	git commit -m "Build notebooks"
	@echo "${BLUE}Deploying book to Gitbook.${NOCOLOR}"
	@echo "${BLUE}=========================${NOCOLOR}"
	git push origin gh-pages
	@echo ""
	@echo "${BLUE}    Done, see book at ${BOOK_URL}.${NOCOLOR}"
