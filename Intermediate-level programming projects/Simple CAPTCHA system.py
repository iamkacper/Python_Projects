""" That Simple CAPTCHA system in Python that generates random image-based CAPTCHA challenges. It uses the PIL library to create an image with distorted text."""

"""
Before running the script, install the required libraries: 

pip install pillow

"""

import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Generate a random CAPTCHA text
def generate_captcha_text(length=6):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))

# Generate a CAPTCHA image
def create_captcha_image(text, filename="captcha.png"):
    width, height = 200, 80  # Image size
    image = Image.new('RGB', (width, height), (255, 255, 255))  # White background
    draw = ImageDraw.Draw(image)

    # Load a font (change the path if needed)
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    # Randomize text position
    text_x = random.randint(10, 50)
    text_y = random.randint(10, 30)
    
    # Draw text with a random color
    draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

    # Apply distortion (optional)
    image = image.filter(ImageFilter.GaussianBlur(random.uniform(0.5, 1.5)))

    # Save the image
    image.save(filename)
    print(f"CAPTCHA saved as {filename}")

# Verify CAPTCHA
def verify_captcha(correct_text):
    user_input = input("Enter the CAPTCHA: ").strip()
    return user_input == correct_text

# Main CAPTCHA process
def captcha_system():
    captcha_text = generate_captcha_text()
    create_captcha_image(captcha_text)

    print("\nA CAPTCHA image has been generated (captcha.png). Open it and type the text below.\n")

    if verify_captcha(captcha_text):
        print("✅ CAPTCHA verified! You are human.")
    else:
        print("❌ CAPTCHA failed! Please try again.")

if __name__ == "__main__":
    captcha_system()


"""
 
How the CAPTCHA System Works?

1. Generates a random 6-character CAPTCHA (letters & digits).

2. Creates an image (captcha.png) with the CAPTCHA text.

3. Applies slight distortions to prevent easy bot detection.

4. Asks the user to enter the CAPTCHA.

5. Verifies if the entered text matches. 

"""