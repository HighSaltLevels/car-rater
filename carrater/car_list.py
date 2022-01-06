""" CarList class. Responsible for sorting and keeping up with cars and results """

import json
import os
from pathlib import Path

from car import Car

CAR_PATH = f"{Path.home()}/.config/car_rater"
CAR_FILE = f"{CAR_PATH}/carlist.json"


class CarList:
    """CarList class"""

    def __init__(self):
        self._cars = []

        if not os.path.isfile(CAR_FILE):
            self.create_car_file()

        else:
            self.load()

        super().__init__()

    def __str__(self):
        """Return text box friendly list of cars"""
        return_str = (
            "Owner                          | Category | Kind of Car                       "
            "| Score |\n"
        )
        return_str += f"{87 * '-'}\n"
        for car in self._cars:
            return_str += (
                f"{car.owner:30} | {car.category:8} | {car.kind:33} | {car.score:5} |\n"
            )

        return return_str

    @property
    def cars(self):
        """Return the list of cars"""
        return self._cars

    @staticmethod
    def create_car_file():
        """Create a brand new car file"""
        os.makedirs(CAR_PATH, exist_ok=True)
        with open(CAR_FILE, "w", encoding="utf-8"):
            pass

    def add_car(self, car):
        """Add a car to the list"""
        self._cars.append(car)
        self.sort()
        self.write()
        print(f'Added car "{car}"')

    def delete_car(self, car):
        """Delete a car from the list"""
        self._cars.remove(car)
        self.write()
        print(f'Deleted car "{car}"')

    def load(self):
        """Load the current data from disk"""
        try:
            with open(CAR_FILE, encoding="utf-8") as car_file:
                self._cars = [Car().from_dict(car) for car in json.load(car_file)]

        except json.decoder.JSONDecodeError:
            print("Car file is corrupted! Creating a new one")
            self.create_car_file()

    def sort(self):
        """Sort the cars for ratings in order of highest to lowest"""
        # Selection Sort
        new_cars = []
        for _ in range(len(self._cars)):
            curr_highest = 0

            for idx, car in enumerate(self._cars):
                if car.score > self._cars[curr_highest].score:
                    curr_highest = idx

            new_cars.append(self._cars[curr_highest])
            del self._cars[curr_highest]

        self._cars = new_cars

    def write(self):
        """Write the current cars to disk"""
        cars = [car.to_dict() for car in self._cars]
        with open(CAR_FILE, "w", encoding="utf-8") as car_file:
            car_file.write(json.dumps(cars))


def get_longest_str(cars):
    """Function for getting the longest of each string"""
    longest_owner = 0
    longest_category = 0
    longest_kind = 0

    for car in cars:
        if len(car.owner) > longest_owner:
            longest_owner = len(car.owner)

        if len(car.category) > longest_category:
            longest_category = len(car.category)

        if len(car.kind) > longest_kind:
            longest_kind = len(car.kind)

    return longest_owner + 2, longest_category + 2, longest_kind + 2
