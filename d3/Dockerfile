FROM python:3.7-alpine
WORKDIR /app
ADD . .
RUN pip install -r req.txt
CMD gunicorn -b 0.0.0.0:5000 app:app