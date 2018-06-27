# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
import logging
SECRET_KEY = "*qzC!')@=7#7td`nDc6Nw9%["

FB_APP_ID = 318494538688205

CONFIG_DB = {
    u"db": {
        u"user": u"root",
        u"host" : u"127.0.0.1",
        u"password": u"localroot1234",
        u"database": u"web_app_fb",
        u"charset": u"utf-8"
    },
    u"logging": {
        u"level": logging.INFO,
        u"pattern": u'%(levelname)s - %(asctime)s : %(message)s',
        u"pattern_debug": u'[%(filename)15s::%(funcName)15s]-[l.%(lineno)3s] %(message)s'
    },
    u"app": {
        u"env": u"dev",
        u"debug": True
    }
}