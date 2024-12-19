import os
from PIL import Image

# Directory containing the images
image_directory = './QR_CODE_IMAGES/19-12-2024/'

# Get a list of all image files in the directory
image_files = [file for file in os.listdir(image_directory) if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Check if there are any images
if not image_files:
    print("No images found in the directory.")
else:
    # Loop through and display each image
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        print(f"Displaying image: {image_file}")

        # Open and display the image
        img = Image.open(image_path)
        img.show()  # This opens the image in the default image viewer

print("All images displayed.")
