CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg
docker run  -it --rm  \
     -p 80:8888 --name=${CONTAINER} \
     -v /Users/ginger/Desktop/mysql_docker/local_backup:/mysql_docker/backup\
     -e user='ddt'\
     -e password='testpass'\
     ${IMAGE_NAME} 

     #      -e user='ddt'\
     # -e password='yang'\
     

# -v /Users/tzuying/Desktop/mysql_docker/local_backup:/mysql_docker/backup\
# -v /home/dbbackup:/mysql_docker/backup\