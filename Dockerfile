FROM jupyter/scipy-notebook

MAINTAINER Sam Lau <samlau95@gmail.com>


RUN /bin/bash -c 'pip install -I datascience'
