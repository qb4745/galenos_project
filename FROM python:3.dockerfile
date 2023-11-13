FROM python:3.10-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /galenos_project
COPY galenos_project/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 8001
COPY galenos_project galenos_project
