class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '7_*$&\x18\xdc\x8be1\x1b\xeaQHD\x89\xfd\xbc\xb2\x9c\xf6\x075d'
    ADMINS = ['pbeeson@thevariable.com']
    MAIL_SERVER = 'smtp.webfaction.com'
    MAIL_USERNAME = 'thevariable'
    MAIL_PASSWORD = 'V@r1able'
    MAIL_PORT = 465
    MAIL_USE_SSL = True


class ProductionConfig(Config):
    DEBUG = False
    TWILIO_ACCOUNT = 'ACb01b4d6edfb1b41a8b80f5fed2c19d1a'
    TWILIO_TOKEN = '97e6b9c0074b2761eff1375fb088adda'
    SITE_URL = 'http://textme.thevariable.com/'
    STATIC_PATH = '/home/thevariable/webapps/text_me/text_me/app/'


class DevelopmentConfig(Config):
    DEBUG = True
    TWILIO_ACCOUNT = 'ACb01b4d6edfb1b41a8b80f5fed2c19d1a'
    TWILIO_TOKEN = '97e6b9c0074b2761eff1375fb088adda'
    SITE_URL = 'http://dev.thevariable.com/'
    STATIC_PATH = '/Users/pbeeson/sites/textme/app/'
    TESTING = True
