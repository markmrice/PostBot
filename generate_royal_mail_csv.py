import os
import pandas as pd
import logging

# Setup logging
log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)  # Ensure log directory exists
log_file = os.path.join(log_dir, "generate_csv.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def generate_csv():
    logging.info("Starting Royal Mail CSV generation...")
    print("Simulating Royal Mail CSV generation...")

    # Simulated data
    data = [
        ["John Doe", "123 Main St", "", "London", "Greater London", "UK", "Royal Mail Tracked", "Sample Product"]
    ]

    df = pd.DataFrame(data, columns=[
        "Name", "Street1", "Street2", "City", "State", "Country", "ShippingMethod", "Item"
    ])

    csv_path = "/app/royal_mail_orders.csv"

    try:
        df.to_csv(csv_path, index=False)
        success_message = f"CSV generated successfully at {csv_path}."
        logging.info(success_message)
        print(success_message)
    except Exception as e:
        error_message = f"Error generating CSV: {e}"
        logging.error(error_message)
        print(error_message)

if __name__ == "__main__":
    generate_csv()
