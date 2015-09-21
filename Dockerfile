FROM python:3.3

ADD requirements.txt /requirements.txt
RUN pip freeze
RUN pip install -r /requirements.txt

COPY /src /app
WORKDIR /app
CMD [python, run.py]