import os
import pandas as pd

def write_log(message):
    """Helper function to append log messages to postbot.log."""
    with open("/app/postbot.log", "a") as log_file:
        log_file.write(message + "\n")

def generate_csv():
    write_log("Starting Royal Mail CSV generation...")

    # Simulated data
    data = [
        ["John Doe", "123 Main St", "", "London", "Greater London", "UK", "Royal Mail Tracked", "Sample Product"]
    ]

    try:
        df = pd.DataFrame(data, columns=[
            "Name", "Street1", "Street2", "City", "State", "Country", "ShippingMethod", "Item"
        ])
        df.to_csv("/app/royal_mail_orders.csv", index=False)
        write_log("Royal Mail CSV generated successfully at /app/royal_mail_orders.csv.")
    except Exception as e:
        write_log(f"Error generating Royal Mail CSV: {e}")

if __name__ == "__main__":
    generate_csv()
