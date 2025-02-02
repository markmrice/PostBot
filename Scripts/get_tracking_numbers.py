import os

def write_log(message):
    """Helper function to append log messages to postbot.log."""
    with open("/app/postbot.log", "a") as log_file:
        log_file.write(message + "\n")
        print(message)  # Add this for debugging

def get_tracking():
    write_log("Starting tracking retrieval from Royal Mail API...")

    # Simulated tracking response
    tracking_data = {
        "orders": [
            {"orderID": "123456", "trackingNumber": "RM123TRACK"}
        ]
    }

    try:
        write_log(f"Tracking Data: {tracking_data}")
        write_log("Tracking numbers retrieved successfully.")
    except Exception as e:
        write_log(f"Error retrieving tracking numbers: {e}")

if __name__ == "__main__":
    get_tracking()
