#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    "assets",
    "covers",  # Make it dynamic to work with 'assets/covers'
)
libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
)
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
import traceback
from waveshare_OLED import OLED_1in5_rgb
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    disp = OLED_1in5_rgb.OLED_1in5_rgb()

    logging.info("\r 1.5inch rgb OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

    # Draw image
    logging.info("***draw image")
    Himage2 = Image.new("RGB", (disp.width, disp.height), 0)  # 0: clear the frame

    # Get all images in assets/covers and display them
    if os.path.exists(picdir):
        for filename in os.listdir(picdir):
            if filename.lower().endswith(
                (".png", ".jpg", ".jpeg", ".bmp")
            ):  # Check for image extensions
                try:
                    bmp = Image.open(os.path.join(picdir, filename))
                    bmp = bmp.resize((disp.width, disp.height), Image.BILINEAR)
                    Himage2.paste(bmp, (0, 0))
                    Himage2 = Himage2.rotate(0)
                    disp.ShowImage(disp.getbuffer(Himage2))
                    time.sleep(10)  # Display each image for 10 seconds
                    disp.clear()
                except Exception as e:
                    logging.error(f"Error displaying image {filename}: {e}")
                    continue
    else:
        logging.error("The 'assets/covers' directory was not found.")

    # Display "Done!" text after all images have been shown
    logging.info("*** Displaying 'Done!' text")
    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")  # Black background
    draw = ImageDraw.Draw(image1)
    font = ImageFont.truetype(
        os.path.join(picdir, "Font.ttc"), 24
    )  # Use a suitable font and size
    draw.text((20, 40), "Done!", font=font, fill="GREEN")  # Position the text
    disp.ShowImage(disp.getbuffer(image1))  # Display the "Done!" message
    time.sleep(3)  # Show the "Done!" message for 3 seconds

    disp.clear()  # Clear the screen after displaying "Done!"

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
