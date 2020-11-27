FROM python:3.8

WORKDIR /usr/src/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat

ENTRYPOINT ["sh", "entrypoint.sh"]
