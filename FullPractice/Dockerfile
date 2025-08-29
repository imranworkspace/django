# Dockerfile

# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /fullpractice

# Install dependencies
COPY requirnments.txt /fullpractice/
RUN pip install --upgrade pip
RUN pip install -r requirnments.txt


# Copy project files
COPY . /fullpractice/

# Copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh

# Give execute permissions
RUN chmod +x /entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]