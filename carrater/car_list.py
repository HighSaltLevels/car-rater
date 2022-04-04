""" CarList class. Responsible for sorting and keeping up with cars and results """

import json
import os
from pathlib import Path

from car import Car

CAR_PATH = f"{Path.home()}/.config/car_rater"


class CarList:
    """CarList class"""

    def __init__(self, category):
        self._category = category
        self._cars = []
        self._path = f"{CAR_PATH}/{category}.json"

        if not os.path.isfile(self._path):
            self.create_car_file()

        else:
            self.load()

        super().__init__()

    def __str__(self):
        """Return text box friendly list of cars"""
        return_str = "\n"
        return_str += f"{self._category}".center(58)
        return_str += "\n\n"
        return_str += 58 * "="
        return_str += "\n"
        return_str += "Owner              | Year | Kind of Car          | Score |\n"
        return_str += f"{58 * '-'}\n"
        for car in self._cars:
            return_str += (
                f"{car.owner:18} | {car.year:4} | {car.kind:20} | {car.score:5} |\n"
            )

        return return_str

    @property
    def category(self):
        """Make category read only"""
        return self._category

    @property
    def cars(self):
        """Return the list of cars"""
        return self._cars

    def create_car_file(self):
        """Create a brand new car file"""
        os.makedirs(CAR_PATH, exist_ok=True)
        with open(self._path, "w", encoding="utf-8"):
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
            with open(self._path, encoding="utf-8") as car_file:
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
        with open(self._path, "w", encoding="utf-8") as car_file:
            car_file.write(json.dumps(cars))
