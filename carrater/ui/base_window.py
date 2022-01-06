""" GUI class base for other windows """

from PyQt5.QtWidgets import QDialog

from errors import show_error


OWNER_MAX_LEN = 30
KIND_MAX_LEN = 33


class BaseWindow(QDialog):
    """Base Window class"""

    def __init__(self, car_list, title=""):
        super().__init__(None)
        self.setWindowTitle(title)
        self._car_list = car_list
        self._elements = self.build_ui()

    def build_ui(self):
        """Build the UI"""
        raise NotImplementedError("Subclasses must implement build_ui")

    @property
    def car_list(self):
        """Make the car_list a property"""
        return self._car_list

    @staticmethod
    def is_valid(owner, kind):
        """Return True if owner and kind are within size limits"""
        if len(owner) > OWNER_MAX_LEN:
            show_error(f"Owner name cannot be greater than {OWNER_MAX_LEN} characters.")
            return False

        if len(kind) > KIND_MAX_LEN:
            show_error(f"Kind of car cannot be greater than {KIND_MAX_LEN} characters.")
            return False

        if len(owner) < 1:
            show_error('You must fill out the "Owner" field')
            return False

        if len(kind) < 1:
            show_error('You must fill out the "Kind of Car" field')
            return False

        return True
