from flask import Flask, jsonify, render_template
from eralegis import thelemicdate
import flaskeralegis.libri as libers
import random


def create_app():
    application = Flask(__name__)

    @application.route('/')
    def index():
        today = thelemicdate.now()
        random_al_capitulo = liberal_quote()[0]
        random_al_versiculo = liberal_quote()[1]
        return render_template('index.html', datathelemica=today,
                               al_cap=random_al_capitulo,
                               al_ver=random_al_versiculo)

    @application.route('/api/')
    def api():
        today = thelemicdate.now()
        response = jsonify(data=today)
        response.headers.add("Access-Control-Allow-Origin", '*')
        return response

    @application.route('/liberal/', methods=['GET', 'POST'])
    def liberal_api():
        response = jsonify(capitulo=liberal_quote()[0],
                           versiculo=liberal_quote()[1])
        response.headers.add("Access-Control-Allow-Origin", '*')
        return response

    def liberal_quote():
        liberal = {'LIBER AL I': libers.liber_al_c_i,
                   'LIBER AL II': libers.liber_al_c_ii,
                   'LIBER AL III': libers.liber_al_c_iii}
        capitulo_key = random.choice(list(liberal.keys()))
        capitulo_textos = liberal[capitulo_key].split('\n\n')
        versiculo = random.choice(capitulo_textos)
        return (capitulo_key, versiculo)


    return application
