FROM python:3.11.5-alpine

WORKDIR /usr/src/app

COPY src/. /usr/src/app 
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python3", "./main.py" ]