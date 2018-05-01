from flask import Flask, jsonify
from eralegis import thelemicdate


def create_app():
    application = Flask(__name__)

    @application.route('/')
    def index():
        today = thelemicdate.now()
        return today

    @application.route('/api/')
    def api():
        today = thelemicdate.now()
        response = jsonify(data=today)
        response.headers.add("Access-Control-Allow-Origin", '*')
        return response

    return application
