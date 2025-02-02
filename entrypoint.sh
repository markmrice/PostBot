#!/bin/bash
# Entrypoint script to initialize the application

# Activate the Python virtual environment
source /app/venv/bin/activate

# Function to run a script and log its output
run_script() {
    script_name=$1
    params=$2
    echo "Starting $script_name with params: $params" | tee -a /app/logs/postbot.log
    output=$(python "$script_name" $params 2>&1)
    echo "$output" >> /app/logs/postbot.log
    if [ $? -eq 0 ]; then
        echo "$script_name completed successfully." | tee -a /app/logs/postbot.log
    else
        echo "Error: $script_name failed." | tee -a /app/logs/postbot.log
        exit 1
    fi
    echo "$output"
}

# Run each script and pass parameters between them
orders_file=$(run_script Scripts/fetch_ebay_orders.py)
csv_file=$(run_script Scripts/generate_royal_mail_csv.py "$orders_file")
upload_result=$(run_script Scripts/upload_to_royal_mail.py "$csv_file")
tracking_info=$(run_script Scripts/get_tracking_numbers.py "$upload_result")
run_script Scripts/update_ebay_orders.py "$tracking_info"

# Keep the container running by tailing the log file
exec tail -f /app/logs/postbot.log