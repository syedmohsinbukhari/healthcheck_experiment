FROM python:3.8-slim-buster

RUN pip install redis

WORKDIR /

COPY ./redis_pub.py .

