FROM python:3.7-alpine
WORKDIR /app
RUN pwd
ADD . .
RUN ls
RUN pip install -r req.txt
CMD gunicorn -b 0.0.0.0:5000 app:app