FROM python:3.10-slim

# Create a non-root user
RUN useradd -m myuser

# Set the working directory
WORKDIR /app

# Create the logs directory and set permissions
RUN mkdir -p /app/logs && chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Copy the application code and set ownership
COPY --chown=myuser:myuser . .

# Create a virtual environment and install dependencies
RUN python -m venv /app/venv \
    && . /app/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Add a health check (optional)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost:8080/ || exit 1

# Set the entry point or command as needed
CMD ["/bin/bash", "-c", "source /app/venv/bin/activate && python fetch_ebay_orders.py"]
