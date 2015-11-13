"""
This file holds multiple configuration sets for the app.
Which one gets used will depend on the environment; in this way
we can use the same code without modification in each place.

What's left up to environment variables?
MAIL_USERNAME
MAIL_PASSWORD
SECRET_KEY
DATABASE_URL
DEV_DATABASE_URL
TEST_DATABASE_URL
FLASK_CONFIG (called by manage.py, tells the app which config to use)
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'something they wont guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # This is deprecated, but I don't
                                            # know if turning it off will break
                                            # anything. Let's see.
    PYSTMARK_API_KEY = os.environ.get('POSTMARK_API_KEY')
    PYSTMARK_DEFAULT_SENDER = os.environ.get('PYSTMARK_DEFAULT_SENDER')
    FLASKULA_MAIL_SUBJECT_PREFIX = '[Flaskula]'
    FLASKULA_ADMIN = os.environ.get('FLASKULA_ADMIN')
    FLASKULA_POSTS_PER_PAGE = 20
    FLASKULA_FOLLOWERS_PER_PAGE = 20
    SSL_DISABLE = True # for all except Heroku
    
    @staticmethod
    def init_app(app):
        pass
        

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # necessary, I think, for
                                           # auto-generating db migrations
                                           
    #DEBUG = True #This setting breaks the application on my windows box
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
        
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
        
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class HerokuConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE')) # on heroku, use SSL

        
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig    # default
}
    