FROM python:3.9.4-buster
#initialize
RUN apt-get update
RUN apt-get -y install wget unzip sudo less vim ibus-mozc iputils-ping \
    tor supervisor
RUN pip install bs4
RUN pip install PySocks

#Japanize
RUN apt-get install -y locales
RUN echo "ja_JP UTF-8" > /etc/locale.gen
RUN locale-gen
RUN echo export LANG=ja_JP.UTF-8 >> ~/.profile

#create user webadmin
ARG UID=1000
ARG GID=1000
ARG GROUP=webadmin
ARG USERNAME=webadmin

#a modification is required along with your env if necessary
ARG PASSWD=webadmin

# echo "username:password" | chpasswd
# root password is "root"

RUN echo "root:root" | chpasswd && \
    groupadd --gid ${GID} ${GROUP} && \
    groupadd --gid ${GID} wheel -o && \
    adduser --uid ${UID} --ingroup wheel \
    --disabled-password --gecos "" "${USERNAME}" && \
    usermod -G wheel,${GROUP} ${USERNAME} && \
    echo "${USERNAME}:${USERNAME}" | chpasswd && \
    echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    echo '%${GROUP} ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    #echo "%wheel    ALL=(ALL)   NOPASSWD:    ALL" >> /etc/sudoers.d/wheel && \
    #echo "%${GROUP}    ALL=(ALL)   NOPASSWD:    ALL" >> /etc/sudoers.d/${GROUP} && \
    chmod -R 0440 /etc/sudoers.d

#RUN echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
#RUN echo '%${GROUP} ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers
RUN rm -rf /etc/sudoers.d/*

ARG PROJECTDIR=/var/www/html
WORKDIR ${PROJECTDIR}
COPY ./scraper.py ${PROJECTDIR}
COPY ./tor_checker.py ${PROJECTDIR}
COPY ./docker-entrypoint.sh ${PROJECTDIR}

#USER ${USERNAME}