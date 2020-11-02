FROM python:3.8-alpine

ENV STATIC_PATH /app/static

RUN pip install virtualenv

RUN apk add -U --no-cache git \
    gcc \
    libffi-dev \
    make \
    musl-dev \
    openssl \
    openssl-dev

COPY ./requirements.txt /app/requirements.txt
RUN virtualenv /env && \
    /env/bin/python -m pip install --upgrade pip && \
    /env/bin/pip install --no-cache-dir -r /app/requirements.txt

COPY ./ /app

VOLUME ["/opt/docker-compose-projects"]

COPY ./demo-projects /opt/docker-compose-projects

EXPOSE 5000

CMD []
ENTRYPOINT ["/env/bin/python", "/app/main.py"]

WORKDIR /opt/docker-compose-projects/
