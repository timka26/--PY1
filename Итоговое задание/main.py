import random


class Car:
    """
    Abstract car
    """

    def __init__(self, model: str, type: str, color: str, country_creator: str, car_stats: str):
        self.model = model
        self.type = type
        self.color = color
        self.country_creator = country_creator
        self._car_stats = car_stats

    def __str__(self) -> str:
        """
        Abstract car string representation
        :return: str
        """
        return f"Model: {self.model} with color: {self.color}"

    def __repr__(self) -> str:
        """
        Abstract car object representation
        :return: str
        """
        return f"Car(model={self.model}, type={self.type}, color={self.color}, country_creator={self.country_creator}"

    def greet_driver(self) -> str:
        """
        greeting driver
        :return: str
        """
        return f"{self.model} greeting you! Beep!"


class Mercedes(Car):
    """
    Mercedes car
    """

    def __init__(self, model: str, type: str, color: str, country_creator: str, car_stats: str, interior_lighting: str,
                 ar: str, massage: str) -> None:
        super().__init__(model, type, color, country_creator, car_stats)
        self.interior_lighting = interior_lighting
        self.ar = ar
        self.massage = massage

    def __str__(self) -> str:
        """
        Mercedes string representation
        :return: str
        """

    def __repr__(self) -> str:
        """
        Mercedes object representation
        :return: str
        """

    def greet_driver(self):
        """
        greeting driver
        :return: str
        """
        self.interior_lighting = "green"
        return f"Mercedes model {self.model} greets you with green light!"

    def __update_ar_system(self):
        """
        Updating AR system
        :return: None
        """
        self.ar = "updating..."


class Tesla(Car):
    """
    Tesla car
    """

    def __init__(self, model: str, type: str, color: str, country_creator: str, car_stats: str, auto_pilot: str,
                 auto_doors: str) -> None:
        super().__init__(model, type, color, country_creator, car_stats)
        self.auto_doors = auto_doors
        self.auto_pilot = auto_pilot

    def __str__(self) -> str:
        """
        Tesla string representation
        :return: str
        """

    def __repr__(self) -> str:
        """
        Tesla object representation
        :return: str
        """

    def greet_driver(self):
        """
        greeting driver
        :return: str
        """
        self.auto_doors = "open"
        self.auto_pilot = "on"
        return f"Tesla model {self.model} greets you with opened doors and auto pilot is on!"

    def __count_car_stats_for_car_producer(self) -> None:
        """
        count secret info only for Tesla company
        :return: None
        """
        self._car_stats = random.randint(0, 100)
