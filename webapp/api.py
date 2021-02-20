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
            {'name':'Aleph', 'birth_year':1984, 'death_year':2002, 'description':'sweet and cranky'},
            {'name':'Curby', 'birth_year':1999, 'death_year':2000, 'description':'gone too soon'},
            {'name':'Digby', 'birth_year':2000, 'death_year':2018, 'description':'the epitome of Cat'},
            {'name':'Max', 'birth_year':1998, 'death_year':2009, 'description':'seismic'},
            {'name':'Scout', 'birth_year':2007, 'death_year':None, 'description':'accident-prone'}]
    return json.dumps(games)
