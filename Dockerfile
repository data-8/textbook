FROM node:8.5.0-stretch

ENV BOOKDIR /gitbook
WORKDIR $BOOKDIR

EXPOSE 4000 35729

RUN apt update
RUN apt -y install make python3-pip

ADD . $BOOKDIR

RUN pip3 install -r requirements.txt 

RUN npm install --global gitbook-cli
RUN gitbook fetch latest
RUN gitbook install
RUN gitbook update
RUN python3 convert_notebooks_to_html_partial.py
RUN gitbook build
CMD [ "gitbook", "--help" ]
