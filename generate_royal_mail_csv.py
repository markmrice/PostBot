import json
import pandas as pd

def generate_csv():
    print("Simulating Royal Mail CSV generation...")

    # Simulated data (instead of reading from API)
    data = [
        ["John Doe", "123 Main St", "", "London", "Greater London", "UK", "Royal Mail Tracked", "Sample Product"]
    ]

    df = pd.DataFrame(data, columns=[
        "Name", "Street1", "Street2", "City", "State", "Country", "ShippingMethod", "Item"
    ])

    df.to_csv("royal_mail_orders.csv", index=False)
    print("CSV Generated successfully (Simulated).")

if __name__ == "__main__":
    generate_csv()
