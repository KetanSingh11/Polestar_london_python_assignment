#!/usr/bin/env bash
### Sequential Script to complete local setup and DB setup

# --- 5010 is local machine's port
# --- 8010 is docker's port


# delete database file, if exists
rm -rf db/*.db

# copy positions.csv from ../ to current directory
cp ../positions.csv .

# remove previous docker image, if any (costly operation)
#docker rmi polestar_app:latest

# build docker image
docker build -t polestar_app:latest .

# remove any old container with the same name
docker stop my_polestar_app
docker rm my_polestar_app

# create and run a new container (deamon mode)
docker run -d -p 5010:8010 --name my_polestar_app polestar_app:latest

# interactive shell
##docker exec -it my_polestar_app /bin/bash

# wait for some seconds for docker container to come up, else will return blanks
printf "\n> sleeping 10 sec... \n"
sleep 10

# test api call
printf "\n> Making Test API call... \n"
curl -X GET "http://localhost:5010/test/"

printf "\n> sleeping 5 sec... \n"
sleep 5

# init database with csv file
curl -X GET "http://localhost:5010/api/init_db/"


# open index.html in browser
printf "\n\n"
printf '\e[1;34m%-6s\e[m' "  >> Please open 'index.html' in your browser now. <<"
printf "\n\n"

