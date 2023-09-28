FROM python:3.11.5-alpine

WORKDIR /usr/src/app

COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/. ./

EXPOSE 5000

CMD [ "python3", "./main.py" ]