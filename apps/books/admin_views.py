from core.utils import get_next_id
from core.file_manager import append, read, writerows
from datetime import datetime


def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book : ")
    pages = input("Enter the book pages: ")
    quantity = input("Enter the book quantity: ")
    
    books_id = get_next_id(filename="books")
    append(filename="books", data=[books_id, title, author ,pages, quantity])
    print("The book was added successfully ✅")


def delete_book():
    book_id = input("Enter the book id: ")
    books = read(filename="books")
    
    new_book = []
    for row in books:
        if row[0] != book_id:
            new_book.append(row)
    books = new_book
    writerows(filename="books", data=books)
    print("Subscription successfully canceled ✅")


def rent_book():
    email = input("Enter your email: ")
    users = read(filename="users")
    is_found = False
    for user in users:
        if user[2] == email:
            is_found = True
            break
    
    if is_found:
        book_id = input("Enter the book id: ")
        books = read(filename="books")
        for index, book in enumerate(books):
            if book[0] == book_id and int(book[4]) > 0:
                books[index][4] = str(int(book[4]) - 1)
                writerows(filename="books", data=books)
                
                next_id = get_next_id(filename="rents")
                status = "ijaraga berildi"
                data = [next_id, book_id, email, datetime.now(), status]
                append(filename="rents", data=data)
                print("Book is rented ✅")
                return
            
        print("Book not found ❌")
    
    else:
        print("User not found, please register first")


def return_book():
    rent_id = input("Enter the rent ID: ")
    rents = read(filename="rents")
    updated = False

    for rent in rents:
        if rent[0] == rent_id and rent[-1] != "Qaytarib olindi":
            rent[-1] = "Qaytarib olindi"
            updated = True

            books = read(filename="books")
            for book in books:
                if book[0] == rent[1]:
                    book[4] = str(int(book[4]) + 1)
                    break
            writerows("books", books)
            break

    if updated:
        writerows("rents", rents)
        print("The book was successfully returned ✅")
    else:
        print("No valid rent found for this ID or already returned ❌")


def show_all_rented_books():
    
    rents = read(filename="rents")
    
    for rent in rents:
        print(f"User id: {rent[0]} Book id: {rent[1]} Email: {rent[2]} Date: {rent[3]} Status: {rent[4]}")


def logout():
    users = read(filename="users")
    for index, user in enumerate(users):
        users[index][-2] = "False"  
    writerows(filename="users", data=users)