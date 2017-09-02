FROM jupyter/base-notebook
ADD . /home/jovyan/work
WORKDIR /home/jovyan/work
