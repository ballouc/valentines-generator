from PIL import Image, ImageDraw, ImageFont
import os

'''
This program is an automation of generating Valentines day cards
using a template saved as a .png in a set location.

All Valentines strings are located in the 'valentine_list'
and should be kept in the format of ["Message 1", "Message 2", "Message n"]
'''

# template_path is equal to the location of the template object.
template_path = ""
template_image = Image.open(template_path)

# font_path is the location of the .ttf file
# I used a custom valentines font.
font_path = "./cute_font.ttf"
font_size = 28
font = ImageFont.truetype(font_path, font_size)
text_color = (255, 255, 255)

# This array is filled with strings containing Valentines messages.
valentine_list = []

# If a 'completed_valentines' folder does not exist, create it and save all output images in that folder.
output_dir = "./completed_valentines"
os.makedirs(output_dir, exist_ok=True)

for i, valentine in enumerate(valentine_list):
    
    # Copy the image template and create a new image
    new_image = template_image.copy()

    draw = ImageDraw.Draw(new_image)
    text_width, text_height = draw.textsize(valentine, font=font)

    # Text height is slightly altered to match the offset location on the template.
    text_position=((new_image.width - text_width) // 2, (new_image.height - text_height - 40) // 2)

    # Calling the text function of our new draw object allows us to input
    # position, desired text, and other properties of our text function.
    draw.text(text_position, valentine, fill=text_color, font=font)

    # Ensure to save each image as a unique name, in this case as its position in the array
    output_path = os.path.join(output_dir, f"image_{i+1}.png")
    # Actual save function
    new_image.save(output_path)

# If this line is reached, the program executed successfully.
print("All images generated successfully")