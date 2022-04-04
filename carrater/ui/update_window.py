""" GUI class for the Update Car Window """

from datetime import date

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
    QPushButton,
    QComboBox,
)

from car import Car
from constants import CATEGORIES
from ui.base_window import BaseWindow


class UpdateCarWindow(BaseWindow):
    """Update Car Window"""

    def __init__(self, car_file, car_list, title, car):
        self._car_list = car_list
        self._car = car
        super().__init__(car_file, title)

    # This UI has a lot of elements in it
    # pylint: disable=too-many-locals
    def build_ui(self):
        """Build the UI"""
        grid = QGridLayout()
        self.setLayout(grid)

        lbl_owner = QLabel("Name of Owner", self)
        edit_owner = QLineEdit(self)
        edit_owner.setText(self._car.owner)

        lbl_categories = QLabel("Category", self)
        box_categories = QComboBox(self)
        for idx, category in enumerate(CATEGORIES):
            box_categories.addItem(category)
            if category == self._car.category:
                box_categories.setCurrentIndex(idx)

        lbl_year = QLabel("Year of Car", self)
        spin_box_year = QSpinBox(self)
        spin_box_year.setRange(1920, date.today().year)
        spin_box_year.setValue(self._car.year)

        lbl_kind = QLabel("Kind of Car", self)
        edit_kind = QLineEdit(self)
        edit_kind.setText(self._car.kind)

        lbl_score = QLabel("Score", self)
        spin_box_score = QSpinBox(self)
        spin_box_score.setRange(0, 100)
        spin_box_score.setValue(self._car.score)

        btn_add = QPushButton("Update", self)
        btn_add.clicked.connect(self._update)
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.clicked.connect(self.close)

        grid.addWidget(lbl_owner, 0, 0, Qt.AlignCenter)
        grid.addWidget(edit_owner, 0, 1, Qt.AlignCenter)
        grid.addWidget(lbl_categories, 1, 0, Qt.AlignCenter)
        grid.addWidget(box_categories, 1, 1, Qt.AlignCenter)
        grid.addWidget(lbl_year, 2, 0, Qt.AlignCenter)
        grid.addWidget(spin_box_year, 2, 1, Qt.AlignCenter)
        grid.addWidget(lbl_kind, 3, 0, Qt.AlignCenter)
        grid.addWidget(edit_kind, 3, 1, Qt.AlignCenter)
        grid.addWidget(lbl_score, 4, 0, Qt.AlignCenter)
        grid.addWidget(spin_box_score, 4, 1, Qt.AlignCenter)
        grid.addWidget(btn_add, 5, 0, Qt.AlignCenter)
        grid.addWidget(btn_cancel, 5, 1, Qt.AlignCenter)

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
                "update": btn_add,
                "cancel": btn_cancel,
            },
            "labels": {
                "owner": lbl_owner,
                "categories": lbl_categories,
                "year": lbl_year,
                "kind": lbl_kind,
            },
        }

    def _update(self):
        """Update the car"""
        owner = self._elements["edits"]["owner"].text()
        category = self._elements["combo_box"].currentText()
        year = self._elements["spin_boxes"]["year"].value()
        kind = self._elements["edits"]["kind"].text()
        score = self._elements["spin_boxes"]["score"].value()

        if self.is_valid(owner, kind):
            car = Car(owner, year, category, kind, score)
            self._car_list.delete_car(self._car)
            self._car_list.add_car(car)
            self.close()
