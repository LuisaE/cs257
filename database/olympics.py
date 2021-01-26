# Luisa Escosteguy
# Jan 25, 2021
# A database-driven command-line application, using the olympics database

import argparse
import psycopg2
import sys

from config import password
from config import database
from config import user

def get_parsed_arguments():
    """
    Returns arguments from argparser. 
    """
    parser = argparse.ArgumentParser(description='Filter the olympics database using the commands below:')
    parser.add_argument('--athlete', '-a', nargs=1, metavar='noc', help='list the names of all the athletes from the specified NOC')
    parser.add_argument('--medal-noc', '-m', action='store_true', help='list all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals')
    parser.add_argument('--event','-s', nargs=1, metavar='sport', help='list all the events of a specific sport')
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def athletes_by_noc(noc, cursor):
    """
    Prints the names of all the athletes from a specified NOC
    """
    query = '''SELECT DISTINCT athlete.athlete_name 
                FROM athlete, committee, athlete_competition
                WHERE athlete.athlete_id = athlete_competition.athlete_id
                AND athlete_competition.committee_id = committee.committee_id
                AND committee.region = %s
                ORDER BY athlete.athlete_name;'''
    try:
        cursor.execute(query, (noc[0],))
    except Exception as e:
        print(e)
        exit()

    if cursor.rowcount == 0:
        print("We are sorry. We cannot find any results that match your search criteria.", file=sys.stderr)
        exit()

    print('===== Athletes from noc {0} ====='.format(noc[0]))
    for row in cursor:
        print(row[0])
    print()

def gold_medals_by_noc(cursor):
    """
    Prints all NOCs and the number of gold medals they have won, 
    in decreasing order of the number of gold medals
    """ 
    query = '''SELECT committee.region, COUNT(athlete_competition_event.medal)
                FROM committee, athlete_competition, athlete_competition_event
                WHERE committee.committee_id = athlete_competition.committee_id 
                AND athlete_competition.athlete_competition_id = athlete_competition_event.athlete_competition_id
                AND athlete_competition_event.medal = 'Gold'
                GROUP BY  committee.region
                ORDER BY COUNT(athlete_competition_event.medal) DESC;'''
    try:
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    print('===== NOCs and their number of gold medals {0} =====')
    for row in cursor:
        print(row[0], row[1])
    print()

def events_by_sport(sport, cursor):
    """
    Prints all the events of a specific sport
    """ 
    query = '''SELECT event_name 
                FROM event 
                WHERE sport = %s'''
    try:
        cursor.execute(query, (sport[0],))
    except Exception as e:
        print(e)
        exit()

    if cursor.rowcount == 0:
        print("We are sorry. We cannot find any results that match your search criteria.", file=sys.stderr)
        exit()

    print('===== Events from the sport {0} ====='.format(sport[0]))
    for row in cursor:
        print(row[0])
    print()

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

def main():
    argument = get_parsed_arguments()
    cursor, connection = connect_database()

    if argument:
        if argument.athlete:
            athletes_by_noc(argument.athlete, cursor)
        if argument.medal_noc:
            gold_medals_by_noc(cursor)
        if argument.event:
            events_by_sport(argument.event, cursor)
            
    connection.close()

if __name__ == '__main__':
    main()