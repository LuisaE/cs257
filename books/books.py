#Claire Williams and Luisa Escosteguy

import argparse
import csv

books = list()

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='Process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book-search', '-b', nargs=1, metavar='S', help='print a list of books whose titles contain the string S')
	parser.add_argument('--author-search', '-a', nargs=1, metavar='S', help='print a list of authors whose names contain the string S')
	parser.add_argument('--publication','-p', nargs=2, metavar='year', help='print a list of books published between the two years')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

def publication(args):
	year_start, year_end = args
	year_start = int(year_start)
	year_end = int(year_end)

	#make sure the years are in the correct order
	if year_start > year_end:
		temp = year_start
		year_start = year_end
		year_end = temp

	#find the books not published between year_start and year_end and remove from list
	for book in books:
		year_of_publication = int(book[1])
		if year_of_publication < year_start or year_of_publication > year_end:
			books.remove(book)

def get_data():
	data = csv.reader(open('books.csv', "r"), delimiter=",")
	#adds the data to a python list so we can remove rows that we want to filter out
	for row in data:
		books.append(row)

def main():
	arguments = get_parsed_arguments()
	get_data()

	if arguments:
		if arguments.publication:
			publication(arguments.publication)
	
	#create function that prints what is left in books. How to print nicely?

if __name__ == '__main__':
    main()