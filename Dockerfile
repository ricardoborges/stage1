FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip3 install newspaper3k

COPY ./app /app