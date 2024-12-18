#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

# Dynamically find the path to the 'assets/covers' folder
script_dir = os.path.dirname(
    os.path.realpath(__file__)
)  # Get the directory where the script is located
assets_dir = os.path.join(
    script_dir, "assets", "covers"
)  # Construct the path to 'assets/covers'

libdir = os.path.join(script_dir, "lib")
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
    if os.path.exists(assets_dir):
        for filename in os.listdir(assets_dir):
            if filename.lower().endswith(
                (".png", ".jpg", ".jpeg", ".bmp")
            ):  # Check for image extensions
                try:
                    bmp = Image.open(os.path.join(assets_dir, filename))
                    bmp = bmp.resize((disp.width, disp.height), Image.BILINEAR)
                    Himage2.paste(bmp, (0, 0))
                    Himage2 = Himage2.rotate(0)
                    disp.ShowImage2(disp.getbuffer(Himage2))
                    time.sleep(5)  # Display each image for 5 seconds
                    disp.clear()
                except Exception as e:
                    logging.error(f"Error displaying image {filename}: {e}")
                    continue
    else:
        logging.error("The 'assets/covers' directory was not found.")

except IOError as e:
    logging.error(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
