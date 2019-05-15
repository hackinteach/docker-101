FROM python:3.7-alpine
WORKDIR /app
RUN pwd
ADD req.txt .
RUN pip install -r req.txt
ADD . .
CMD gunicorn -b 0.0.0.0:5000 app:app
