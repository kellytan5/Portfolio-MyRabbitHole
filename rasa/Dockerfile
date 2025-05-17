# Use official Rasa image (Python 3.8+, Ubuntu-based)
FROM rasa/rasa:3.6.10-full

# Set working directory
WORKDIR /app

# Copy the Rasa project files into the container
COPY . /app

ENV SQLALCHEMY_SILENCE_UBER_WARNING=1

RUN pip install --no-cache-dir -r requirements.txt || true

# Expose Rasa default port
EXPOSE 5005

# Start Rasa with API and CORS enabled
CMD ["rasa", "run", "--enable-api", "--model", "models", "--cors", "*"]