#Claire Williams and Luisa Escosteguy

import argparse

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book-search', '-bs', nargs=1, metavar='keyword', help='the keyword to search for in the book titles')
	parser.add_argument('--author-search', '-as', nargs=1, metavar='author', help='the author whose books to search for')
	parser.add_argument('--publish','-p', nargs=2, metavar='year', help='the range of years the books were published between')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

get_parsed_arguments()
