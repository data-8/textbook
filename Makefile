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
ifneq ($(shell git for-each-ref --format='%(upstream:short)' $(shell git symbolic-ref -q HEAD)),origin/staging)
	@echo "Please check out the staging branch if you want to stage your revisions."
	@echo "You might need to bring the staging branch up to date by merging it with the gh-pages branch."
	@echo "For example: 'git checkout staging && git pull && git merge gh-pages && make stage'"
	@echo "(Current branch: $(shell git for-each-ref --format='%(upstream:short)' $(shell git symbolic-ref -q HEAD)))"
	exit 1
endif
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
ifneq ($(shell git for-each-ref --format='%(upstream:short)' $(shell git symbolic-ref -q HEAD)),origin/gh-pages)
	@echo "Please check out the deployment branch, gh-pages, if you want to deploy your revisions."
	@echo "You might also need to bring the deployment branch up to date by merging it with the staging branch."
	@echo "For example: 'git checkout gh-pages && git pull && git merge staging && make deploy'"
	@echo "(Current branch: $(shell git for-each-ref --format='%(upstream:short)' $(shell git symbolic-ref -q HEAD)))"
	exit 1
endif
	git pull
	make notebooks
	git add -A
	git commit -m "Build notebooks"
	@echo "${BLUE}Deploying book to Gitbook.${NOCOLOR}"
	@echo "${BLUE}=========================${NOCOLOR}"
	git push origin gh-pages
	@echo ""
	@echo "${BLUE}    Done, see book at ${BOOK_URL}.${NOCOLOR}"
