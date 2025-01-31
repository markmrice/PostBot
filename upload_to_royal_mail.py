import os

# Placeholder values for FTP testing
FTP_HOST = os.getenv("ROYALMAIL_FTP_HOST", "test.royalmail.com")
FTP_USER = os.getenv("ROYALMAIL_FTP_USER", "test_user")
FTP_PASS = os.getenv("ROYALMAIL_FTP_PASS", "test_password")

def upload_csv():
    print(f"Simulating upload to Royal Mail FTP: {FTP_HOST}")
    print(f"Using username: {FTP_USER}")
    print("CSV upload simulated successfully.")

if __name__ == "__main__":
    upload_csv()
