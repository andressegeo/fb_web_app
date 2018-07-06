#coding: utf-8
import random
#import MySQLdb
import logging
from PIL import Image, ImageDraw, ImageFont
#from config import CONFIG_DB
import os
import textwrap

import fbapp

def find_content(gender):
    print "here"
    con = fbapp.models.Content
    gen = fbapp.models.Gender
    """
    SQL Alchemy This method allow to get random content in db according to the gender pass on url
    """
    try:
        contents = con.query.filter(con.gender == gen[gender]).all()
        #contents = con.query.filter_by(gender=gen['male'])
        print "this is contents: {}".format(contents)
        return random.choice(contents)
    except BaseException, e:
        logging.error("error is: {}".format(e))

    return u"smalafde"

class OpenGraphImage:
    """
    This class help to implement image object provide by the Pillow library

    """

    
    def __init__(self, uid, first_name, description):
        self.location = self._location(uid)
        background = self.base()
        self.print_on_image(background, first_name.capitalize(), 70, 50)
        
        sentences = textwrap.wrap(description, width=60)
        current_h, pad = 180, 10
        for sentence in sentences:
            w, h = self.print_on_image(background, sentence, 40, current_h)
            current_h += h + pad
        
        #background.show()
        background.save(self._path(uid))

    
    def base(self):
        #create basic image
        img = Image.new('RGB', (1200,630), '#18BC9C')

        return img
    
    def print_on_image(self, img, text, size, height):

        font = ImageFont.truetype(os.path.join('fbapp', 'static', 'fonts',
        'Arcon-Regular.otf'), size)

        draw = ImageDraw.Draw(img)

        w, h = draw.textsize(text, font)

        position = ((img.width - w) / 2, height)

        draw.text(position, text, (255, 255, 255), font=font)
        return (w,h)


    def _path(self, uid):
        return os.path.join('fbapp', 'static', 'tmp', '{}.jpg'.format(uid))
    


    def _location(self, uid):
        """
        Return image location on tmp file

        """
        return 'tmp/{}.jpg'.format(uid)

