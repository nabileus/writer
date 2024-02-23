import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def generate_image(text,page):
    img = Image.open("dark.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assfont.ttf", 90)
    mont = ImageFont.truetype("assfont.ttf", 30)
    x, y = 25,200
    a = str(page)
    draw.text((15,15), a , fill=(255, 255, 255), font=mont)
    lines = text.split("\n")
    line_height = 45
    for line in lines:
        draw.text((x, y), line, fill=(255, 255, 255), font=font)
        y += line_height - 5
    current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    file = f"output/writer-{current_time}.jpg"
    img.save(file)
    return file

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        page=187
        for word in words:
            page=page+1
            generate_image(word,page)
          

# Modify the file path as per your text file's location
text_file_path = "input.txt"  # Change this to your text file's path

# Process the text file
process_text_file(text_file_path)
