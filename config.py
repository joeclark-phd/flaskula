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
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKULA_MAIL_SUBJECT_PREFIX = '[Flaskula]'
    FLASKULA_MAIL_SENDER = 'Flaskula Admin <flaskula@example.com>'
    FLASKULA_ADMIN = os.environ.get('FLASKULA_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
        

class DevelopmentConfig(Config):
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

        
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig    # default
}
    