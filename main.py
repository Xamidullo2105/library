from apps.auth.views import register, login, logout
from apps.books import admin_views
from apps.books import user_views
from apps.books import user_views


def auth_menu():
    print("""
    1. Register
    2. Login
    3. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        if register():
            print("Successfully registered")
        else:
            print("Something went wrong")
    elif choice == "2":
        result = login()
        if result == "admin":
            print("Welcome my owner")
            return admin_menu()
        elif result == "user":
            return user_menu()
        else:
            return login()
    elif choice == "3":
        print("Good bye")
        return None
    else:
        print("Invalid choice")
    return auth_menu()


def admin_menu():
    print("""
    1. Add book
    2. Delete book
    3. Rent a book
    4. Return the book
    5. Show all rented books
    6. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        admin_views.add_book()
    elif choice == "2":
        admin_views.delete_book()
    elif choice == "3":
        admin_views.rent_book()
    elif choice == "4":
        admin_views.return_book()
    elif choice == "5":
        admin_views.show_all_rented_books()
    elif choice == "6":
        logout()
        return auth_menu()
    else:
        print("Invalid choice")
    return admin_menu()


def user_menu():
    print("""
    1. Show my rented books
    2. Show all books
    3. Logout
    """)
    choice = input("Choice: ")
    if choice == "1":
        user_views.show_user_rented_books()
    elif choice == "2":
        user_views.show_all_books()
    elif choice == "3":
        print("Good bye")
        return None
    else:
        logout()
        return auth_menu()

    return user_menu()


if __name__ == '__main__':
    logout()
    auth_menu()
