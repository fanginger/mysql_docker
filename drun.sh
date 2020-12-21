CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg
docker run  -it --rm  \
     -p 80:8888 --name=${CONTAINER} \
     -e MYSQL_ROOT_PASSWORD=ginger123 \
     -v /home/backup:/mysql_docker/backup \
     ${IMAGE_NAME} 