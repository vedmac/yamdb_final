FROM python:3.8-alpine as builder

# Систмные переменные (это скорее настройки питона) которые не 
# планируют меняться лучше хранить здесь.
# Так пишут в интернетах, если не правда могу перенести в .env
# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/web

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt ./

RUN python3 -m pip install --upgrade pip \
    && pip3 install -r requirements.txt --no-cache-dir

WORKDIR $APP_HOME
COPY . $APP_HOME

CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000