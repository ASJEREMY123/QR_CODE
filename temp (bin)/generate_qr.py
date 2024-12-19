import pandas as pd
import qrcode
from io import BytesIO
from PIL import Image
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as OpenpyxlImage

# Load the Excel file
file_path = '../data/sample_data.xlsx'
output_file = '../data/product_data.xlsx'
data = pd.read_excel(file_path)

# Ensure the column name is 'SKU' (or replace with the correct column name)
if 'SKU' not in data.columns:
    raise ValueError("The column 'SKU' does not exist in the data.")

# Add a new column for QR Codes
data['QR Code'] = None

# Save the DataFrame to an Excel file first to insert images
data.to_excel(output_file, index=False)

# Open the Excel file with openpyxl to add QR codes as images
wb = load_workbook(output_file)
ws = wb.active

# Loop through each SKU and generate QR codes
for row_index, sku in enumerate(data['SKU'], start=2):  # Excel rows start at 2 (1 for header)
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

    # Save the QR code to an in-memory file
    qr_image = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)

    # Insert the image into the Excel file
    qr_img = OpenpyxlImage(buffer)
    ws.add_image(qr_img, f'D{row_index}')  # Adjust 'D' to the column for QR Code

# Save the updated Excel file
wb.save(output_file)

print(f"QR codes added successfully to {output_file}!")
