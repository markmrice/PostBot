import os

# Placeholder FTP environment variables
FTP_HOST = os.getenv("ROYALMAIL_FTP_HOST", "test.royalmail.com")
FTP_USER = os.getenv("ROYALMAIL_FTP_USER", "test_user")
FTP_PASS = os.getenv("ROYALMAIL_FTP_PASS", "test_password")

def write_log(message):
    """Helper function to append log messages to postbot.log."""
    with open("/app/postbot.log", "a") as log_file:
        log_file.write(message + "\n")

def upload_csv():
    write_log(f"Starting upload to Royal Mail FTP server: {FTP_HOST}")

    try:
        # Simulated upload process
        write_log(f"Using FTP credentials: Username={FTP_USER}")
        write_log("CSV upload simulated successfully.")
    except Exception as e:
        write_log(f"Error uploading CSV: {e}")

if __name__ == "__main__":
    upload_csv()
