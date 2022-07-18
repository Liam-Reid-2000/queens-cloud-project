FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app
COPY server.py commaCount.py /app

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]