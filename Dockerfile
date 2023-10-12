FROM python:3.10.3-slim-buster

ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
COPY . /code/

WORKDIR /code

RUN apt-get update &&  \
    apt-get install -y libcurl4-nss-dev libssl-dev gcc &&  \
    apt-get install -y uwsgi uwsgi-plugin-python3 && \
    rm -rf /usr/lib/python*/ensurepip && \
    rm -rf /var/cache/apk/* &&  \
    apt-get clean --dry-run

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    apt-get install -y python3-dev default-libmysqlclient-dev build-essential curl && \
    pip install -r requirements.txt

CMD ["uwsgi", "--ini", "uwsgi_config.ini"]

EXPOSE 8080/tcp

# docker build -t jenfi-webserver:latest .
# docker rmi -f jenfi-webserver:latest
# docker rm jenfi-cnt ; docker run --name jenfi-cnt -it --mount "type=bind,source=$(pwd)/,target=/code/" -p 8000:8080 jenfi-webserver:latest
# or
# docker start -a jenfi-cnt
# CMD ["python", "manage.py", "runserver"]

# learnings
# install `uwsgi` in image, requirement.txt also download `uwsgi-plugin-python3`
# module in uwsgi config.settings
