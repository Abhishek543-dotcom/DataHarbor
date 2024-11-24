FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of the backend code
COPY . .

# Expose the port Flask uses
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
