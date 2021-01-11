#Claire Williams and Luisa Escosteguy

import argparse

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='Process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book-search', '-bs', nargs=1, metavar='S', help='print a list of books whose titles contain the string S')
	parser.add_argument('--author-search', '-as', nargs=1, metavar='S', help='print a list of authors whose names contain the string S')
	parser.add_argument('--publish','-p', nargs=2, metavar='year', help='print a list of books published between the two years')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

get_parsed_arguments()
