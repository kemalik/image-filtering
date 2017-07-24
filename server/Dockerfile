FROM python:3
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/app
ENV PROJECT_NAME=image_filtering

COPY requirements.txt ${APP_HOME}/requirements.txt
RUN pip install -r ${APP_HOME}/requirements.txt

ADD . ${APP_HOME}
WORKDIR ${APP_HOME}

EXPOSE 8000
CMD ["python", "manage.py runserver"]