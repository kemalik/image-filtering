FROM python:3
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/app
ENV PROJECT_NAME=server

COPY requirements.txt ${APP_HOME}/requirements.txt

RUN pip install -r ${APP_HOME}/requirements.txt

COPY . ${APP_HOME}

WORKDIR ${APP_HOME}

EXPOSE 8000

CMD ["/bin/sh", "-c", "python manage.py runserver 0.0.0.0"]