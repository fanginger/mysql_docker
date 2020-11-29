CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg
docker run  -it --rm  \
     --name=${CONTAINER} \
     ${IMAGE_NAME} 
     # bash     -p 3306:3306  
               # -it --rm 