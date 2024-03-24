# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy and install requirements first to leverage Docker's caching mechanism
COPY requirements.txt .

# Install bot dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot's source code into the container
COPY . .

# Command to run the bot
CMD ["python", "bot.py"]
