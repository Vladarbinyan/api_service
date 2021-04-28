from python:3.9.2

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./service ./service

RUN pip3 install -r /service/requirements.txt

COPY wait-for-postgre.sh .
RUN chmod +x wait-for-postgre.sh
RUN pip3 install gunicorn