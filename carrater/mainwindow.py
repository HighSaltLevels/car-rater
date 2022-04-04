""" Main Window Class """

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QTextEdit, QTabWidget

from car_file import CarFile
from constants import ICON_PATH
from ui.add_window import AddCarWindow
from ui.delete_window import DeleteCarWindow
from ui.select_window import SelectCarWindow, SelectCategoryWindow
from ui.update_window import UpdateCarWindow
from version import VERSION


APP = QApplication([])


class MainWindow(QWidget):
    """MainWindow class"""

    def __init__(self, parent=None, title=f"Car Rater {VERSION}"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.car_file = CarFile()
        self.elements = self.build_ui()

    def build_ui(self):
        """
        Build the UI and return a dict mapping of elements
        """
        grid_main = QGridLayout()
        self.setLayout(grid_main)

        add = QPushButton("Add Car", self)
        add.clicked.connect(self._add_car)
        delete = QPushButton("Delete Car", self)
        delete.clicked.connect(self._delete_car)
        update = QPushButton("Update Car", self)
        update.clicked.connect(self._update_car)

        chevies = QTextEdit(self)
        fords = QTextEdit(self)
        mopars = QTextEdit(self)
        trucks = QTextEdit(self)
        other = QTextEdit(self)

        tabs = QTabWidget()
        tabs.addTab(chevies, "Chevies")
        tabs.addTab(fords, "Fords")
        tabs.addTab(mopars, "Mopars")
        tabs.addTab(trucks, "Trucks")
        tabs.addTab(other, "Other")

        for text_edit in [chevies, fords, mopars, trucks, other]:
            text_edit.setFontFamily("Courier")
            text_edit.setMinimumWidth(500)
            text_edit.setMinimumHeight(200)
            text_edit.setReadOnly(True)

        chevies.setText(str(self.car_file.chevy_list))
        fords.setText(str(self.car_file.ford_list))
        mopars.setText(str(self.car_file.mopar_list))
        trucks.setText(str(self.car_file.truck_list))
        other.setText(str(self.car_file.other_list))

        close = QPushButton("Close", self)
        close.clicked.connect(self.close)

        grid_main.addWidget(add, 0, 0)
        grid_main.addWidget(update, 1, 0)
        grid_main.addWidget(delete, 2, 0)
        grid_main.addWidget(close, 3, 0)
        grid_main.addWidget(tabs, 4, 0)

        return {
            "grids": {
                "main": grid_main,
            },
            "buttons": {
                "add": add,
                "delete": delete,
                "update": update,
            },
            "text_edits": {
                "Chevy": chevies,
                "Ford": fords,
                "Mopar": mopars,
                "Truck": trucks,
                "Other": other,
            },
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
        add_window = AddCarWindow(self.car_file, "Add a Car")
        add_window.exec_()
        add_window.show()

        car_list = add_window.selected_list
        if car_list is not None:
            self.elements["text_edits"][car_list.category].setText(str(car_list))

        self.setEnabled(True)

    def _delete_car(self):
        """
        Show the Delete Car Window
        """
        self.setEnabled(False)
        select_window = SelectCategoryWindow(self.car_file, "Select a Category")
        select_window.exec_()
        select_window.show()

        car_list = select_window.car_list
        select_window.close()

        if car_list is not None:
            delete_window = DeleteCarWindow(self.car_file, car_list, "Delete a Car")
            delete_window.exec_()
            delete_window.show()
            self.elements["text_edits"][car_list.category].setText(str(car_list))

        self.setEnabled(True)

    def _update_car(self):
        """
        Show the Update Car Window
        """
        self.setEnabled(False)

        select_window = SelectCategoryWindow(self.car_file, "Select a Category")
        select_window.exec_()
        select_window.show()

        car_list = select_window.car_list
        select_window.close()
        # Exit early if they hit cancel
        if car_list is None:
            self.setEnabled(True)
            return

        select_window = SelectCarWindow(self.car_file, car_list, "Select a Car")
        select_window.exec_()
        select_window.show()

        car = select_window.selected_car
        select_window.close()

        if car is not None:
            update_window = UpdateCarWindow(
                self.car_file, car_list, "Update a Car", car
            )
            update_window.exec_()
            update_window.show()
            self.elements["text_edits"][car_list.category].setText(str(car_list))

        self.setEnabled(True)
