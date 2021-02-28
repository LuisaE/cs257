# Claire Williams and Luisa Escosteguy

import sys
import flask
import json
import psycopg2

from config import password
from config import database
from config import user

api = flask.Blueprint('api', __name__)

@api.route('/games/') 
def get_games():
    query = '''SELECT DISTINCT games.name, games.year, publishers.publisher, genres.genre, platforms.platform, sales.global_sales
                FROM games, publishers, genres, games_platforms, platforms, sales
                WHERE games.publisher_id = publishers.id
                AND games.genre_id = genres.id
                AND games.id = games_platforms.games_id
                AND games_platforms.platforms_id = platforms.id
                AND games_platforms.sales_id = sales.id
                ORDER BY sales.global_sales DESC
                LIMIT 400;'''
    try:
        cursor = connect_database()
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    games_dictionary = []
    for row in cursor:
        name, year, publisher, genre, platform, sales = row
        sales = str(sales)
        games_dictionary.append({'name': name, 'year': year, 'publisher': publisher, 'genre': genre, 'platform': platform, "sales": sales })

    return json.dumps(games_dictionary)

@api.route('/platforms/') 
def get_platforms():
    query = '''SELECT DISTINCT platform
                FROM platforms
                ORDER BY platform'''
    try:
        cursor = connect_database()
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    platforms_list = []
    for platform in cursor:
        platforms_list.append(platform[0])

    return json.dumps(platforms_list)

@api.route('/genres/') 
def get_genres():
    query = '''SELECT DISTINCT genre
                FROM genres
                WHERE genre IS NOT NULL
                ORDER BY genre;'''
    try:
        cursor = connect_database()
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    genre_list = []
    for genre in cursor:
        genre_list.append(genre[0])

    return json.dumps(genre_list)

@api.route('/publishers/') 
def get_publishers():
    query = '''SELECT DISTINCT publisher
                FROM publishers
                ORDER BY publisher
                LIMIT 300;'''
    try:
        cursor = connect_database()
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    publisher_list = []
    for publisher in cursor:
        publisher_list.append(publisher[0])

    return json.dumps(publisher_list)

@api.route('/help/') 
def get_help():
    content = ''
    with open('doc/api-design.txt', 'r') as f:
        line = f.readline()
        while line:
            content += line + '<br />'
            line = f.readline()
    return content

def connect_database():
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(e)
        exit()