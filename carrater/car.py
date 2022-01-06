""" Module for operations on Car objects """


class Car:
    """Car Representation"""

    def __init__(self, owner="", category="", kind="", score=""):
        self._owner = owner
        self._category = category
        self._kind = kind
        self._score = score

    def __str__(self):
        return f"{self._owner}'s {self._category} {self._kind}"

    def __repr__(self):
        return f"{self} at: {self._score}"

    @property
    def owner(self):
        """Owner property"""
        return self._owner

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
            "category": self._category,
            "kind": self._kind,
            "score": self._score,
        }
