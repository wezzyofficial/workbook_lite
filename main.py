#!/usr/bin/env python3
import os, textwrap, math, random
from PIL import Image, ImageDraw, ImageFont


def TextToPicture(text, color=(47, 79, 159), max_char=47, max_lines=21, indent=49.5, font_size=50, notebook_picture='original_picture_1',notebook_picture2='original_picture_2', font_name='font4.otf'):
    tc = textwrap.wrap(text, max_char)
    page = 1
    for current_line in range(0, len(tc), max_lines):
        tc_part = tc[current_line:current_line + max_lines]
        print(page, tc_part, '\n\n')
        if page % 2 == 0:
            pic_name = notebook_picture
            x, y = 155, -47
        else:
            pic_name = notebook_picture2
            x, y = 15, -47
        load_font = ImageFont.truetype(os.path.join(r"fonts/") + font_name, font_size)
        open_notebook_picture = Image.open(pic_name + '.jpg')
        draw_notebook_picture = ImageDraw.Draw(open_notebook_picture)
        
        y_indent = y
        for tl_data in tc_part:
            y_indent += indent
            x_random = x - random.randint(-2, 2)
            if x_random <= 0: x_random = 1
            draw_notebook_picture.text((x_random , int(y_indent)), tl_data, color, font=load_font)
        open_notebook_picture.save('scanned_images/scanned_images_' + '_' + str(page) + '_out.jpg')
        page += 1

text='''Привет как у тебя дела?'''

TextToPicture(text=text)
