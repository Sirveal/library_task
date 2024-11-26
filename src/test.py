import unittest
from unittest.mock import patch, MagicMock
from library import Library
from main import main


class TestLibraryConsoleApp(unittest.TestCase):

    """
        Unit test class for testing the Library console application.

        This class contains test cases for various functionalities of the Library application,
        including adding, removing, finding, displaying books, changing book status, and exiting.
    """

    def setUp(self):

        """
            Set up the test environment before each test case.

            This method creates a mock object for the Library class and sets up return values
            for its methods to simulate expected behavior during testing.
        """

        # Create a mock for the Library
        self.library_mock = MagicMock(spec=Library)
        self.library_mock.add_book.return_value = "Книга успешно добавлена!"
        self.library_mock.remove_book.return_value = "Книга успешно удалена!"
        self.library_mock.find_books.return_value = "Найденные книги:\n..."
        self.library_mock.display_books.return_value = "Все книги в библиотеке:\n..."
        self.library_mock.change_status.return_value = "Статус успешно изменён!"

    @patch('builtins.input', side_effect=['1', '0'])  # Simulate input
    @patch('main.Library', return_value=None)  # Mock the Library class
    def test_add_book(self, mock_library, mock_input):

        """
            Test the addition of a book to the library.

            This test simulates user input for adding a book and verifies that the correct
            success message is printed when a book is added successfully.
        """

        mock_library.return_value = self.library_mock  # Return our mock
        with patch('builtins.print') as mock_print:
            main()  # Call the main function
            mock_print.assert_any_call("Книга успешно добавлена!")  # Check output

    @patch('builtins.input', side_effect=['2', '1', '-1', '1', '0'])  # Simulate input
    @patch('main.Library', return_value=None)
    def test_remove_book(self, mock_library, mock_input):

        """
            Test the removal of a book from the library.

            This test simulates user input for removing a book and verifies that the correct
            success message is printed when a book is removed successfully.
        """

        mock_library.return_value = self.library_mock
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Книга успешно удалена!") # Check output

    @patch('builtins.input', side_effect=['3', 'Master', '0'])  # Simulate input
    @patch('main.Library', return_value=None)
    def test_find_books(self, mock_library, mock_input):

        """
            Test the searching of books in the library.

            This test simulates user input for finding books and verifies that the correct
            found books message is printed.
        """

        mock_library.return_value = self.library_mock
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Найденные книги:\n...")  # Check output

    @patch('builtins.input', side_effect=['4', '0'])  # Simulate input
    @patch('main.Library', return_value=None)
    def test_display_books(self, mock_library, mock_input):

        """
            Test the display of all books in the library.

            This test simulates user input for displaying books and verifies that the correct
            message showing all books is printed.
        """

        mock_library.return_value = self.library_mock
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Все книги в библиотеке:\n...")  # Check output

    @patch('builtins.input', side_effect=['5', '0'])  # Simulate input
    @patch('main.Library', return_value=None)
    def test_change_status(self, mock_library, mock_input):

        """
            Test the changing of a book's status.

            This test simulates user input for changing the status of a book and verifies
            that the correct success message is printed.
        """

        mock_library.return_value = self.library_mock
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("Статус успешно изменён!")  # Check output

    @patch('builtins.input', side_effect=['0'])  # Simulate exit
    @patch('main.Library', return_value=None)
    def test_exit(self, mock_library, mock_input):

        """
            Test the exit functionality of the library application.

            This test simulates user input for exiting the application and verifies that
            the print function was called at least once, indicating that the menu was displayed.
        """

        mock_library.return_value = self.library_mock
        with patch('builtins.print') as mock_print:
            main()
            # Check that the menu was printed at least once
            self.assertGreater(mock_print.call_count, 0)  # Ensure print was called


if __name__ == "__main__":
    unittest.main()  # Run the unit tests
