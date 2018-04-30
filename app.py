from flask import Flask
from eralegis import thelemicdate

def create_app():
    application = Flask(__name__)

    @application.route('/')
    def hello():
        hoje = thelemicdate.now()
        return hoje

    return application