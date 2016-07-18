FROM python:2.7

MAINTAINER Cassio Almeida "<kssioalmeida@gmail.com>"

ADD app/ /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD python app.py
