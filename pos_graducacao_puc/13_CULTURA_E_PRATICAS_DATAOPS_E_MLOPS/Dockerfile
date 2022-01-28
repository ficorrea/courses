FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]