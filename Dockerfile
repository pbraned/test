# syntax=docker/dockerfile:1

FROM python:3.12-slim
RUN python3 -m pip install imagehash --upgrade
#WORKDIR /data

RUN python3 -m pip install flask
COPY ./app /app
WORKDIR /app
CMD flask run --host=0.0.0.0 --port=5000
EXPOSE 5000
