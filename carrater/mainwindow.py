""" Main Window Class """

from pathlib import Path
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon

from car_list import CarList
from ui.add_window import AddCarWindow
from ui.delete_window import DeleteCarWindow
from ui.select_window import SelectCarWindow
from ui.update_window import UpdateCarWindow
from version import VERSION


APP = QApplication([])
ICON_PATH = f"{Path.home()}/.config/car_rater/icon.ico"


class MainWindow(QWidget):
    """MainWindow class"""

    def __init__(self, parent=None, title=f"Car Rater {VERSION}"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.car_list = CarList()
        self.elements = self.build_ui()

    def build_ui(self):
        """
        Build the UI and return a dict mapping of elements
        """
        grid = QGridLayout()
        self.setLayout(grid)

        add = QPushButton("Add Car", self)
        add.clicked.connect(self._add_car)
        delete = QPushButton("Delete Car", self)
        delete.clicked.connect(self._delete_car)
        update = QPushButton("Update Car", self)
        update.clicked.connect(self._update_car)

        cars = QTextEdit(self)
        cars.setFontFamily("Courier")
        cars.setMinimumWidth(725)
        cars.setMinimumHeight(300)
        cars.setReadOnly(True)
        cars.setText(str(self.car_list))

        close = QPushButton("Close", self)
        close.clicked.connect(self.close)

        grid.addWidget(add, 0, 0)
        grid.addWidget(update, 1, 0)
        grid.addWidget(delete, 2, 0)
        grid.addWidget(cars, 3, 0)
        grid.addWidget(close, 4, 0)

        return {
            "grid": grid,
            "buttons": {
                "add": add,
                "delete": delete,
                "update": update,
            },
            "text_edit": cars,
        }

    def start(self):
        """
        Show and start the GUI
        """
        self.show()
        sys.exit(APP.exec_())

    def _add_car(self):
        """
        Show the Add Car Window
        """
        self.setEnabled(False)
        add_window = AddCarWindow(self.car_list, "Add a Car")
        add_window.exec_()
        add_window.show()
        self.setEnabled(True)

        self.elements["text_edit"].setText(str(self.car_list))

    def _delete_car(self):
        """
        Show the Delete Car Window
        """
        self.setEnabled(False)
        delete_window = DeleteCarWindow(self.car_list, "Delete a Car")
        delete_window.exec_()
        delete_window.show()
        self.setEnabled(True)

        self.elements["text_edit"].setText(str(self.car_list))

    def _update_car(self):
        """
        Show the Update Car Window
        """
        self.setEnabled(False)
        select_window = SelectCarWindow(self.car_list, "Select a Car")
        select_window.exec_()
        select_window.show()

        car = select_window.selected_car
        select_window.close()

        if car is not None:
            update_window = UpdateCarWindow(self.car_list, "Update a Car", car)
            update_window.exec_()
            update_window.show()
            self.elements["text_edit"].setText(str(self.car_list))

        self.setEnabled(True)
