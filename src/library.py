from book import Book
import os
import json


def context_menu_print(**kwargs) -> None:
    """
    Print the context menu with optional error messages.

    :param kwargs: Optional keyword arguments that can include:
    - ver: Version of the menu to display (None for main menu, 0 for removal menu, 1 for back navigation).
    - context_error: An optional error message to display.
    """

    print("\n--------------------------------------------------------")
    print(kwargs.get('context_error')) if kwargs.get('context_error') is not None else None
    print("0. Вернуться в главное меню.")
    print("-1. Вернуться назад.") if kwargs.get('ver') is not None and kwargs.get('ver') == 0 else None
    print("\n")


class Library:
    def __init__(self, file_name: str):

        """
        Initialize the book library with a given file name.

        :param file_name: The name of the file to store the books in JSON format.
        """

        self.file_name: str = file_name  # Name of the file to store books
        self.books: list[Book] = []  # List to hold Book objects
        self.load_books()  # Load books from the file

    def load_books(self) -> None:

        """
        Load books from a JSON file.

        This function attempts to read the book data from the specified JSON file.
        If the file does not exist or is not a valid JSON, a new file will be created.
        """

        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_name = os.path.join(file_path, self.file_name)
        if os.path.exists(file_path):
            try:
                with open(self.file_name, 'r', encoding='utf-8') as file:
                    self.books = [Book(**book) for book in json.load(file)]
                    print('Файл с книгами найден и успешно загружен!')
            except (json.JSONDecodeError, FileNotFoundError):
                print('Файл не является форматом JSON. Новый файл с книгами будет создан в формате JSON!')
        else:
            print('Файл не найден. Новый файл с книгами будет создан в формате JSON!')

    def add_book(self, **kwargs) -> str:

        """
        Add a new book to the library.

        This function prompts the user for book details and adds the new book to the library.

        :param kwargs: Optional keyword arguments for book attributes:
            - title: Title of the book.
            - author: Author of the book.
            - year: Publication year of the book.
        :return: A message indicating the result of the operation.
        """

        book_id = int(self.books[len(self.books) - 1].to_dict()['id']) + 1 if len(self.books) != 0 else 1
        book = Book(
            id=book_id,
            title=kwargs.get('title').strip() if kwargs.get('title') is not None else '',
            author=kwargs.get('author').strip() if kwargs.get('author') is not None else '',
            year=kwargs.get('year').strip() if kwargs.get('year') is not None else ''
        )

        def set_title(new_title: str) -> str:

            """
            Set the title of the book with validation.

            :param new_title: The title to set.
            :return: Validated title.
            """

            while True:
                if new_title == "0":
                    break

                if not new_title:
                    context_menu_print(context_error="Название книги не может быть пустым!")
                    new_title = input("Введите название книги: ").strip()
                    continue
                else:
                    break

            return new_title

        def set_author(new_author: str) -> str:

            """
            Set the author of the book with validation.

            :param new_author: The author to set.
            :return: Validated author.
            """

            while True:
                if new_author == "0":
                    break

                if new_author == "-1":
                    context_menu_print()
                    new_title = input("Введите название книги: ").strip()
                    book.title = set_title(new_title)
                    if book.title == '0':
                        break
                    context_menu_print(ver=0)
                    new_author = input("Введите автора книги: ").strip()
                    continue

                if not new_author:
                    context_menu_print(context_error="Автор книги не может быть пустым!", ver=0)
                    new_author = input("Введите автора книги: ").strip()
                    continue
                else:
                    break

            return new_author

        def set_year(new_year: str) -> int:

            """
            Set the publication year of the book with validation.

            :param new_year: The year to set.
            :return: Validated year.
            """

            while True:
                if new_year == "0":
                    break

                if new_year == "-1":
                    context_menu_print(ver=0)
                    new_author = input("Введите автора книги: ").strip()
                    book.author = set_author(new_author)
                    if book.author == '0':
                        break
                    context_menu_print(ver=0)
                    new_year = input("Введите год издания: ").strip()
                    continue

                if not new_year:
                    context_menu_print(context_error="Год издания не может быть пустым!", ver=0)
                    new_year = input("Введите год издания: ").strip()
                    continue

                if not new_year.isdigit():
                    context_menu_print(context_error="Год издания должен быть числом!", ver=0)
                    new_year = input("Введите год издания: ").strip()
                    continue

                year_value = int(new_year)
                if 1000 <= year_value <= 2024:
                    new_year = int(new_year)
                    break
                else:
                    context_menu_print(context_error="Год издания должен быть больше 1000 и меньше 2024!", ver=0)
                    new_year = input("Введите год издания: ").strip()
                    continue

            return new_year

        while True:
            context_menu_print()
            title = input("Введите название книги: ").strip()
            book.title = set_title(title)
            if book.title == '0':
                return ""

            context_menu_print(ver=0)
            author = input("Введите автора книги: ").strip()
            book.author = set_author(author)
            if book.author == '0' or book.title == '0':
                return ""

            context_menu_print(ver=0)
            year = input("Введите год издания: ").strip()
            book.year = set_year(year)
            if book.year == '0' or book.author == '0':
                return ""

            self.books.append(book)
            self.save_books()
            return "Книга успешно добавлена!"

    def save_books(self) -> None:

        """
        Save the list of books to a JSON file.

        This function writes the current list of books to the specified JSON file.
        """

        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def remove_book(self, book_id: str) -> str:

        """
        Remove a book from the library by its ID.

        This function prompts the user for a book ID and removes the corresponding book
        from the library if found.

        :param book_id: The ID of the book to remove.
        :return: A message indicating the result of the operation.
        """

        while True:
            if not book_id.isdigit():
                context_menu_print(context_error="ID книги должен быть числом!")
                book_id = input("Введите ID книги для удаления: ").strip()
                continue
            if int(book_id) != 0:
                for book in self.books:
                    if book.id == int(book_id):
                        self.books.remove(book)
                        self.save_books()
                        return "Книга успешно удалена!"
                context_menu_print(context_error="Книга с таким ID не найдена.")
                book_id = input("Введите ID книги для удаления: ").strip()
            else:
                return "0"

    def find_books(self, query: str) -> str:

        """
        Find books by title, author, or publication year.

        This function searches for books that match the given query and returns the results.

        :param query: The search query for title, author, or year.
        :return: A string representation of the found books or a message if none are found.
        """

        results = [book for book in self.books
                   if query.lower() in book.title.lower() or
                   query.lower() in book.author.lower() or
                   query == str(book.year)]
        print(results)
        results_print = ''
        if results:
            for book in results:
                results_print += (
                    f"ID: {book.id}, "
                    f"Название: {book.title}, "
                    f"Автор: {book.author}, "
                    f"Год: {book.year}, "
                    f"Статус: {book.status}\n")
            return results_print
        else:
            return "Книги не найдены."

    def display_books(self) -> str:

        """
        Display all books in the library.

        This function returns a string representation of all books currently in the library.

        :return: A string containing details of all books or a message if the library is empty.
        """

        if not self.books:
            return "Нет книг в библиотеке."
        result = ""
        for book in self.books:
            result += (f"ID: {book.id}, "
                       f"Название: {book.title}, "
                       f"Автор: {book.author}, "
                       f"Год: {book.year}, "
                       f"Статус: {book.status}\n")
        return result

    def change_status(self) -> str:

        """
        Change the status of a book by its ID.

        This function prompts the user for a book ID and a new status, then updates the
        status of the corresponding book if found.

        :return: A message indicating the result of the operation.
        """

        context_menu_print()
        book_id = input("Введите ID книги для изменения статуса: ").strip()
        while True:
            if not book_id.isdigit():
                context_menu_print(context_error="ID книги должен быть числом!")
                book_id = input("Введите ID книги для изменения статуса: ").strip()
                continue
            if book_id == "0":
                return ""
            book_id = int(book_id)
            break

        context_menu_print(ver=0)
        new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
        while True:
            if not new_status:
                context_menu_print(context_error="Статус не может быть пустым!", ver=0)
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
                continue

            if new_status == "0":
                return ""

            if new_status == "-1":
                return self.change_status()
            print(new_status)
            print(new_status != "в наличии")
            print(new_status != "выдана")
            if new_status == "в наличии" or new_status == "выдана":
                for book in self.books:
                    if book.id == book_id:
                        if new_status in ["в наличии", "выдана"]:
                            book.status = new_status
                            self.save_books()
                            return "Статус успешно  изменён!"
                return "Книга с таким ID не найдена."
            else:
                context_menu_print(context_error="Статус может быть значением 'в наличии' или 'выдана'!", ver=0)
                new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
                continue
