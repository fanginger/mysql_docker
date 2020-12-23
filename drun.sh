CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg
docker run  -it --rm  \
     -p 80:8888 --name=${CONTAINER} \
     -e user='ddt'\
     -e password='yang'\
     -v /Users/tzuying/Desktop/mysql_docker/local_backup:/mysql_docker/backup\
     ${IMAGE_NAME} 
     

# -v /Users/tzuying/Desktop/mysql_docker/local_backup:/mysql_docker/backup\
# -v /home/dbbackup:/mysql_docker/backup\