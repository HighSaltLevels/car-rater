""" Module for operations on Car objects """


class Car:
    """Car Representation"""

    # pylint: disable=too-many-arguments
    def __init__(self, owner="", year=0, category="", kind="", score=0):
        self._owner = owner
        self._year = year
        self._category = category
        self._kind = kind
        self._score = score

    def __str__(self):
        return f"{self._owner}'s {self._year} {self._category} {self._kind}"

    def __repr__(self):
        return f"{self} at: {self._score}"

    @property
    def owner(self):
        """Owner property"""
        return self._owner

    @property
    def year(self):
        """Year property"""
        return self._year

    @property
    def category(self):
        """Category property"""
        return self._category

    @property
    def kind(self):
        """Kind property"""
        return self._kind

    @property
    def score(self):
        """Score property"""
        return self._score

    def from_dict(self, data):
        """Rebuild the Car object from a dict"""
        try:
            self._owner = data["owner"]
            self._year = data["year"]
            self._category = data["category"]
            self._kind = data["kind"]
            self._score = data["score"]

            return self

        except (ValueError, KeyError) as error:
            raise ValueError("Car file corrupted!") from error

    def to_dict(self):
        """Export the object as a dict"""
        return {
            "owner": self._owner,
            "year": self._year,
            "category": self._category,
            "kind": self._kind,
            "score": self._score,
        }
