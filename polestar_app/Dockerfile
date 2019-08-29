FROM ubuntu:19.04

MAINTAINER Your Name "ketansingh_vsec@yahoo.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential && \
    pip install --upgrade pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
