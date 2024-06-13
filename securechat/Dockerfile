FROM python:3.11.2-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME 'admin'
ENV DJANGO_SUPERUSER_PASSWORD 'admin'
ENV DJANGO_SUPERUSER_EMAIL 'admin@example.com'

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]