FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt ./app/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
        pip3 install -r ./app/requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
