FROM python:3.12-alpine

# ARG PYTHON_VERSION='3.12'

COPY ./requirements.txt /

# Installing compiler and headers to build C extensions for the python cryptography pachage and other similar packages
# Installing python dependencies
# Deleting compiler and headers because the necessary C extensions are already configured
# Uninstalling pip itself to further reduce the image size
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo pkgconfig &&\
    pip3 install --no-cache-dir --upgrade -r /requirements.txt &&\
    apk del --purge gcc musl-dev python3-dev libffi-dev openssl-dev cargo pkgconfig &&\
    pip uninstall -y pip

COPY ./app /app

# HTTP1/2
EXPOSE 8001/tcp 
# HTTP3
EXPOSE 8001/udp 

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port", "8001"]