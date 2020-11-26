FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#RUN apt-get update && apt-get install -y netcat-openbsd

COPY . .

#CMD ["/bin/bash", "docker-entrypoint.sh"]

CMD ["python", "manage.py", "db", "init"]
CMD ["python", "manage.py", "db", "migrate"]
CMD ["python", "manage.py", "db", "upgrade"]
#
CMD ["python", "manage.py", "runserver", "--host", "0.0.0.0", "--port", "5000"]

