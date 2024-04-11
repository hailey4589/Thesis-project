
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import os

# Specify the image path
image_path = "C:\SCHOOL\Thesis-project\CT-2_DJI_0069.jpg"
# Check if the image file exists
if not os.path.exists(image_path):
    print("Error: Image file does not exist.")

    
image = Image.open(image_path)

# Load bounding box coordinates from the text file
annotations_file = 'C:\SCHOOL\Thesis-project\CT-2_DJI_0069.txt'

with open(annotations_file, 'r') as f:
    lines = f.readlines()

# Iterate through each line (each line contains class label followed by 4 coordinates)
for line in lines:
    parts = line.strip().split()
    class_label = parts[0]
    # Parse the coordinates (in normalized form)
    x_center, y_center, width, height = map(float, parts[1:])
    
    # Convert center coordinates and width/height to bounding box coordinates
    width = width * image.width
    height = height * image.height
    x_min = (x_center * image.width) - (width / 2)
    y_min = (y_center * image.height) - (height / 2)
    x_max = x_min + width
    y_max = y_min + height
    
    # Draw the bounding box on the image
    draw = ImageDraw.Draw(image)
    draw.rectangle([x_min, y_min, x_max, y_max], outline='red', width=3)

# Display the image with the bounding box
plt.imshow(image)
plt.axis('off')
plt.show()