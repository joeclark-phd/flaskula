from threading import Thread
from flask import current_app, render_template
from flask.ext.pystmark import Message
from . import pystmark


def send_async_email(app, msg):
    with app.app_context():
        pystmark.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(to=to,
                  subject=app.config['FLASKULA_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  html = render_template(template + '.html', **kwargs),
                  text = render_template(template + '.txt', **kwargs))
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
