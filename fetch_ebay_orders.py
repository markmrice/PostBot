import os
import logging

# Setup logging
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)  # Ensure log directory exists
log_file = os.path.join(log_dir, "fetch_orders.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Simulated response
response_text = "<?xml version='1.0'?><Orders><Order><OrderID>123456</OrderID></Order></Orders>"
file_path = "/app/orders.xml"

try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response_text)
    message = f"Orders saved successfully to {file_path}"
    logging.info(message)
    print(message)
except Exception as e:
    error_message = f"Error writing file: {e}"
    logging.error(error_message)
    print(error_message)

# Verify that the file exists after writing
if os.path.exists(file_path):
    verification_msg = f"Verification: {file_path} exists."
    logging.info(verification_msg)
    print(verification_msg)
else:
    verification_msg = f"Verification: {file_path} was NOT created."
    logging.error(verification_msg)
    print(verification_msg)
