class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = ''
    ADMINS = ['']
    MAIL_SERVER = ''
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_PORT = 465
    MAIL_USE_SSL = True


class ProductionConfig(Config):
    DEBUG = False
    TWILIO_ACCOUNT = ''
    TWILIO_TOKEN = ''
    SITE_URL = ''
    STATIC_PATH = ''


class DevelopmentConfig(Config):
    DEBUG = True
    TWILIO_ACCOUNT = ''
    TWILIO_TOKEN = ''
    SITE_URL = ''
    STATIC_PATH = ''
    TESTING = True
