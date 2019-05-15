FROM python:3.7-alpine
WORKDIR /app
RUN pwd
ADD . .
RUN ls
# TODO: Change CMD to ENTRYPOINT
ENTRYPOINT ["python", "app.py"]
