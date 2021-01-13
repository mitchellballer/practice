FROM python:alpine3.7
ADD app.py /
ADD requirements.txt /
WORKDIR /
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py" ]
