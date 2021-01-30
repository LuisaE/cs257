#Aishwarya Varma and Luisa Escosteguy
#January 30, 2021

import sys
import argparse
import flask
import json
import psycopg2

from config import password
from config import database
from config import user

app = flask.Flask(__name__)

@app.route('/games')
def get_games():
    ''' Comment '''
    return 'Games'

@app.route('/nocs')
def get_nocs():
    ''' Comment '''
    query = '''SELECT region, abbreviation
                FROM committee
                ORDER BY abbreviation;'''
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    nocs_dictionary = []
    for row in cursor:
        nocs_dictionary.append({row[1]: row[0]})

    return json.dumps(nocs_dictionary)

@app.route('/medalists/games/<games_id>')
def get_medalists_by_games(games_id):
    ''' Comment '''
    noc = flask.request.args.get('noc', default='USA', type=int)
    return 'Medalists games';

def connect_database():
    """
    Connects to the olympic database
    """
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        return cursor, connection
    except Exception as e:
        print(e)
        exit()

if __name__ == '__main__':
    cursor, connection = connect_database()

    parser = argparse.ArgumentParser('Olympics Flask application API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
