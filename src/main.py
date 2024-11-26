from library import Library


def menu(**kwargs) -> None:

    """
    Display the menu options to the user.

    This function shows the available actions that the user can take in the library console program.

    :param kwargs: Optional keyword arguments that can include:
        - ver: Version of the menu to display (None for main menu, 0 for removal menu, 1 for back navigation).
        - context_error: An optional error message to display.
    """

    print("\n--------------------------------------------------------")
    if kwargs.get('ver') is None:
        print(kwargs.get('context_error')) if kwargs.get('context_error') is not None else None
        print("\n1. Добавить книгу.")
        print("2. Удалить книгу.")
        print("3. Найти книгу.")
        print("4. Отобразить все книги.")
        print("5. Изменить статус книги.")
        print("0. Выход.\n")
    if kwargs.get('ver') == 0:
        print("0. Вернуться в главное меню.\n")
    if kwargs.get('ver') == 1:
        print("0. Вернуться в главное меню.")
        print("-1. Вернуться назад.\n")


def main() -> None:

    """
    Display the menu options to the user.

    This function shows the available actions that the user can take in the library console program.

    """

    library = Library('library.json')  # Initializing the library with the specified JSON file
    menu()  # Display the main menu

    while True:
        option: str = input("Выберите действие: ")  # Get user input for menu option

        match option:
            case '1':
                context_error = library.add_book()  # Add a book and get answer about mistake or successful
                menu(context_error=context_error)  # Display the menu with get answer about mistake or successful
                continue
            case '2':
                menu(ver=0)  # Show menu for removing a book
                book_id = input("Введите ID книги для удаления: ").strip()  # Get book ID from user
                if book_id == "0":
                    menu()   # Return to the main menu
                    continue
                context_error = library.remove_book(book_id)  # Removing the book
                if context_error == "0":
                    menu()  # Return to the main menu
                    continue
                menu(context_error=context_error)  # Display the menu with get answer about mistake or successful
                continue
            case '3':
                menu(ver=0)  # Show menu for finding a book
                query: str = input("Введите название, автора или год для поиска: ").strip()  # Get search query
                if query == "0":
                    menu()  # Return to the main menu
                    continue
                context_error = library.find_books(query)  # Find books and get answer about mistake or successful
                menu(context_error=context_error)  # Display the menu with get answer about mistake or successful
                continue
            case '4':
                context_error = library.display_books()  # Find all books and get answer about mistake or successful
                menu(context_error=context_error)  # Display the menu with get answer about mistake or successful
                continue
            case '5':
                context_error = library.change_status()  # Change the status of a book
                menu(context_error=context_error)  # Display the menu with get answer about mistake or successful
                continue
            case '0':
                break  # Exit the loop and end the program
            case _:
                menu(context_error="Неправильный статус! Напишите цифру из списка!")  # Handle invalid input


if __name__ == "__main__":
    main()  # Run the main function
