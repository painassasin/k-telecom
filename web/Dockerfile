FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y netcat

COPY . .

ENTRYPOINT ["sh","entrypoint.sh"]
