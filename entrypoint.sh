#!/bin/bash
# Entrypoint script to initialize the application

# Activate the Python virtual environment
source /app/venv/bin/activate

# Run the main script
exec python fetch_ebay_orders.py
exec python generate_royal_mail_csv.py
exec python upload_to_royalmail.py
exec python get_tracking_numbers.py
exec python update_ebay_orders.py