# Use official Python image
#FROM python:3.12-slim

# Set working directory
#WORKDIR /app

# Copy project files
#COPY . /app

# Install dependencies
#RUN pip install --upgrade pip
#RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Expose Flask port
#EXPOSE 5000

# Run the Flask app directly
#CMD ["python3", "app.py"]

# Use official Python 3.12 slim image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy the game code
COPY game.py .

# (Optional) If you have requirements.txt, uncomment this line
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Default command: run Python REPL or script
# You can also provide an entrypoint to run a test script
CMD ["python3"]
