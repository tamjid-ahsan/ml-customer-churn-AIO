FROM python:3.8-bookworm

WORKDIR /app

ADD . /app


RUN pip install -r requirements.txt
RUN pip install -U dash
RUN pip install -U flask
RUN pip install -U Jinja2 
RUN pip install -U werkzeug
CMD ["uwsgi", "app.ini"]