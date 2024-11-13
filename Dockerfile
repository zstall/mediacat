FROM python:3.12.6
WORKDIR /mediacatapp
COPY . /mediacatapp
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y mediainfo
RUN apt-get install -y less
RUN apt-get install -y vim
RUN apt-get install -y postgresql-client
EXPOSE 5000
CMD flask --app fmediacat run -h 0.0.0.0 -p 5000

