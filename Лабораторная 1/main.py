from datetime import datetime
from typing import List


class Singer:
    """
    Class represents unique Singer
    """

    def __init__(self, pseudonym: str, first_name: str, last_name: str, age: int):
        """
        :param pseudonym: pseudonym
        :param first_name: first name
        :param last_name: last name
        :param age: current age
        """
        self.pseudonym = pseudonym
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def add_one_year_to_age(self) -> None:
        """
        Add +1 to age
        :return: None
        """
        self.age += 1

    def set_pseudonym(self, pseudonym: str) -> None:
        """
        Set new pseudonym
        :param pseudonym: new str pseudonym
        :return: None
        """
        self.pseudonym = pseudonym

    def get_full_name(self) -> str:
        """
        Return full name with pseudonym
        :return: str

        >>> singer = Singer("Oxxxymiron", "Мирон", "Oxxxymiron", 37)
        >>> singer.pseudonym
        'Oxxxymiron'
        >>> singer.get_full_name()
        "Мирон 'Oxxxymiron' Oxxxymiron"
        """
        return f"{self.first_name} '{self.pseudonym}' {self.last_name}"


class Song:
    """
    Class represents unique Song
    """

    def __init__(self, name: str, date: datetime, duration: str, genres: List[str] = None, authors: List[Singer] = None):
        """
        :param name: song name
        :param date: creation date
        :param genres: genres of song
        :param duration: auration of song
        :param authors: Singers
        """
        if genres is None:
            genres = []
        if authors is None:
            authors = []
        self.authors = authors
        self.duration = duration
        self.genres = genres
        self.date = date
        self.name = name

    def set_now_date(self) -> None:
        """
        Setting current date time
        :return: None
        """
        self.date = datetime.now()

    def add_genre(self, genre) -> None:
        """
        Add new genre
        :param genre: str genre
        :return: None
        """
        self.genres.append(genre)

    def get_duration(self) -> str:
        """
        Get duration of song
        :return: str
        """
        return self.duration

    class Concert:
        """
        Class represents Concert show
        """

        def __init__(self, country: str, city: str, place: str, date: datetime, singers: List[Singer] = None):
            """
            :param country: country
            :param city: city
            :param place: place
            :param date: date of the show
            :param singers: list of singers
            """
            if singers is None:
                singers = []
            self.singers = singers
            self.date = date
            self.place = place
            self.city = city
            self.country = country

        def get_anonce_info(self) -> str:
            """
            Get anonce info
            :return: anonce str
            """
            return f"At {self.date} In {self.country},{self.city},{self.place} will be show by {self.singers}. " \
                   f"Start at: {self.date}."

        def set_date(self, date) -> None:
            """
            Set new date
            :param date: new date
            :return: None
            """
            self.date = date

        def add_singer(self, singer: Singer):
            """
            Add new singer to the show
            :param singer:
            :return:
            """
            self.singers.append(singer)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
