from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap

news_image_path = "img1.webp"
overlay_path = "new_black_overlay.png"
logo_path = "logo_template.png"

news_image = Image.open(news_image_path)
overlay = Image.open(overlay_path)
logo = Image.open(logo_path)

max_width = 1080
max_height = 900

news_image.thumbnail((max_width, max_height), Image.ANTIALIAS)
news_width, news_height = news_image.size


background = Image.new("RGB", (1080, 1080), color="black")


blurred_image = (
    news_image.copy().resize((1081, 1081)).filter(ImageFilter.GaussianBlur(15))
)
background.paste(blurred_image, (0, 0))


def image_fit(w, h):
    max_width = 1080
    max_height = 900
    aspect_ratio = w / h
    for _ in range(0, 1080):
        if w >= max_width or h >= max_height:
            break
        h += 1
        w += aspect_ratio

    return int(w), int(h)


img_w, img_h = news_image.size

img_w, img_h = image_fit(img_w, img_h)
news_image = news_image.resize((img_w, img_h))

img_w, img_h = news_image.size
print("height", img_w, img_h)
if img_w >= 1080:
    w_org = 0
else:
    w_org = abs((max_width - img_w) // 2)

if img_h >= 1080 or img_h == max_height:
    h_org = 0
else:
    h_org = abs((max_height - img_h) // 2)
print(f"worg = {w_org} h_org {h_org}")

background.paste(news_image, (w_org, h_org))
# background.paste(
#     news_image, ((max_width - news_width) // 2, (max_height - news_height) // 2)
# )

overlay = overlay.resize((1500, 1080), Image.ANTIALIAS)
background.paste(overlay, (0, 0), overlay)

draw = ImageDraw.Draw(background)
font = ImageFont.truetype("font/static/Oswald-Medium.ttf", 40)  # Adjust font size

text = "'Har koi Har koi bachana chahta hai'  whether Baba Siddique was murdered 'because of  "

text_box_height = 300  # Height area for text


def wrap_text(text, font, max_width):
    lines = []
    words = text.split(" ")
    current_line = ""

    for word in words:
        # Check width of the line with the next word added
        test_line = current_line + word + " "
        text_width, _ = draw.textsize(
            test_line,
            font=font,
            spacing=7,
        )

        if text_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)
    return lines


no_words = len(text.split(" "))
if no_words < 10:
    text_size = 70
elif no_words < 15:
    text_size = 65
elif no_words < 20:
    text_size = 60
elif no_words < 30:
    text_size = 55
elif no_words < 40:
    text_size = 45
else:
    text_size = 40
font = ImageFont.truetype("font/static/Oswald-Medium.ttf", text_size)

wrapped_text_lines = wrap_text(text, font, (max_width - 30))

line_height = draw.textsize("A", font=font)[1]
total_text_height = (line_height + 5) * len(wrapped_text_lines)

if len(wrapped_text_lines) >= 5:
    text_min_start = 660
    text_y = (
        text_min_start + (((1080 - text_min_start) - (total_text_height)) // 2) - 10
    )

else:
    text_min_start = 750
    text_y = (
        text_min_start + (((1080 - text_min_start) - (total_text_height)) // 2) - 50
    )


for line in wrapped_text_lines:
    text_width, _ = draw.textsize(line, font=font)
    text_x = (max_width - text_width) // 2
    draw.text(
        (text_x, text_y),
        line,
        fill="#fff",
        font=font,
        spacing=7,
    )
    text_y += line_height

logo = logo.resize((1080, 1080), Image.ANTIALIAS)
background.paste(logo, (0, 0), logo)

background.save("instagram_post_with_text.jpg")
background.show()
