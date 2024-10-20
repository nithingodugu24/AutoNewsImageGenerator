from PIL import ImageFont, Image, ImageDraw, ImageFont, ImageFilter


# Create a new 1080x1080 image with a black background
img = Image.new("RGBA", (1080, 1080), color="black")

draw = ImageDraw.Draw(img)

# Load the font
font = ImageFont.truetype("font/Poppins-Bold.ttf", size=60)

# Load the overlay image
overlay = Image.open("img1.webp")
o_w, o_h = overlay.size
overlay = overlay.resize((1080, o_h))

# Paste the resized overlay onto the background
resized_image = overlay.resize((1080, 1080))

blurred_background = resized_image.filter(ImageFilter.GaussianBlur(10))
blurred_background.putalpha(10)
img.paste(blurred_background, (0, 0))
img.paste(overlay, (0, 0))

black_overlay = Image.open("new_black_overlay.png")
# black_overlay = black_overlay.resize((1080, 1080))
img = img.resize((1080, 1080))
img = Image.alpha_composite(img.convert("RGBA"), black_overlay.convert("RGBA"))


# img = Image.alpha_composite(img, black_overlay)
# text = "Instagram Post Title"

# # Calculate text size
# text_size = draw.textsize(text, font=font)

# # Calculate the Y position to center the text
# text_position = ((1080 - text_size[0]) // 2, 0)  # Center horizontally; keep Y fixed

# Add text to the image
# draw.text(text_position, text, fill="yellow", font=font)

# Save and show the result
img.save("instagram_post.jpg")
img.show()
