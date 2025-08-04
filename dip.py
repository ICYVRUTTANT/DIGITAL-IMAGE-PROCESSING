from PIL import Image

# Open the image
img = Image.open("input.jpg")
pixels = img.load()

# Get image dimensions
width, height = img.size

# Loop through all pixels
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]

        # Manual grayscale conversion (weighted average for better accuracy)
        gray = int(0.299 * r + 0.587 * g + 0.114 * b)

        # Set new pixel value
        pixels[x, y] = (gray, gray, gray)

# Save the black and white image
img.save("output_bw.jpg")
img.show()
