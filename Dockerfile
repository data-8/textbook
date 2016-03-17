FROM andrewosh/binder-base

MAINTAINER Sam Lau <samlau95@gmail.com>


RUN /bin/bash -c 'source activate python3; pip install -I datascience'

