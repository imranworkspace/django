# Dockerfile

# Base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /FBV_crud

# 1️⃣ Install system dependencies first
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /FBV_crud/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /FBV_crud/

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]