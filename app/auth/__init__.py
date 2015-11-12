"""
This package holds app routes related to authentication.
"""

from flask import Blueprint

auth = Blueprint('auth',__name__)

from . import views     # this comes last to avoid circular dependencies

                                