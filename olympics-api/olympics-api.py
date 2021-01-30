# Aishwarya Varma and Luisa Escosteguy
# January 30, 2021

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
    ''' Returns a JSON list of games dictionaries with keys of id, year, season, city. '''
    query = '''SELECT competition_id, year, city, season
                FROM competition
                ORDER BY year;'''
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    games_dictionary = []
    for row in cursor:
        id, year, season, city = row
        games_dictionary.append({'id': id, 'year': year, 'season': season, 'city': city})

    return json.dumps(games_dictionary)


@app.route('/nocs')
def get_nocs():
    ''' Returns JSON list of nocs dictionaries with keys of the noc abbreviation and corresponding region. '''
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
        name, abbreviation = row
        nocs_dictionary.append({'abbreviation': abbreviation, 'name': name})

    return json.dumps(nocs_dictionary)

@app.route('/medalists/games/<games_id>')
def get_medalists_by_games(games_id):
    ''' Returns JSON list of dictionaries where each represents an athlete who earned medal in specified games. '''
    noc = flask.request.args.get('noc', type=str)
    
    noc_query = ''
    if noc:
        noc_query = "AND athlete_competition.committee_id = committee.committee_id AND committee.abbreviation = '{}'".format(noc)
   
    query = '''SELECT DISTINCT athlete.athlete_id, athlete.athlete_name, athlete.sex, event.sport, event.event_name, athlete_competition_event.medal
                FROM athlete, athlete_competition_event, event, athlete_competition, committee
                WHERE athlete.athlete_id = athlete_competition.athlete_id
                AND athlete_competition.athlete_competition_id = athlete_competition_event.athlete_competition_id
                AND athlete_competition_event.event_id = event.event_id
                AND athlete_competition_event.medal IS NOT NULL
                {}
                AND athlete_competition.competition_id = %s;'''.format(noc_query)
    try:
        cursor.execute(query, (int(games_id),))
    except Exception as e:
        print(e)
        exit()

    medalists_by_games_dictionary = []
    for row in cursor:
        athlete_id, athlete_name, athlete_sex, sport, event, medal = row
        medalists_by_games_dictionary.append({'athlete_id': athlete_id, 'athlete_name': athlete_name, 'athlete_sex': athlete_sex, 'sport': sport, 'event': event, 'medal': medal})
    return json.dumps(medalists_by_games_dictionary)

def connect_database():
    '''Connects to the olympic database'''
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
