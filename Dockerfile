# syntax=docker/dockerfile:1

FROM python:3.9.18-alpine3.18
RUN pip install flask
COPY ./app /app
WORKDIR /app
CMD flask run --host=0.0.0.0 --port=5000
EXPOSE 5000
