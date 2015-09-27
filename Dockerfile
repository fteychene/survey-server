FROM python:3.3

MAINTAINER francois.teychene@gmail.com

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

EXPOSE 5000
WORKDIR /app

COPY /src /app/
CMD ["gunicorn", "-w=1", "-b=0.0.0.0:5000", "-n=SurveyServer", "--proxy-allow-from=*", "--access-logfile=-", "--error-logfile=-", "run:app"]
