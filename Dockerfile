
FROM gogineni/ubuntu:14.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

WORKDIR /opt/

COPY gigon/* gigon/
COPY requirements.txt gigon.build/
COPY requirements/* gigon.build/requirements/
COPY conf/* gigon/conf/

RUN virtualenv gigon/.env

RUN source gigon/.env/bin/activate \
    && cd gigon.build \
    && pip install -r requirements.txt

ADD scripts/entrypoint.sh /opt/
RUN chmod +x /opt/entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/opt/entrypoint.sh"]




