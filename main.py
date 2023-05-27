import os
from PIL import Image, ImageDraw, ImageFont

def generate_image(text):
    img = Image.open("template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assfont.ttf", 30)
    x, y = 150, 140
    lines = text.split("\n")
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "generated.jpg"
    img.save(file)
    return file

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# Ask for text input
text_input = input("Enter the text: ")

# Generate image
image_file = generate_image(text_input)
print("Image file:", image_file)
