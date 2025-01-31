import os

# Simulated response
response_text = "<?xml version='1.0'?><Orders><Order><OrderID>123456</OrderID></Order></Orders>"

# Define file path
file_path = "orders.xml"

try:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response_text)
    print(f"Orders saved successfully to {file_path}")
except Exception as e:
    print(f"Error writing file: {e}")

# Verify that the file exists after writing
if os.path.exists(file_path):
    print(f"Verification: {file_path} exists.")
else:
    print(f"Verification: {file_path} was NOT created.")
