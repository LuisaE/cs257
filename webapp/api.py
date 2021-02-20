# Claire Williams and Luisa Escosteguy

import sys
import flask
import json
import config
import psycopg2

api = flask.Blueprint('api', __name__)

@api.route('/games/') 
def get_games():
    games = [{'name':'Emma', 'birth_year':1983, 'death_year':2003, 'description':'the boss'},
            {'name':'Aleph', 'birth_year':1984, 'death_year':2002, 'description':'sweet and cranky'},]
    return json.dumps(games)

@api.route('/platforms/') 
def get_platforms():
    platforms = [{'name':'Emma', 'birth_year':1983, 'death_year':2003, 'description':'the boss'},
            {'name':'Aleph', 'birth_year':1984, 'death_year':2002, 'description':'sweet and cranky'},]
    return json.dumps(platforms)