FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt
COPY . /app
