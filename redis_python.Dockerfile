FROM python:3.8-slim-buster

RUN pip install redis

COPY ./redis_pub.py

