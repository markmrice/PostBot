FROM python:3.10-slim

# Create a non-root user
RUN useradd -m myuser

# Set the working directory
WORKDIR /app

# Create necessary directories and files with proper permissions
RUN mkdir -p /app/logs && \
    touch /app/logs/postbot.log && \
    chown -R myuser:myuser /app && \
    chmod -R 777 /app

# Switch to the non-root user
USER myuser

# Copy the application code
COPY --chown=myuser:myuser . .

# Set up a Python virtual environment and install dependencies
RUN python -m venv /app/venv \
    && . /app/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Set environment variables for logging
ENV LOG_FILE="/app/logs/postbot.log"

# Use a script for more control over the execution and logging
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Default entry point
CMD ["/app/entrypoint.sh"]
