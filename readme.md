#Flaskula

[![build status](https://travis-ci.org/joeclark-phd/flaskula.svg?branch=master)](https://travis-ci.org/joeclark-phd/flaskula)

This is an app that I have created by following the tutorial in Miguel 
Grinberg's "Flask Web Development" book.  It has been modified to work on 
Heroku and to send e-mail via the [Postmark](https://postmarkapp.com) add-on 
instead of SMTP.  Also to run on my (Windows 7) personal computer.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Tag "ch7" is the version you need if you want to jump into Part II of the
book.  It may be a useful starter template for other Flask applications to
be deployed on Heroku, too.

Tag "v1.0" is up to date with the end of the book. A few innovations of my own are the
one-step "Deploy to Heroku" button abd set-up for continuous integration with TravisCI.

## Requirements

Python 3 seems to be necessary for database *write* on Heroku.  Everything else
including database *read* seems to work with Python 2 as well.  YMMV.

Python dependencies are stored in `requirements.txt`.  I advise you to use a 
Python virtual environment. You can install all the dependencies in one step 
like so:

    (venv) $ pip install -r requirements.txt

## How to get it going: 

###Easy mode:

1. Click this: 
    
    [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
   
###To set it up manually on Heroku:

1. Create a Heroku account, download the toolbelt, etc.
2. `git clone`, make any changes, `git commit`
3. `heroku create`
4. In Heroku, provision a PostgreSQL database and the 
     [Postmark](https://postmarkapp.com) add-on.
5. Make sure the necessary environment variables are set:
  - `SECRET_KEY`
  - `DATABASE_URL`: Heroku provides this for its PostgreSQL add-on 
    automatically; if not found (i.e. on your development machine) the app 
    will just use a SQLite database, and that's fine.
  - `FLASK_CONFIG=heroku` (for Heroku) or `=development` for localhost
  - `FLASKULA_ADMIN`: email address to send log messages to
  - `POSTMARK_API_KEY`: automatically provided by Heroku when you add-on 
    Postmark
  - `PYSTMARK_DEFAULT_SENDER`: default e-mail sender called by the 
    [Flask-Pystmark](https://github.com/xsleonard/flask-pystmark) library 
    (yes, that's a "y")
6. `git push heroku master`
7. `heroku run python manage.py deploy` -- this should create the database
    tables.
    
If you get into trouble upgrading the database, go into Postgres and drop
all tables, *especially* the table called `alembic_version`, and issue the
deploy command again.  That re-creates the database from scratch (all
migrations, not just the one you just did).
    
###To make it work on my Windows development machine:

1. Set environment variables accordingly (one way to do this is to modify
    your virtual environment's "activate" script.
  - all environment variables listed above, plus:
  - `SSL_DISABLE=1` for non-Heroku environments    
2. `python manage.py deploy` (only the first time)
3. `python manage.py runserver`

###To *simulate Heroku* on my Windows machine:

I don't recommend this because you don't get error messages that are quite as
helpful.  But this is possible.

1. Set environment variables in a `.env` file. (`.gitignore` keeps it private)
2. `heroku local run python manage.py deploy`
3. `heroku local -f Procfile.windows`


##To test

    python manage.py test
    
    