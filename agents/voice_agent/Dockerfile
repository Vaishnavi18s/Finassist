# Use Python 3.10 base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files to /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
