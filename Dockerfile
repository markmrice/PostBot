FROM python:3.10

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

# Set the entry point or command as needed
CMD ["python", "fetch_ebay_orders.py"]

