FROM python:3.12-alpine3.20

COPY ./backend/requirements.txt /tmp/requirements.txt
COPY ./backend /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client libldap && \
    apk add --update --no-cache --virtual .tmp-build-deps build-base postgresql-dev musl-dev openldap-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser --disabled-password --no-create-home container-user

ENV PATH="/py/bin:$PATH"

USER container-user