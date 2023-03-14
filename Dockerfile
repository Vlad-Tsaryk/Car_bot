# syntax=docker/dockerfile:1
FROM python:3.10

WORKDIR /home/app/pizza_bot

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
# copy project
COPY . /home/app/pizza_bot
RUN apt update
RUN pip install -r requirements.txt
