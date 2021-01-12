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
        keyword = arg[0].lower()
        for book in books: 
                if book[0].lower().count(keyword) > 0:
                        new_books.append(book)
        return new_books

def author(arg, books):
        new_books = []
        name = arg[0].lower()
        for book in books:
                if book[2].lower().count(name) > 0:
                        new_books.append(book)
        return new_books

def publication(args, books):
        new_books = []
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
                if year_of_publication >= year_start and year_of_publication <= year_end:
                        new_books.append(book)
        return new_books

def get_data():
        books = []
        data = csv.reader(open('books.csv', "r"), delimiter=",")
        #adds the data to a python list so we can remove rows that we want to filter out
        for row in data:
                books.append(row)
        return books

#temporary print method for functionality, modify for formatting
def print_books(books):
        for book in books:
                print(book)

def main():
        arguments = get_parsed_arguments()
        books = get_data()

        if arguments:
                if arguments.book:
                        books = book(arguments.book, books)
                if arguments.author:
                        books = author(arguments.author, books)
                if arguments.publication:
                        books = publication(arguments.publication, books)
	
	#create function that prints what is left in books. How to print nicely?
        print_books(books)

if __name__ == '__main__':
        main()
