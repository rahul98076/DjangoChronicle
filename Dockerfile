# Start from an official Python base image
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the project code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run collectstatic
RUN python manage.py collectstatic --noinput

# The command to run the application using a production server (Gunicorn)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_project.wsgi"]