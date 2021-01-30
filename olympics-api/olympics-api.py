#Aishwarya Varma and Luisa Escosteguy
#January 30, 2021

import sys
import argparse
import flask
import json

app = flask.Flask(__name__)

@app.route('/games')
def get_games():
    ''' Comment '''
    return 'Games'

@app.route('/nocs')
def get_nocs():
    ''' Comment '''
    return 'Nocs'

@app.route('/medalists/games/<games_id>')
def get_medalists_by_games(games_id):
    ''' Comment '''
    return 'Medalists games';

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Olympics Flask application API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
