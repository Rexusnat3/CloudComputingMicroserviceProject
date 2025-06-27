# Use a slim Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set Python path to allow module imports
ENV PYTHONPATH=/usr/src/app

# Expose the port your FastAPI app will run on
EXPOSE 8000

# Start the FastAPI app using Uvicorn with the correct module path
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]