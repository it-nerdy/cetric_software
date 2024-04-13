# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary files
COPY src/ ./src
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to ensure Python logs are sent to the console.
ENV PYTHONUNBUFFERED=1

# Command to run on container start
CMD ["python", "./src/check_duplicates.py"]
