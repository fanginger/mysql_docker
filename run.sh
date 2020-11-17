CONTAINER=wpg
IMAGE_NAME=gingerfan/wpg:latest
docker run -it --rm \
     --name=${CONTAINER} \
     ${IMAGE_NAME} \
     bash