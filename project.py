import csv

class Library:
    def __init__(self, path):
        self.path = path
        self.books = self.load_books()

    def load_books(self):
        books = []
        with open(self.path, 'r') as data:
            reader = csv.DictReader(data)
            for row in reader:
                books.append(row)
        return books

    def save_books(self):
        with open(self.path, 'w', newline='') as data:
            colnames = ['bid', 'title', 'author', 'category', 'status']
            writer = csv.DictWriter(data, fieldnames=colnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow(book)

    def add_book(self, bid, title, author, category, status='Available'):
        for book in self.books:
            if book['title'].lower() == title.lower() and book['author'].lower() == author.lower():
                print(f'Book {title} by {author} already exists in the library')
                return
        new_book = {
            'bid': bid,
            'title': title,
            'author': author,
            'category': category,
            'status': status
        }
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' added successfully.")

    def search_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                return book
        return None

    def remove_book(self, title):
        book = self.search_book(title)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Book '{title}' has been removed from the library.")
        else:
            print(f"Book '{title}' is not available in the library.")

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book['status'].lower() == 'available':
                book['status'] = 'Issued'
                self.save_books()
                print(f"Book '{title}' has been issued.")
            else:
                print(f"Book '{title}' is currently not available.")
        else:
            print(f"Book '{title}' is not available in the library.")

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            if book['status'].lower() == 'issued':
                book['status'] = 'Available'
                self.save_books()
                print(f"Book '{title}' has been returned and is now available.")
            else:
                print(f"Book '{title}' is already available.")
        else:
            print(f"Book '{title}' is not available in the library.")

    def display_books(self):
        print("Current list of books in the library:")
        for book in self.books:
            print(f"ID: {book['bid']}, Title: {book['title']}, Author: {book['author']}, "
                  f"Category: {book['category']}, Status: {book['status']}")

    def search_and_display_book(self, title):
        book = self.search_book(title)
        if book:
            print(f"Book found:\nID: {book['bid']}, Title: {book['title']}, Author: {book['author']}, "
                  f"Category: {book['category']}, Status: {book['status']}")
        else:
            print(f"Book '{title}' is not available in the library.")

def main():
    library = Library(r"C:\Users\USER\Downloads\Books_data - Sheet1.csv")

    options = {
        '1': library.add_book,
        '2': library.borrow_book,
        '3': library.return_book,
        '4': library.display_books,
        '5': library.search_and_display_book,
        '6': library.remove_book,
        '7': exit
    }

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Search Book")
        print("6. Remove Book")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bid = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            category = input("Enter book category: ")
            options[choice](bid, title, author, category)
        elif choice in ['2', '3', '5', '6']:
            title = input("Enter book title: ")
            options[choice](title)
        elif choice in options:
            options[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

