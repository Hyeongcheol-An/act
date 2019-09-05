docker-compose down
docker ps -aq | xargs docker rm
docker image rm act1_web
#docker image rm compose-flask
