#!/bin/bash
# Entrypoint script to initialize the application

# Activate the Python virtual environment
source /app/venv/bin/activate

# Function to run a script and log its output
run_script() {
    script_name=$1
    echo "Starting $script_name..." | tee -a /app/logs/postbot.log
    python "$script_name" >> /app/logs/postbot.log 2>&1
    if [ $? -eq 0 ]; then
        echo "$script_name completed successfully." | tee -a /app/logs/postbot.log
    else
        echo "Error: $script_name failed." | tee -a /app/logs/postbot.log
    fi
}

# Run each script
run_script Scripts/fetch_ebay_orders.py
run_script Scripts/generate_royal_mail_csv.py
run_script Scripts/upload_to_royalmail.py
run_script Scripts/get_tracking_numbers.py
run_script Scripts/update_ebay_orders.py

# Keep the container running by tailing the log file
exec tail -f /app/logs/postbot.log
