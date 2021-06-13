FROM python:3.8.6

WORKDIR /usr/src/

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt

COPY . .
