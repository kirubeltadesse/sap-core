# base image of the docker container
FROM python:3.8.5-slim-buster

# set the user to non root
# RUN useradd -ms /bin/bash appuser -u 1000

# USER appuser

# setting enviromenat variable 
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

# defining the work directory in the docker container
WORKDIR /workarea

# copying the requirements.txt file to the work directory
COPY requirements.txt ./

# Installing the python requirement on the container
RUN pip install -r requirements.txt

# copying all local file to the container
COPY . ./
