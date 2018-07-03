#coding: utf8
import random
import MySQLdb
import logging
from config import CONFIG_DB




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