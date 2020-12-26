CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg
docker run  -it --rm  \
     -p 80:8888 --name=${CONTAINER} \
     -v /home/dbbackup:/mysql_docker/backup\
     -e password='testpass'\
     ${IMAGE_NAME} 

# -v /home/dbbackup:/mysql_docker/backup\
# /Users/ginger/Desktop/mysql_docker/dbbackup:/mysql_docker/backup\