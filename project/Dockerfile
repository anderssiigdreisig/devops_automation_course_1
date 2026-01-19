# use the golang:alpine base image
FROM python:3.8
LABEL maintainer="Anders Dreisig"

# Set working directory to  app/techtrends
WORKDIR /app/techtrends

# Copy all contents of the `projects/techtrends` directory to the container's `/app/techtrends`
COPY techtrends/ /app/techtrends/

RUN pip install -r requirements.txt

EXPOSE 3111

# command to run on container start
CMD ["sh", "-c", "python init_db.py && python app.py"]