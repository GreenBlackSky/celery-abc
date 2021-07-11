FROM python:3.9-slim-buster

RUN mkdir /app && chmod +rwx /app
COPY run.sh /app/run.sh
COPY test_caller.py /app/test_caller.py

WORKDIR /app

RUN chmod +x /app/run.sh && \
    apt-get update && \
    apt-get -y dist-upgrade && \
    apt-get -y install bash netcat && \
    pip install celery && \
    pip install pytest

CMD ./run.sh