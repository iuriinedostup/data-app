FROM python:2.7

ENV CONFIG_PATH /hellofresh/configs

ADD ./code/requirements.txt /hellofresh/requirements.txt

WORKDIR /hellofresh

RUN pip install -r requirements.txt

