"""
This __init__.py sets up the 'main' subfolder as a "Blueprint" package to
hold the app.routes and custom error messages for the app.
"""

from flask import Blueprint

main = Blueprint('main',__name__)

from . import views, errors     # this comes last to avoid circular
                                # dependencies, since views.py and errors.py
                                # will import 'main'
                                