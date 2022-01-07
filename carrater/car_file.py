""" CarFile class. Responsible for keeping up with all car files """

from car_list import CarList
from constants import CATEGORIES


class CarFile:
    """CarFile class"""

    def __init__(self):
        self._chevy_list = CarList("Chevy")
        self._ford_list = CarList("Ford")
        self._mopar_list = CarList("Mopar")
        self._truck_list = CarList("Truck")
        self._other_list = CarList("Other")

        self._list_mapping = {
            "Chevy": self._chevy_list,
            "Ford": self._ford_list,
            "Mopar": self._mopar_list,
            "Truck": self._truck_list,
            "Other": self._other_list,
        }

    @property
    def chevy_list(self):
        """Make this property Read-Only"""
        return self._chevy_list

    @property
    def ford_list(self):
        """Make this property Read-Only"""
        return self._ford_list

    @property
    def mopar_list(self):
        """Make this property Read-Only"""
        return self._mopar_list

    @property
    def truck_list(self):
        """Make this property Read-Only"""
        return self._truck_list

    @property
    def other_list(self):
        """Make this property Read-Only"""
        return self._other_list

    def get_list(self, category):
        """Return the appropriate list based on specified category"""
        assert category in CATEGORIES, f"Category {category} is not one of {CATEGORIES}"
        return self._list_mapping[category]
