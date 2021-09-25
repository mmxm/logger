FROM python:3.8-alpine
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./src .
CMD ["main.py"]
ENTRYPOINT ["python3"]
