# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV MONGO_URI <your_mongodb_uri>

# Set the working directory in the container
WORKDIR /django-app

# Copy the requirements file into the container at /django-app
COPY requirements.txt /django-app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /django-app
COPY . /django-app/

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "authentication_system_project.wsgi:application"]
