import os
import matplotlib.pyplot as plt
from PIL import Image

# Directory containing the images
image_directory = './QR_CODE_IMAGES/19-12-2024/'

# Get a list of all image files in the directory
image_files = [file for file in os.listdir(image_directory) if file.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Check if there are any images
if not image_files:
    print("No images found in the directory.")
else:
    # Define container layout width and height (in centimeters)
    container_width_cm = 15    # Width of the layout container
    container_height_cm = 15   # Height of the layout container

    # Convert to inches
    container_width = container_width_cm / 2.54
    container_height = container_height_cm / 2.54

    # Number of rows and columns in the grid
    rows = 4
    cols = 4

    # Calculate the number of images we can display (at most 4x4 grid)
    num_images = min(len(image_files), rows * cols)

    # Create a new figure for the grid with defined container size
    fig, axes = plt.subplots(rows, cols, figsize=(container_width, container_height))

    # Flatten the axes array to easily iterate over
    axes = axes.flatten()

    # Loop through the images and add them to the grid
    for i in range(num_images):
        image_path = os.path.join(image_directory, image_files[i])
        img = Image.open(image_path)

        # Convert the image to RGB (to prevent black images in some cases)
        img = img.convert('RGB')

        # Display the image
        axes[i].imshow(img)
        axes[i].axis('off')  # Hide axes for a cleaner look

    # Hide any unused axes if there are fewer images than slots in the grid
    for i in range(num_images, len(axes)):
        axes[i].axis('off')

    # Show the grid with adjusted layout
    plt.tight_layout()
    plt.show()
