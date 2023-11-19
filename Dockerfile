FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY mount/requirements.txt /app/
RUN pip3 install -r requirements.txt

ADD mount/ .

ENV FLASK_APP=app
CMD ["python","app.py"]
