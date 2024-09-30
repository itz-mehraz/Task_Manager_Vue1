from PIL import Image
import numpy as np

# Load the image
image_path = 'path_to_your_image.jpg'
img = Image.open(image_path)

# Ensure the image is in RGB format
img_rgb = img.convert('RGB')

# Convert the RGB image to a numpy array
image_array = np.array(img_rgb)

# Display the array
print(image_array)
