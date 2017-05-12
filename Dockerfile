
FROM gogineni/ubuntu:14.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /opt/

COPY gigon/* gigon/
COPY requirements.txt gigon.build/
COPY requirements/* gigon.build/requirements/

RUN virtualenv gigon/.env

RUN source gigon/.env/bin/activate \
    && cd gigon.build \
    && pip install -r requirements.txt




