import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def generate_image(text):
    img = Image.open("dark.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assfont.ttf", 50)
    x, y = 150, 140
    lines = text.split("\n")
    line_height = 45 #font.getsize("hg")[1]  # Calculate line height
    for line in lines:
        draw.text((x, y), line, fill=(255, 255, 255), font=font)
        y += line_height - 5
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file = f"output/writer-{current_time}.jpg"
    img.save(file)
    return file

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

# Ask for text input
text_input = "Welcome\nTo\nThis\nExperiment" #input("Enter the text: ")

# Generate image
image_file = generate_image(text_input)
print("Image file:", image_file)
