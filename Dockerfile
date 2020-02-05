FROM python:3.7-slim-stretch

RUN apt-get update --fix-missing && apt-get install -y --fix-missing \
    pkg-config libreadline-dev libxml2-dev

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

  
#RUN  pip install django==1.2
# jrd last minute django install not defined in requirements.txt ( stupid move ) 


WORKDIR /go/src/github.com/simple-app/

COPY . .
# copy entire contents of directory

ENTRYPOINT ["/app.py"]
