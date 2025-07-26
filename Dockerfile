# Use official Python image
FROM python:3.10-slim
# Set working directory
WORKDIR /app
# Copy project files
COPY requirements.txt .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Expose port
EXPOSE 5000
# Run the app
CMD ["python", "app.py"]
