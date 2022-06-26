# syntax=docker/dockerfile:1
FROM python:3.10.5
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 main.py