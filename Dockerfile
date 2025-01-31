# Use an official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Create a non-root user
RUN useradd -m myuser

# Ensure the new user owns the working directory
RUN chown -R myuser:myuser /app

# Switch to non-root user
USER myuser

# Copy project files and set correct ownership
COPY --chown=myuser:myuser . .

# Create a virtual environment & install dependencies
RUN python -m venv /app/venv \
    && . /app/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Ensure the virtual environment is always activated
ENV PATH="/app/venv/bin:$PATH"

# Run the main script and log output
CMD ["sh", "-c", "python fetch_ebay_orders.py | tee /app/logs/output.log"]