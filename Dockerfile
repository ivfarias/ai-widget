# Use an official Python runtime as a parent image
FROM python:3.10-slim-bullseye

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Install python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

EXPOSE 443

# Run the command to start uWSGI

CMD ["uvicorn", "wsgi:app", "--host", "0.0.0.0", "--port", "443", "--timeout-keep-alive", "120"]