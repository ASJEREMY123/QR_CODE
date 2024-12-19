import os
from PIL import Image, ImageDraw, ImageFont

# Directory containing the images
image_directory = './QR_CODE_IMAGES/19-12-2024/'

# Get a list of all image files in the directory
image_files = [file for file in os.listdir(image_directory) if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Check if we have more than 16 images
if len(image_files) > 16:
    print("Warning: There are more than 16 images. Only the first 16 will be used.")

# Use at most 16 images
image_files = image_files[:16]

# Number of rows and columns in the grid
rows = 2
cols = 8

# Image width and height for each grid cell
image_width = 200  # Adjust based on your image size
image_height = 200  # Adjust based on your image size
text_height = 20  # Space for the text below each image

# Pre-define font size
predefined_font_size = 8  # Set the font size for the text (slightly larger to reduce blurriness)

# Create a new blank image with enough space to fit all the images
grid_width = cols * image_width
grid_height = rows * (image_height + text_height)  # Add space for text below the image
grid_image = Image.new("RGB", (grid_width, grid_height), color=(255, 255, 255))  # White background

# Load the font with the predefined size
font_path = "arial.ttf"  # Adjust the path if necessary
font = ImageFont.truetype(font_path, predefined_font_size)

# Loop through each image and place it in the grid
for i, image_file in enumerate(image_files):
    # Load the image
    image_path = os.path.join(image_directory, image_file)
    img = Image.open(image_path)

    # Resize the image to fit the grid cell
    img = img.resize((image_width, image_height))

    # Calculate the position for this image in the grid
    row = i // cols
    col = i % cols
    x_position = col * image_width
    y_position = row * (image_height + text_height)  # Adjust y position for the text space

    # Paste the image into the grid
    grid_image.paste(img, (x_position, y_position))

    # Draw the filename text below the image
    draw = ImageDraw.Draw(grid_image)

    # Remove the file extension from the image file name
    text = os.path.splitext(image_file)[0]  # Get the file name without the extension

    # Get the bounding box of the text to center it
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Calculate the width of the text
    text_x = x_position + (image_width - text_width) // 2  # Center the text horizontally
    text_y = y_position + image_height  # Position text below the image

    # Draw the text
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))  # Black text

# Save the final image with the 2x8 grid layout
output_file = './QR_CODE_IMAGES/grid_image_with_filenames.png'
grid_image.save(output_file)

print(f"Grid image with filenames saved successfully as {output_file}")
