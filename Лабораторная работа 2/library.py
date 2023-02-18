from typing import List

class Library:
    """
    Класс для библиотеки
    """

    def __init__(self, books: List[Book] = None) -> None:
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает id для новой книги, если книг нет, то вернёт 1
        :return: int
        """
        return len(self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвразает индекс книги в библиотеке
        Если книги нет, то выбрасывается исключение ValueError с сообщением: "Книги с запрашиваемым book_id нет"
        :return: int
        """
        for index, book in enumerate(self.books):
            if book.book_id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым book_id нет")
