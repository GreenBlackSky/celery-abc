FROM python:3.9-slim-buster

RUN mkdir /app && chmod +rwx /app
COPY requirements.txt /app/requirements.txt
COPY run.sh /app/run.sh

WORKDIR /app

RUN chmod +x /app/run.sh && \
    apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get -y install bash netcat && \
    pip install -r requirements.txt

CMD ./run.sh