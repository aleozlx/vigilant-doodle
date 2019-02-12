FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip3 install redis celery #kubernetes
COPY ./app /app
ENV STATIC_INDEX 1
