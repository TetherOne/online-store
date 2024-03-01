FROM python:3.11.4-slim

RUN mkdir /online-store

WORKDIR /online-store

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .