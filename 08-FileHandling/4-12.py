import csv

def read_books(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def filter_books_by_genre(books, genre):
    return [book for book in books if book['Genre'] == genre]

def save_books_to_file(books, file_name):
    with open(file_name, 'w') as file:
        for book in books:
            file.write(f"{book['Title']},{book['Author']},{book['Year']}\n")

def process_books():
    books = read_books('books.csv')
    genres_to_files = {
        "Fantasy": "books_fantasy.txt",
        "Historical": "books_historical.txt",
        "Romance": "books_romance.txt",
        "Classic": "books_classic.txt"
    }
    for genre, file_name in genres_to_files.items():
        filtered_books = filter_books_by_genre(books, genre)
        save_books_to_file(filtered_books, file_name)

process_books()
