FROM python:3.7

RUN apt-get update

WORKDIR /app
ADD . /app
RUN pip install virtualenv
RUN virtualenv /flask
ENV PATH="/flask/bin:$PATH"
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "mnange.py", "runserver"]
