FROM ubuntu:19.04

MAINTAINER Ketan Singh "ketansingh_vsec@yahoo.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential && \
    pip3 install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app
#COPY ../positions.csv /app

#ENTRYPOINT [ "python3", "app.py" ]
CMD [ "python3", "app.py" ]

#CMD ["/bin/bash"]
