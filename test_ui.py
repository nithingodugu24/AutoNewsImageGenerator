# print(image_fit(10, 10))
from PIL import Image

# Open an image file
image = Image.open("img1.webp")

# Get the size of the image
width, height = image.size

# Print the width and height
print(f"Width: {width}, Height: {height}")

# Calculate the aspect ratio
aspect_ratio = width / height
print(f"Aspect Ratio: {aspect_ratio:.2f}")


def image_fit(w, h):
    max_width = 1080
    max_height = 780
    aspect_ratio = w / h
    for _ in range(0, 1080):
        if w >= max_width or h >= max_height:
            break
        h += 1
        w += aspect_ratio

    return w, h


print(image_fit(image.size))
