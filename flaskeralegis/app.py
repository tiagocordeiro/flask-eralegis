from flask import Flask
from eralegis import thelemicdate


def create_app():
    application = Flask(__name__)

    @application.route('/')
    def index():
        today = thelemicdate.now()
        return today

    return application
