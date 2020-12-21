FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    cron

RUN apt-get install -y curl python3.7 python3.7-dev python3.7-distutils

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

RUN update-alternatives --set python /usr/bin/python3.7


RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py --force-reinstall && \
    rm get-pip.py

RUN python -m pip install flask\
                Flask-SQLAlchemy \
                Flask-RESTful \
                flask-marshmallow\
                PyMySQL\
                marshmallow-sqlalchemy
                
WORKDIR /dockerfile

#下載mysql
RUN apt-get update && \
    apt-get install -y \ 
    mysql-server \
    mysql-client

ADD . /dockerfile
COPY cron.sh /dockerfile/cron.sh
COPY sqlcron /etc/cron.d/sqlcron
RUN chmod 0644 /etc/cron.d/sqlcron

RUN crontab /etc/cron.d/sqlcron

CMD bash test.sh 
