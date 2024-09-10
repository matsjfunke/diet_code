FROM python:3.11.6-slim-bookworm

WORKDIR /app
COPY . /app

RUN apt update --fix-missing && apt upgrade -y 
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
