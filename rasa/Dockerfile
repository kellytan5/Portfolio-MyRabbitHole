# Use official Rasa image with a compatible Python version
FROM rasa/rasa:3.6.10-full

# Set working directory
WORKDIR /app

# Copy your Rasa project files
COPY . /app

# Ensure the model folder exists (optional fallback)
RUN rasa train || echo "Skipping training (model may already exist)"

# Run the Rasa server with CORS and API enabled
CMD ["run", "--enable-api", "--cors", "*", "--debug"]