import os
import logging

# Setup logging
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)  # Ensure log directory exists
log_file = os.path.join(log_dir, "ftp_upload.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Load FTP credentials from environment variables
FTP_HOST = os.getenv("ROYALMAIL_FTP_HOST", "test.royalmail.com")
FTP_USER = os.getenv("ROYALMAIL_FTP_USER", "test_user")
FTP_PASS = os.getenv("ROYALMAIL_FTP_PASS", "test_password")
CSV_FILE = "/app/royal_mail_orders.csv"

def upload_csv():
    logging.info(f"Attempting FTP upload to {FTP_HOST} with user {FTP_USER}...")
    print(f"Simulating upload to Royal Mail FTP: {FTP_HOST}")
    print(f"Using username: {FTP_USER}")

    if not os.path.exists(CSV_FILE):
        error_message = f"CSV file {CSV_FILE} not found. Upload aborted."
        logging.error(error_message)
        print(error_message)
        return

    # Simulated FTP upload logic
    try:
        # Simulating FTP upload process
        logging.info(f"Uploading {CSV_FILE} to {FTP_HOST} (Simulated)...")
        print("CSV upload simulated successfully.")

        logging.info("Upload successful.")
    except Exception as e:
        error_message = f"FTP upload failed: {e}"
        logging.error(error_message)
        print(error_message)

if __name__ == "__main__":
    upload_csv()
