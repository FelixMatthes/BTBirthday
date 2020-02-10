FROM ubuntu:18.04 as base

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /BTBirthday/requirements.txt

WORKDIR /BTBirthday

RUN pip3 install -r requirements.txt

COPY . /BTBirthday

ENTRYPOINT [ "python3" ]

CMD [ "run.py" ]