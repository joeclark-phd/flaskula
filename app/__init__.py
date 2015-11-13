"""
Application Factory:
This allows the dynamic creation of application objects with different 
configurations set at runtime, which is useful e.g. for unit testing. It 
loads several Flask extensions, too, keeping other files uncluttered.

As an __init__.py file, it makes the 'app' directory a Python "package".
"""

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
#from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pystmark import Pystmark
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown


from config import config

bootstrap = Bootstrap()
#mail = Mail()
moment = Moment()
db = SQLAlchemy()
pystmark = Pystmark()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
pagedown = PageDown()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)   # what does this line do?
    
    # when on Heroku, force SSL mode
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask.ext.sslify import SSLify
        sslify = SSLify(app)
    
    
    bootstrap.init_app(app)
    #mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pystmark = Pystmark(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    
    #attach main routes and error messages
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    #authentication-related routes
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    

    
    return app
