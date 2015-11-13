"""
Call this script with 'runserver' to start the server, or 'shell'
to access a shell session in the app's context.  Chooses configuration
based on the FLASK_CONFIG environment variable.
"""
import os
from app import create_app, db
from app.models import User, Role, Post
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

def make_shell_context():
    return dict( app=app, db=db, User=User, Role=Role, Post=Post )
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


# a custom command to run the tests!
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    # migrate database to latest revision
    upgrade()
    # create user roles
    Role.insert_roles()
    # create self-follows for all users
    User.add_self_follows()    
    

if __name__ == "__main__":
    manager.run()
