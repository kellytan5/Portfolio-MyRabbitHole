# Use official Rasa image (Python 3.8+, Ubuntu-based)
FROM rasa/rasa:3.6.10-full
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the Rasa project files into the container
COPY . /app

# RUN rasa train 

# Expose Rasa default port
EXPOSE 5005

# Start Rasa with API and CORS enabled
CMD ["rasa", "run", "--enable-api", "--cors", "*", "--debug"]
