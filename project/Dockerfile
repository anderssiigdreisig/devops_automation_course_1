# use the golang:alpine base image
FROM python:3.8
LABEL maintainer="Anders Dreisig"

COPY . /app
WORKDIR /app/techtrends
RUN pip install -r requirements.txt

EXPOSE 3111

# command to run on container start
CMD ["sh", "-c", "python init_db.py && python app.py"]