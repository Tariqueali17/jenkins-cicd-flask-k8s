# Use official Python slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Expose Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
