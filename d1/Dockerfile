FROM python:3.7-alpine
WORKDIR /app
RUN echo $(pwd)
ADD . .
RUN echo $(ls)
CMD python app.py
# RUN pip install -r req.txt
