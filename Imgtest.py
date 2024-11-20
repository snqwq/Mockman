#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "assets/covers"
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
    bmp = Image.open(os.path.join(picdir, "NOTION.jpg"))
    bmp = bmp.resize((disp.width, disp.height), Image.BILINEAR)
    Himage2.paste(bmp, (0, 0))
    Himage2 = Himage2.rotate(0)
    disp.ShowImage(disp.getbuffer(Himage2))
    time.sleep(10)

    disp.clear()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
