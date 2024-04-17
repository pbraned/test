# syntax=docker/dockerfile:1

FROM python:3.9.18-alpine3.18
RUN pip install flask
COPY ./app /app
WORKDIR /app
CMD flask run
EXPOSE 5000
