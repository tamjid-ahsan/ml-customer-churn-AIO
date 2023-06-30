FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade -r ./app/requirements.txt

COPY ./app /app/app

CMD ["uwsgi", "app.ini"]

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--port", "8888", "--allow-root"]