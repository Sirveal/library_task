class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии") -> None:
        """
        Initialize a Book instance.

        :param id: Unique identifier for the book.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Publication year of the book.
        :param status: Availability status of the book, default is "available".
        """

        self.id: int = id  # Unique identifier for the book
        self.title: str = title  # Title of the book
        self.author: str = author  # Author of the book
        self.year: int = year  # Publication year of the book
        self.status: str = status  # Availability status of the book

    def to_dict(self) -> dict:
        """
        Converting the Book instance to a dictionary.

        :return: A dictionary representation of the Book.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
