#!/bin/bash
# Entrypoint script to initialize the application

# Activate the Python virtual environment
source /app/venv/bin/activate

# Run each script in sequence
python fetch_ebay_orders.py
python generate_royal_mail_csv.py
python upload_to_royalmail.py
python get_tracking_numbers.py
python update_ebay_orders.py

# Keep the container running by tailing the log file
exec tail -f /app/logs/postbot.log
