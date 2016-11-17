
import logging
from flask import Flask,request
from google.appengine.api import users


app = Flask(__name__)


@app.route('/')
def user_login():
    return 'Welcome! <a href={}>Sign in or register</a>.'.format(users.create_login_url(request.path))


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
