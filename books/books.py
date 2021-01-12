#Claire Williams and Luisa Escosteguy
#test comment
import argparse
import csv

def get_parsed_arguments():
	parser = argparse.ArgumentParser(description='Process books.csv using a keyword from the title, an author, or a range of publication')
	parser.add_argument('--book', '-b', nargs=1, metavar='S', help='print a list of books whose titles contain the string S')
	parser.add_argument('--author', '-a', nargs=1, metavar='S', help='print a list of authors whose names contain the string S')
	parser.add_argument('--publication','-p', nargs=2, metavar='year', help='print a list of books published between the two years')
	parsed_arguments = parser.parse_args()
	return parsed_arguments

def book(arg, books):
	new_books = []
	S = arg[0].lower()

	for book in books: 
		if book[0].lower().count(S) > 0:
			new_books.append(book)
	
	return new_books

def author(arg, books):
	new_books = []
	S = arg[0].lower()

	for book in books:
		if book[2].lower().count(S) > 0:
			new_books.append(book)

	return new_books

def publication(args, books):
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

	return new_books

def print_books(books):
	if not books:
		print("We are sorry. We cannot find any results that match your search criteria.")
		exit()
	
	for book in books:
		print('\t'.join(book))

def main():
	arguments = get_parsed_arguments()
	books = csv.reader(open('books.csv', "r"), delimiter=",")

	if arguments:
		if arguments.book:
			books = book(arguments.book, books)
		if arguments.author:
			books = author(arguments.author, books)
		if arguments.publication:
			if arguments.publication[0].isnumeric() and arguments.publication[1].isnumeric():
				books = publication(arguments.publication, books)
			else:
				print("Please, type numbers only")
				exit()
	
	print_books(books)

if __name__ == '__main__':
	main()
