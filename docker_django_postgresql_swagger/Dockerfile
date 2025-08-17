# Dockerfile

# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /docker_dir

# Install dependencies
COPY requirnments.txt /docker_dir/
RUN pip install --upgrade pip
RUN pip install -r requirnments.txt

# Copy project files
COPY . /docker_dir/