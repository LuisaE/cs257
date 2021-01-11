#Claire Williams and Luisa Escosteguy

import argparse
import csv

csv_file = csv.reader(open('books.csv', "r"), delimiter=",")

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='Process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book-search', '-bs', nargs=1, metavar='S', help='print a list of books whose titles contain the string S')
	parser.add_argument('--author-search', '-as', nargs=1, metavar='S', help='print a list of authors whose names contain the string S')
	parser.add_argument('--publish','-p', nargs=2, metavar='year', help='print a list of books published between the two years')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

def publish(args):
	year_start, year_end = args
	year_start = int(year_start)
	year_end = int(year_end)

	#make sure the years are in the correct order
	if year_start > year_end:
		temp = year_start
		year_start = year_end
		year_end = temp
	
	#find the books published between year_start and year_end
	for row in csv_file:
		name_of_book = row[0]
		year_of_publication = int(row[1])
		if year_of_publication >= year_start and year_of_publication <= year_end:
			print(name_of_book, "published in", year_of_publication)

def main():
	arguments = get_parsed_arguments()

	if arguments:
		if arguments.publish:
			publish(arguments.publish)

if __name__ == '__main__':
    main()