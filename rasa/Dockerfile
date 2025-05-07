# Use official Rasa image (Python 3.8+, Ubuntu-based)
FROM rasa/rasa:3.6.10-full

# Set working directory
WORKDIR /app

# Copy only necessary files first for caching benefits
# COPY ./requirements.txt ./requirements.txt

# Install any extra dependencies first
# RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
# COPY . .

# Optionally train model if no model exists
RUN rasa train || echo "Skipping training (model may already exist)"

# Expose Rasa default port
EXPOSE 5005

# Start Rasa with API and CORS enabled
CMD ["run", "--enable-api", "--cors", "*", "--debug"]
