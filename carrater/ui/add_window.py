""" GUI class for the Add Car window """

from PyQt5.QtWidgets import (
    QGridLayout,
    QLineEdit,
    QLabel,
    QComboBox,
    QDoubleSpinBox,
    QPushButton,
)

from constants import CATEGORIES
from car import Car
from ui.base_window import BaseWindow


class AddCarWindow(BaseWindow):
    """Add Car Window"""

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

        lbl_kind = QLabel("Kind of Car", self)
        edit_kind = QLineEdit(self)

        lbl_score = QLabel("Score", self)
        spin_box_score = QDoubleSpinBox(self)
        spin_box_score.setRange(0, 10)

        btn_add = QPushButton("Add", self)
        btn_add.clicked.connect(self._add)
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.clicked.connect(self.close)

        grid.addWidget(lbl_owner, 0, 0)
        grid.addWidget(edit_owner, 0, 1)
        grid.addWidget(lbl_categories, 1, 0)
        grid.addWidget(box_categories, 1, 1)
        grid.addWidget(lbl_kind, 2, 0)
        grid.addWidget(edit_kind, 2, 1)
        grid.addWidget(lbl_score, 3, 0)
        grid.addWidget(spin_box_score, 3, 1)
        grid.addWidget(btn_cancel, 4, 0)
        grid.addWidget(btn_add, 4, 1)

        self.setLayout(grid)
        return {
            "grid": grid,
            "combo_box": box_categories,
            "spin_box": spin_box_score,
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
                "categories": lbl_categories,
                "kind": lbl_kind,
            },
        }

    def _add(self):
        """Add a car to the CarList"""
        owner = self._elements["edits"]["owner"].text()
        category = self._elements["combo_box"].currentText()
        kind = self._elements["edits"]["kind"].text()
        score = str(self._elements["spin_box"].value())

        if self.is_valid(owner, kind):
            car = Car(owner, category, kind, score)
            self._car_list.add_car(car)
            self.close()
