FROM python:3.10.7
WORKDIR /data/web
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
COPY . .