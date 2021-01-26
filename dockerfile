FROM ubuntu:18.04
RUN apt update -y && apt install -y wget
RUN apt install -y software-properties-common
RUN apt update -y
RUN sh -c "wget -O - http://dl.openfoam.org/gpg.key | apt-key add -"
RUN add-apt-repository http://dl.openfoam.org/ubuntu
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y openmpi-doc openmpi-bin libopenmpi-dev
RUN apt install -y openfoam7
RUN apt install -y x11-apps
RUN apt install -y vim 
RUN apt install -y unzip
RUN apt install -y python3-pip
RUN pip3 install flask
ARG DOCKER_UID=1000
ARG DOCKER_USER=user
ARG DOCKER_PASSWORD=pass
RUN useradd -m --uid ${DOCKER_UID} --groups root ${DOCKER_USER} \
  && echo ${DOCKER_USER}:${DOCKER_PASSWORD} | chpasswd
USER ${DOCKER_USER}
WORKDIR /home/${DOCKER_USER}
RUN echo ". /opt/openfoam7/etc/bashrc" >> ~/.bashrc;. ~/.bashrc
COPY ./app /opt/app