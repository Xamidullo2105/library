from apps.auth.utils import get_active_user
from core.file_manager import read, writerows


def show_user_rented_books():
    user = get_active_user()
    
    books = read(filename="rents")
    rented_books_id = []
    
    for book in books:
        if book[2] == user[2]:
            rented_books_id.append(book[1])
    
    
    if rented_books_id:
        books = read(filename="books")
        for book in books:
            if book[0] in rented_books_id:
                print(f"ID: {book[0]} TITLE: {book[1]}")
    
    else:
        print("You don't have any books yet")


def show_all_books():
    books = read(filename="books")
    if books:
        for book in books:
            print(f"Book id: {book[0]} Title: {book[1]} Author: {book[2]} Page: {book[3]} Quantity: {book[4]}")
    else:
        print("No books")


def logout():
    users = read(filename="users")
    for index, user in enumerate(users):
        users[index][-2] = "False"  
    writerows(filename="users", data=users)
    