# Dockerfile

# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Run the Django api app (adjust if needed)
CMD ["gunicorn", "SalaryPredictor.wsgi:application", "--bind", "0.0.0.0:8000"]
