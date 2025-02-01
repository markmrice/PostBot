import os

response_text = "<?xml version='1.0'?><Orders><Order><OrderID>123456</OrderID></Order></Orders>"
file_path = "/app/orders.xml"

def write_log(message):
    """Helper function to append log messages to postbot.log."""
    with open("/app/postbot.log", "a") as log_file:
        log_file.write(message + "\n")

try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response_text)
    write_log(f"Orders saved successfully to {file_path}")
except Exception as e:
    write_log(f"Error writing file: {e}")

if os.path.exists(file_path):
    write_log(f"Verification: {file_path} exists.")
else:
    write_log(f"Verification: {file_path} was NOT created.")
