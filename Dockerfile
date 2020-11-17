FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    libaio1 \
    libaio-dev \
    wget

# for anaconda
RUN apt-get install -y libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

RUN apt-get update && \
    apt-get install -y \
    mysql-server 

WORKDIR ~/Downloads
RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
RUN bash Anaconda3-2020.02-Linux-x86_64.sh -b

# Make RUN commands use the new environment:
RUN echo "export PATH=~/anaconda3/bin:$PATH" >> ~/.bashrc

RUN ~/anaconda3/bin/conda install flask
