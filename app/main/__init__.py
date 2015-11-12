"""
This __init__.py sets up the 'main' subfolder as a "Blueprint" package to
hold the app.routes and custom error messages for the app.
"""

from flask import Blueprint

main = Blueprint('main',__name__)

from . import views, errors     # this comes last to avoid circular
                                # dependencies, since views.py and errors.py
                                # will import 'main'
                                

# This next bit makes the Permission object available to every template
# so that they don't need to import it.                                
from ..models import Permission
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
    