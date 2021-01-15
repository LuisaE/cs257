#Claire Williams and Luisa Escosteguy

import argparse
import csv

books = []

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='Process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book', '-b', nargs=1, metavar='S', help='print a list of books whose titles contain the string S')
	parser.add_argument('--author', '-a', nargs=1, metavar='S', help='print a list of authors whose names contain the string S')
	parser.add_argument('--publication','-p', nargs=2, metavar='year', help='print a list of books published between the two years')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

def search_books_by_title(arg):
	global books
	new_books = []
	S = arg[0].lower()

	for book in books: 
		if book[0].lower().count(S) > 0:
			new_books.append(book)
	
	books = new_books

def search_books_by_author(arg):
	global books
	new_books = []
	S = arg[0].lower()

	for book in books:
		if book[2].lower().count(S) > 0:
			new_books.append(book)

	books = new_books

def search_books_by_publication(args):
	global books
	new_books = []
	year_start, year_end = args
	year_start = int(year_start)
	year_end = int(year_end)

	if year_start > year_end:
		temp = year_start
		year_start = year_end
		year_end = temp

	for book in books:
		year_of_publication = int(book[1])
		if year_of_publication >= year_start and year_of_publication <= year_end:
			new_books.append(book)

	books = new_books

def print_books():
	global books
	if not books:
		print("We are sorry. We cannot find any results that match your search criteria.")
		exit()

	dash = '-' * 80
	print(dash)
	print('{:<44s}{:>6s}{:>30s}'.format('Book', 'Year', 'Author'))
	print(dash)
	for i in range(len(books)):
		book_name, year, author = books[i]
		print('{:<44s}{:^6s}{:>30s}'.format(book_name, year, author))

def main():
	global books
	arguments = get_parsed_arguments()
	books = csv.reader(open('books.csv', "r"), delimiter=",")

	if arguments:
		if arguments.book:
			search_books_by_title(arguments.book)
		if arguments.author:
			search_books_by_author(arguments.author)
		if arguments.publication:
			if arguments.publication[0].isnumeric() and arguments.publication[1].isnumeric():
				search_books_by_publication(arguments.publication)
			else:
				print("Please type numbers only")
				exit()
				
	if not (arguments.book or arguments.author or arguments.publication):
		print("Please add a flag to search for books")
		print("For additional information, enter python3 books.py --help")
		exit()
	
	print_books()

if __name__ == '__main__':
	main()
