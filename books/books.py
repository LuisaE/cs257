#Claire Williams and Luisa Escosteguy

import argparse
import csv
import sys

books = []

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='Process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book', '-b', nargs=1, metavar='S', help='print a list of books whose titles contain the string S')
	parser.add_argument('--author', '-a', nargs=1, metavar='S', help='print a list of authors whose names contain the string S')
	parser.add_argument('--publication','-p', nargs=2, type=int, metavar='year', help='print a list of books published between the two years')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

def filter_books_by_title(title):
	global books
	new_books = []
	S = title[0].lower()

	for book in books: 
		if book[0].lower().count(S) > 0:
			new_books.append(book)
	
	books = new_books

def filter_books_by_author(author):
	global books
	new_books = []
	S = author[0].lower()

	for book in books:
		if book[2].lower().count(S) > 0:
			new_books.append(book)

	books = new_books

def filter_books_by_publication(years):
	global books
	new_books = []
	
	year_start = min(years)
	year_end = max(years)

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
	books = csv.reader(open("books.csv", "r"), delimiter=",")

	if arguments:
		if arguments.book:
			filter_books_by_title(arguments.book)
		if arguments.author:
			filter_books_by_author(arguments.author)
		if arguments.publication:
			filter_books_by_publication(arguments.publication)
				
	if not (arguments.book or arguments.author or arguments.publication):
		print("Please add a flag to search for books")
		print("For additional information, enter python3 books.py --help")
		exit()
	
	print_books()

if __name__ == '__main__':
	main()
