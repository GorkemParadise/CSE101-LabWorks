# SORU 1
class Book:
    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title.strip()
        self.author = author.strip()

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book1 = Book(title="2025", author="ayarlicazhocam")
book2 = Book(title="1984", author=" George Orwell ")
print(book1)
print(book2)
#Book(title='2025', author='ayarlicazhocam')
#Book(title='1984', author='George Orwell')


# SORU 2
class Book2:
    total_created = 0

    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title.strip()
        self.author = author.strip()
        Book2.total_created += 1

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
kitap1 = Book2(title="NE DIYON", author="ALİ BAYRAM")
kitap2 = Book2(title="Yeditepe", author="GÖRKEM")
kitap3 = Book2(title="UHAKSBKHJAW", author="MEHMET")
print(f"Total books created: {Book2.total_created}")
#Total books created: 3


# SORU 3
def save_books(books, filepath):
    with open(filepath, 'w') as file:
        for book in books:
            file.write(f"{book.title},{book.author}\n")
def load_books(filepath):
    books = []
    with open(filepath, 'r') as file:
        for line in file:
            title, author = line.strip().split(',')
            books.append(Book(title, author))
    return books
books_to_save = [book1, book2, kitap1, kitap2, kitap3]
save_books(books_to_save, 'books.txt')
loaded_books = load_books('books.txt')
for book in loaded_books:
    print(book)
#Book(title='2025', author='ayarlicazhocam')
#Book(title='1984', author='George Orwell')
#Book(title='NE DIYON', author='ALİ BAYRAM')
#Book(title='Yeditepe', author='GÖRKEM')
#Book(title='UHAKSBKHJAW', author='MEHMET')


# SORU 4
import json
def export_books_to_json(books, filepath):
    with open(filepath, 'w') as file:
        json_books = [{"title": book.title, "author": book.author} for book in books]
        json.dump(json_books, file)
def import_books_from_json(filepath):
    books = []
    with open(filepath, 'r') as file:
        try:
            json_books = json.load(file)
            for entry in json_books:
                if 'title' in entry and 'author' in entry:
                    books.append(Book(entry['title'], entry['author']))
                else:
                    print(f"Warning: {entry}")
        except json.JSONDecodeError as e:
            print(f"Error reading JSON: {e}")
    return books
books_for_json = [book1, book2, kitap1]
export_books_to_json(books_for_json, 'books.json')
imported_books = import_books_from_json('books.json')
for book in imported_books:
    print(book)
#Book(title='2025', author='ayarlicazhocam')
#Book(title='1984', author='George Orwell')
#Book(title='NE DIYON', author='ALİ BAYRAM')


# SORU 5
import requests
def fetch_sample_todo():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        todo = response.json()
        print(f"TODO {todo['id']}: {todo['title']} (completed={todo['completed']})")
        return todo
    except requests.RequestException as e: #EXCEPT KISMINA İNTERNETTEN BAKILDI, ANLAYAMADIM
        print(f"Network error: {e}")
        return None
fetch_sample_todo()
#TODO 1: delectus aut autem (completed=False)
#{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}



# SORU 6
def main():
    book_a = Book(title="DENEMNE 1", author="TBHKW")
    book_b = Book(title="To Kill", author="dsd sde")
    
    books = [book_a, book_b]
    
    save_books(books, 'books.txt')
    loaded_books_txt = load_books('books.txt')
    print("Books loaded from text:")
    for book in loaded_books_txt:
        print(book)
    
    export_books_to_json(books, 'books.json')
    loaded_books_json = import_books_from_json('books.json')
    print("Books loaded from JSON:")
    for book in loaded_books_json:
        print(book)
    
    print("TODO:")
    fetch_sample_todo()

if __name__ == "__main__":
    main()
#Books loaded from text:
#Book(title='DENEMNE 1', author='TBHKW')
#Book(title='To Kill', author='dsd sde')
#Books loaded from JSON:
#Book(title='DENEMNE 1', author='TBHKW')
#Book(title='To Kill', author='dsd sde')
#TODO:
#TODO 1: delectus aut autem (completed=False)