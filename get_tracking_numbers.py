import os
import json
import logging

# Setup logging
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)  # Ensure log directory exists
log_file = os.path.join(log_dir, "tracking.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Simulated tracking data retrieval
def get_tracking():
    logging.info("Starting tracking retrieval from Royal Mail API (Simulated)...")
    print("Simulating tracking retrieval from Royal Mail API...")

    tracking_data = {
        "orders": [
            {"orderID": "123456", "trackingNumber": "RM123TRACK"}
        ]
    }

    # Save tracking numbers to a file
    tracking_file = "/app/tracking.json"
    try:
        with open(tracking_file, "w", encoding="utf-8") as f:
            json.dump(tracking_data, f, indent=4)
        
        success_message = f"Tracking numbers saved to {tracking_file}."
        logging.info(success_message)
        print(success_message)
    except Exception as e:
        error_message = f"Error writing tracking file: {e}"
        logging.error(error_message)
        print(error_message)

    logging.info(f"Tracking Data: {tracking_data}")
    print(f"Tracking Data: {tracking_data}")
    print("Tracking numbers retrieved successfully (Simulated).")

if __name__ == "__main__":
    get_tracking()
