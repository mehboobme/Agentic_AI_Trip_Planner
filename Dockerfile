# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy entire app
COPY . .

# Expose port (for FastAPI or Streamlit)
EXPOSE 7860

# Set the command to run your app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
