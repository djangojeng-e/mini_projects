FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . /todo

RUN pip install -r /todo/requirements.txt 
RUN chmod 755 /todo/start
WORKDIR /todo 
EXPOSE 8000 

ENTRYPOINT ["/todo/start"] 
