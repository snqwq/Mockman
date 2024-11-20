#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os
import logging
from waveshare_OLED import OLED_1in5_rgb

logging.basicConfig(level=logging.DEBUG)

try:
    disp = OLED_1in5_rgb.OLED_1in5_rgb()

    logging.info("\r 1.5inch rgb OLED ")
    # Initialize library.
    disp.Init()
    # Clear display.
    logging.info("clear display")
    disp.clear()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    disp.module_exit()
    exit()
