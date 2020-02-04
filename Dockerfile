FROM python:latest

RUN apt-get update --fix-missing && apt-get install -y --fix-missing \
    pkg-config libreadline-dev libxml2-dev

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

#RUN  pip install django==1.2
# jrd django install 


WORKDIR /go/src/github.com/simple-app/

COPY . .
# copy entire contents of directory

ENTRYPOINT ["/app.py"]
