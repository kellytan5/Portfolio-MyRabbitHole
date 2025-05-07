# Use official Rasa image (Python 3.8+, Ubuntu-based)
FROM rasa/rasa:3.6.10-full

# Set working directory
WORKDIR /app

# Optionally train model if no model exists
RUN rasa train

# Expose Rasa default port
EXPOSE 5005

# Start Rasa with API and CORS enabled
CMD ["run", "--enable-api", "--cors", "*", "--debug"]
