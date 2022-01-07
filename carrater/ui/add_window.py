""" GUI class for the Add Car window """

from datetime import date

from PyQt5.QtWidgets import (
    QGridLayout,
    QLineEdit,
    QLabel,
    QComboBox,
    QSpinBox,
    QPushButton,
)

from constants import CATEGORIES
from car import Car
from ui.base_window import BaseWindow


class AddCarWindow(BaseWindow):
    """Add Car Window"""

    def __init__(self, car_file, title):
        self._selected_list = None
        super().__init__(car_file, title)

    @property
    def selected_list(self):
        """Keep the selected_list as a property"""
        return self._selected_list

    def build_ui(self):
        """
        Build the UI and return a dict mapping of results
        """
        grid = QGridLayout()

        lbl_owner = QLabel("Name of Owner", self)
        edit_owner = QLineEdit(self)

        lbl_categories = QLabel("Category", self)
        box_categories = QComboBox(self)
        for category in CATEGORIES:
            box_categories.addItem(category)

        lbl_year = QLabel("Year of Car", self)
        spin_box_year = QSpinBox(self)
        spin_box_year.setRange(1920, date.today().year)
        spin_box_year.setValue(1975)

        lbl_kind = QLabel("Kind of Car", self)
        edit_kind = QLineEdit(self)

        lbl_score = QLabel("Score", self)
        spin_box_score = QSpinBox(self)
        spin_box_score.setRange(0, 100)

        btn_add = QPushButton("Add", self)
        btn_add.clicked.connect(self._add)
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.clicked.connect(self.close)

        grid.addWidget(lbl_owner, 0, 0)
        grid.addWidget(edit_owner, 0, 1)
        grid.addWidget(lbl_categories, 1, 0)
        grid.addWidget(box_categories, 1, 1)
        grid.addWidget(lbl_year, 2, 0)
        grid.addWidget(spin_box_year, 2, 1)
        grid.addWidget(lbl_kind, 3, 0)
        grid.addWidget(edit_kind, 3, 1)
        grid.addWidget(lbl_score, 4, 0)
        grid.addWidget(spin_box_score, 4, 1)
        grid.addWidget(btn_cancel, 5, 0)
        grid.addWidget(btn_add, 5, 1)

        self.setLayout(grid)
        return {
            "grid": grid,
            "combo_box": box_categories,
            "spin_boxes": {
                "year": spin_box_year,
                "score": spin_box_score,
            },
            "edits": {
                "owner": edit_owner,
                "kind": edit_kind,
            },
            "buttons": {
                "add": btn_add,
                "cancel": btn_cancel,
            },
            "labels": {
                "owner": lbl_owner,
                "year": lbl_year,
                "categories": lbl_categories,
                "kind": lbl_kind,
            },
        }

    def _add(self):
        """Add a car to the CarList"""
        owner = self._elements["edits"]["owner"].text()
        category = self._elements["combo_box"].currentText()
        year = self._elements["spin_boxes"]["year"].value()
        kind = self._elements["edits"]["kind"].text()
        score = self._elements["spin_boxes"]["score"].value()

        if self.is_valid(owner, kind):
            car = Car(owner, year, category, kind, score)
            car_list = self._car_file.get_list(category)
            car_list.add_car(car)
            self._selected_list = car_list

            self.close()
