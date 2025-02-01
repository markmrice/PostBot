#!/bin/bash

# Activate the virtual environment
source /app/venv/bin/activate

# Redirect logs to the specified file and stdout
exec > >(tee -a "$LOG_FILE") 2>&1

# Run the main script
python fetch_ebay_orders.py
