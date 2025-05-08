# Use official Rasa image (Python 3.8+, Ubuntu-based)
FROM rasa/rasa:3.6.10-full
FROM python:3.10-slim

# Set working directory
WORKDIR /rasa

# Copy the Rasa project files into the container
COPY . /rasa

# Optional: Install any custom dependencies
RUN pip install --no-cache-dir -r requirements.txt || true

# Expose Rasa default port
EXPOSE 5005

# Start Rasa with API and CORS enabled
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
