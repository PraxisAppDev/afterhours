FROM python:3.12-alpine

# ARG PYTHON_VERSION='3.12'

COPY ./requirements.txt /

# Installing necessary dependencies for python cryptography package
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo pkgconfig

# Directly installing python-jose[cryptography]
RUN pip3 install python-jose[cryptography]

RUN pip3 install pytest httpx

# Installing python dependencies
RUN pip3 install --no-cache-dir --upgrade -r /requirements.txt

COPY ./app /app
COPY ./test /test

WORKDIR /test

CMD ["pytest", "-s", "--disable-warnings"]