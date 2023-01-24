# IMPORT PIL 
from PIL import Image

# DEFINE ASCII CHARACTERS BY SURFACE
ascii_characters_by_surface = "`^\,:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


# OPEN IMAGE

def main():
    image = Image.open("Users/Documents/imagenes/messitopo.jpeg")
    # RESIZE IMAGE
    image = image.resize((60, 60))
    ascii_art = convert_to_ascii_art(image)
    save_as_text(ascii_art)


# CONVERT TO ASCII ART

def convert_to_ascii_art(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convert_pixel_to_character(px)
        ascii_art.append(line)
    return ascii_art

def convert_pixel_to_character(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(ascii_characters_by_surface) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return ascii_characters_by_surface[index]


# SAVE AS TXT FILE

def save_as_text(ascii_art):
    with open("messitopo.txt", "a") as file:
        for line in ascii_art:
            file.write(line)
            file.write("\n")
        file.close()

main()

# From code by Emanuel Trandafir 
