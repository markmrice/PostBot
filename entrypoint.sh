#!/bin/bash
# Entrypoint script to initialize the application

# Activate the Python virtual environment
source /app/venv/bin/activate

# Run the main script
exec python fetch_ebay_orders.py
