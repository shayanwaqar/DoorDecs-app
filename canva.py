from PIL import Image, ImageDraw, ImageFont
from collections import Counter

Alist = []
Blist = []
Clist = []
Dlist = []
Atup =  []
STANDARD_SIZE = (900, 1000)

names = open("names.txt")
name_list = names.readlines()

rooms = open("rooms.txt")
room_list = rooms.readlines()

for i in range(len(name_list)):
    tname = name_list[i].strip()
    troom = room_list[i].strip()
    Atup.append((tname, troom))

    if troom[-1] == 'A' or troom[-1] == 'E':
        Alist.append(tname)

    elif troom[-1] == 'B' or troom[-1] == 'F':
        Blist.append(tname)

    elif troom[-1] == 'C':
        Clist.append(tname)

    elif troom[-1] == 'D':
        Dlist.append(tname)
    else:
        print("ISSUE name: ",tname, " room: ", troom)

#Okay so now Alist, Blist, Clist, and Dlist all hold tuples with names

def makeDoorDecs(name_list, image_file, ycoordinate, default_font_size, font_color):
    names = name_list
    
    # Path to your template image
    template_path = 'images/' + image_file
    # Path to save the generated images
    output_dir = 'output_dir/'
    # List of names to add to the template

    # Load your template
    template = Image.open(template_path)

    # Font settings (ensure the font file is available in the specified path)
    font_path = 'sports_world.ttf'
    font_size = default_font_size

    # Coordinates where the text should be placed (adjust these according to your template)
    text_y = ycoordinate

    # Center-alignment adjustments
    template_width, template_height = template.size

    # Shadow settings
    shadow_offset = 5  
    shadow_color = "black" # <-- Highlighted in red

    for name in names:
        #reset the font_size to default so it doesn't change between names
        font_size = default_font_size 
        
        if len(name) > 5 and image_file == "tennis.png":
            print("NAME IS ", name)
            font_size = 100 if (len(name) > 10) else 140
        
        if len(name) > 10 and image_file == "cricket.png":
            print("NAME IS ", name)
            font_size = 33

        if len(name) <= 6 and image_file == "football.png":
            print("NAME IS ", name)
            font_size = 225

        if len(name) >= 10 and image_file == "americanFootball.png":
            print("NAME IS ", name)
            font_size = 120 if (len(name) > 10) else 150

        font = ImageFont.truetype(font_path, font_size)
        # Create a copy of the template to draw on
        image = template.copy()
        draw = ImageDraw.Draw(image)

        # Calculate text size and position for center alignment
        text_bbox = draw.textbbox((0, 0), name.upper(), font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        adjusted_text_x = (template_width - text_width) / 2
        adjusted_text_y = text_y  # Adjust if needed based on the vertical position of "SHAYAN"
        
        # Draw shadow texts, in front and behind of main text.
        draw.text((adjusted_text_x + shadow_offset, adjusted_text_y + shadow_offset), name.upper(), font=font, fill=shadow_color)
        draw.text((adjusted_text_x - shadow_offset, adjusted_text_y - shadow_offset), name.upper(), font=font, fill=shadow_color)
        
        # Add text to the image
        draw.text((adjusted_text_x, adjusted_text_y), name.upper(), font=font, fill=font_color)
        
        # Resize the image to the standard size
        image = image.resize(STANDARD_SIZE)

        # Save the new image
        output_path = f"{output_dir}{name}.png"
        image.save(output_path)
        print(f"Created image for {name}: {output_path}")

    print("All images created successfully for ", image_file)


names = ['Arunnganabathy!!', 'Bravo', "Annalise Marie"]
# makeDoorDecs(Alist, "cricket.png", 330, 50, "white")
# makeDoorDecs(Blist, "football.png", 480, 200, "white")
# makeDoorDecs(Clist, "americanFootball.png", 300, 200, "white")
# makeDoorDecs(Dlist, "tennis.png", 860, 185, "white")