FROM registry.access.redhat.com/ubi8/python-36:latest

WORKDIR /opt/app-src

COPY requirements.txt /opt/app-src/
COPY main.py /opt/app-src/

USER root

RUN which python3 \
 && mkdir /opt/app-src/barcodes \
 && chown -R 1001:1001 /opt/app-src \
 && python3 -m pip install -r requirements.txt

USER 1001

CMD [ "/opt/app-root/bin/python3", "/opt/app-src/main.py" ]