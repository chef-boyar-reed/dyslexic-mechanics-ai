# Dockerfile for serving frontend and backend
FROM python:3.9-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port and run the app
EXPOSE 5000
CMD ["python", "app.py"]
