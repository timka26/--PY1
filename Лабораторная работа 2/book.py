from typing import List


class Book:
    """
    Класс для книги
    """

    def __init__(self, id: int, book_name: str, pages: int) -> None:
        self.pages = pages
        self.book_name = book_name
        self.book_id = id

    def __str__(self) -> str:
        return f"Книга {self.book_name}"

    def __repr__(self) -> str:
        return f"Book(id_={self.book_id}, name={self.book_name}, pages={self.pages})"