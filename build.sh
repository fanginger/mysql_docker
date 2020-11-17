# docker build -t gingerfan/wpg:base .


docker build -f Dockerfile \
--cache-from gingerfan/wpg:latest \
--build-arg PYTHON_VERSION_TAG=3.7.4 \
--build-arg LINK_PYTHON_TO_PYTHON3=1 \
-t gingerfan/wpg:latest .
# --compress .
