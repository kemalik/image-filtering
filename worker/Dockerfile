FROM python:3
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/app
ENV PROJECT_NAME=worker

COPY requirements.txt ${APP_HOME}/requirements.txt
WORKDIR ${APP_HOME}
RUN pip install -r ${APP_HOME}/requirements.txt

COPY . ${APP_HOME}

CMD ["/bin/sh", "-c", "celery -A tasks worker --loglevel=info"]