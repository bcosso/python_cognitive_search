# base image
FROM python:3.8.1-slim

# install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip3 install -r requirements.txt

# add app
COPY . /usr/src/app

ENTRYPOINT [ "python3" ]

CMD [ "search_api.py" ]
