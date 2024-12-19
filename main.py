import os
import pandas as pd
import qrcode
from datetime import datetime

# Replace 'your_file.xlsx' with the path to your .xlsx file
file_path = 'data/product_data.xlsx'

# Read the Excel file
data = pd.read_excel(file_path)

# Base directory for storing QR codes
base_dir = './QR_CODE_IMAGES'

# Create a subfolder named with the current date
current_date = datetime.now().strftime('%d-%m-%Y')  # Format: DD-MM-YYYY
output_dir = os.path.join(base_dir, current_date)
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Ensure the column name is 'SKU' (or replace with the correct column name)
if 'SKU' not in data.columns:
    raise ValueError("The column 'SKU' does not exist in the data.")

# Loop through each SKU and generate QR codes
for index, sku in enumerate(data['SKU']):
    # Skip empty or null values
    if pd.isna(sku):
        continue

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(sku)
    qr.make(fit=True)

    # Save QR code as an image
    # file_path = os.path.join(output_dir, f'sku_qrcode_{index}.png')
    file_path = os.path.join(output_dir, f'{sku}.png')
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)  # Save with a unique name per SKU

print(f"QR codes generated successfully in {output_dir}")
