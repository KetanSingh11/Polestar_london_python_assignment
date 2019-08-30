#!/usr/bin/env bash
### Sequential Script to complete local setup and DB setup

# --- 5010 is local machine's port
# --- 8010 is docker's port


# delete database file, if exists
rm -rf db/*.db

# build docker image
docker build -t polestar_app:latest .

# create and run a new container
docker run -d -p 5010:8010 --name my_polestar_app polestar_app:latest

# test api call
curl -X GET "http://localhost:5010/test/"

# init database with csv file
curl -X GET "http://localhost:5010/api/init_db/"

# open index.html in browser
echo "Please open 'index.html' in your browser now."

