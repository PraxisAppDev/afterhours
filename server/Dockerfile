FROM python:3.12-alpine

# ARG PYTHON_VERSION='3.12'

COPY ./requirements.txt /
RUN pip3 install --no-cache-dir --upgrade -r /requirements.txt

COPY ./app /app

EXPOSE 8000/tcp
EXPOSE 8000/udp

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port", "8000"]