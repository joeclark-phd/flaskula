"""
Application Factory:
This allows the dynamic creation of application objects with different 
configurations set at runtime, which is useful e.g. for unit testing. It 
loads several Flask extensions, too, keeping other files uncluttered.

As an __init__.py file, it makes the 'app' directory a Python "package".
"""

from flask import Flask, render_template
#from flask.ext.bootstrap import Bootstrap
#from flask.ext.mail import Mail
#from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pystmark import Pystmark
from config import config

#bootstrap = Bootstrap()
#mail = Mail()
#moment = Moment()
db = SQLAlchemy()
pystmark = Pystmark()



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)   # what does this line do?
    
    # when on Heroku, force SSL mode
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)
    
    
    #bootstrap.init_app(app)
    #mail.init_app(app)
    #moment.init_app(app)
    db.init_app(app)
    pystmark = Pystmark(app)
    
    #attach routes and custom error messages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
