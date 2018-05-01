from flask import Flask, jsonify, render_template, url_for
from eralegis import thelemicdate
from flaskeralegis.docs import liber_al
import random


def create_app():
    application = Flask(__name__)

    @application.route('/')
    def index():
        today = thelemicdate.now()
        return render_template('index.html', datathelemica=today)

    @application.route('/api/')
    def api():
        today = thelemicdate.now()
        response = jsonify(data=today)
        response.headers.add("Access-Control-Allow-Origin", '*')
        return response

    @application.route('/liberal/')
    def liberal_quote():
        quote_file = liber_al
        lines = quote_file.split('\n\n')
        return random.choice(lines)

    return application
