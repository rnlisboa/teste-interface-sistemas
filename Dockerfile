FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip3 install weasyprint

COPY . /code/
