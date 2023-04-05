FROM python:3.9.2-slim-buster

RUN apt-get update && \
    apt-get install -y \
        chromium-driver \
        chromium \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig1 \
        libnss3-dev \
        libssl-dev \
        libffi-dev \
        git && \
    rm -rf /var/lib/apt/lists/*

ENV CHROME_DRIVER_PATH /usr/bin/chromedriver
ENV CHROME_BIN_PATH /usr/bin/chromium

RUN pip install --upgrade pip
RUN pip install selenium pytest

WORKDIR /app

COPY . /app

CMD ["pytest", "-v"]
