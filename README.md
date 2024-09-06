 Library-management-system
Library Management System 📚  A simple and efficient Library Management System built with Python and CSV for managing books in a library. This project allows users to add, borrow, return, search, and display books easily through a text-based interface.
 Library Management System

This is a simple Library Management System implemented in Python using the `csv` module. The program allows users to manage books, including adding, removing, borrowing, returning, searching, and displaying books.

 Features

- **Add Book**: Adds a new book to the library.
- **Borrow Book**: Issues a book to a user, marking it as "Issued".
- **Return Book**: Returns a borrowed book, marking it as "Available".
- **Display Books**: Displays all books currently in the library.
- **Search Book**: Searches for a book by its title.
- **Remove Book**: Removes a book from the library.

File Structure

- `library_management.py`: The main Python script containing the `Library` class and the program logic.
- `Books_data.csv`: The CSV file used to store the books data.

How to Run

1. Clone the Repository**:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Prepare CSV File**:

   Make sure the CSV file (`Books_data.csv`) is created and properly formatted. The file should have the following columns:
   - `bid` (Book ID)
   - `title` (Book Title)
   - `author` (Author Name)
   - `category` (Category of the Book)
   - `status` (Availability Status)

3. Run the Program**:

    ```bash
    python library_management.py
    ```

4. Use the Application**:

   Follow the on-screen prompts to add, remove, borrow, return, or search for books.

Example CSV File

```csv
bid,title,author,category,status
1,The Great Gatsby,F. Scott Fitzgerald,Fiction,Available
2,To Kill a Mockingbird,Harper Lee,Fiction,Available
3,1984,George Orwell,Science Fiction,Issued
4,The Catcher in the Rye,J.D. Salinger,Fiction,Available
