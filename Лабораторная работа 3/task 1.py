class NameChangeError(Exception):
    """
    Класс ошибок изменения имени
    """

    def __init__(self):
        super().__init__()


class AuthorChangeError(Exception):
    """
    Класс ошибок изменения автора
    """

    def __init__(self):
        super().__init__()


class Book:
    def __init__(self, name: str, author: str):
        self._author = author
        self._name = name

    def __str__(self):
        return f"'{self._name}' {self._author}'"

    def __repr__(self):
        return repr(f'{self._name} {self._author}')

    @property
    def name(self) -> str:
        """
        Возвращает имя книги
        :return: str
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги
        :return: str
        """
        return self._author

    @author.setter
    def author(self, value):
        """
        Устанавливает значение автора
        :param value: значение
        :return: None
        """
        raise AuthorChangeError("Author can't be changed")

    @name.setter
    def name(self, value):
        """
        Устанавливает значение продолжительности книги
        :param value: значение
        :return: None
        """
        raise NameChangeError("Name can't be changed")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float) or duration < 0:
            raise ValueError("Duration must be float and >= 0")
        self._duration = duration

    def __repr__(self):
        return repr(f'{self._name} {self._author} {self._duration}')

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность книги
        :return: float
        """
        return self._duration

    @duration.setter
    def duration(self, value) -> None:
        """
        Устанавливает значение продолжительности
        :param value: значение
        :return: None
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError("Duration - float and >= 0")
        self._duration = value


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Pages - integer and >= 0")
        self._pages = pages

    def __repr__(self):
        return repr(f'{self._name} {self._author} {self._pages}')

    @property
    def pages(self) -> int:
        """
        Возвращает число страниц
        :return: int
        """
        return self._pages

    @pages.setter
    def pages(self, value) -> None:
        """
        Устанавливает значение страниц
        :param value: значение
        :return: None
        """
        if not isinstance(value, int) or value < 0:
            raise ValueError("Pages must be integer and >= 0")
        self._pages = value
