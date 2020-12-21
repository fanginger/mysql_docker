CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg
docker run  -it --rm  \
     -p 80:8888 --name=${CONTAINER} \
     -e MYSQL_ROOT_PASSWORD=ginger123 \
<<<<<<< HEAD
     -v /home/backup:/mysql_docker/backup \
=======
     -v /home/${USER}/mysql_backup:/mysql_docker/backup \
>>>>>>> af8fdc07aff9d74d7c079bbdacc7ee41c945fd6f
     ${IMAGE_NAME} 