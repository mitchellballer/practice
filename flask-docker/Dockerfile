#FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
#RUN apk --update add bash nano
#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static
#COPY ./requirements.txt requirements.txt
#RUN pip install -r requirements.txt


FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
#RUN export FLASK_APP=app
#RUN export FLASK_ENV=development
EXPOSE 5001 
#ENTRYPOINT [ "python" ] 
CMD [ "export FLASK_APP=app & export FLASK_ENV=development & python flask run" ] 