FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y netcat

ENTRYPOINT ["sh", "entrypoint.sh"]
