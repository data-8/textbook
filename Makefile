.PHONY: notebooks deploy

BLUE=\033[0;34m
NOCOLOR=\033[0m

BOOK_URL=https://ds8.gitbooks.io/textbook/content/

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  notebooks     to convert the notebooks to HTML for embedding."
	@echo "  deploy        to deploy the book to Gitbooks."

notebooks:
	@echo "${BLUE}Converting notebooks to HTML.${NOCOLOR}"
	@echo "${BLUE}=============================${NOCOLOR}"
	# Convert notebooks to HTML
	cd notebooks && \
		ipython nbconvert *.ipynb --to html --template basic && \
		find . -name '*.html' -exec mv {} ../notebooks-html \;

	# Remove newlines
	cd notebooks-html && \
		find . -name '*.html' -exec sed -e ':a' -e 'N' -e '$!ba' -e 's/\n/ /g' -i "" {} \;

	@echo ""
	@echo "${BLUE}    Done, output is in notebooks-html${NOCOLOR}"

deploy:
	git pull
	make notebooks
	git add -A
	git commit -m "Build notebooks"
	@echo "${BLUE}Deploying book to Gitbook.${NOCOLOR}"
	@echo "${BLUE}=========================${NOCOLOR}"
	git push
	@echo ""
	@echo "${BLUE}    Done, see book at ${BOOK_URL}.${NOCOLOR}"
