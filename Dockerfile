FROM python:3.9.6-slim

# install equirements before copying application code to optimize layer caching
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

# needed to run multiple processes in one container
# https://docs.docker.com/config/containers/multi-service_container/
CMD ["./startup.sh"]