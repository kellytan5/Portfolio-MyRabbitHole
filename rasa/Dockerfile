FROM rasa/rasa:3.6.10

# Copy Rasa project files
COPY . /app

WORKDIR /app

# Train the model (optional, or can be done manually before pushing)
RUN rasa train

# Run Rasa server
CMD ["run", "--enable-api", "--cors", "*", "--debug"]