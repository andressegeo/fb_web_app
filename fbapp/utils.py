#coding: utf-8
import random
import MySQLdb
import logging
from PIL import Image, ImageDraw, ImageFont
from config import CONFIG_DB
import os
import textwrap


def connect():
    """
    As her name indicates, this method allow to connected on the database
    """
    #db = CONFIG_DB[u"db"]
    con  = MySQLdb.connect(
        host = CONFIG_DB[u"db"][u"host"],
        user = CONFIG_DB[u"db"][u"user"],
        passwd = CONFIG_DB[u"db"][u"password"],
        db = CONFIG_DB[u"db"][u"database"],
        charset=u"utf8",
        use_unicode=True)

    cursor = con.cursor()
    return cursor, con

def find_content(gender):
    """
    This method allow to get random content in db according to the gender pass on url
    """
    print "genre: ",gender

    if gender is None:
        print "yass"
        gender = 1

    items = []

    try:
        print "here"

        cursor, con = connect()
        query = u"SELECT * FROM content where genre={}".format(str(gender)) 
        print query
        cursor.execute(query)
        for row in cursor.fetchall():
            # print(row)
            items.append({
                u'id': row[0],
                u'description': row[1],
                u'genre': row[2],
                u'artiste': row[3],
                u'punchline': row[4]
            })
        con.commit()
        print items
        one = random.choice(items)['artiste']
    except BaseException, e:
        logging.error(u'Error: {}'.format(e))
    
    print "response: {}".format(one)

    return one



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

