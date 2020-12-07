FROM python:3.8.1-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP manage.py

ENTRYPOINT ["sh", "boot.sh"]