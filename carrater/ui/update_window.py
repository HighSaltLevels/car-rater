""" GUI class for the Update Car Window """

from PyQt5.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QDoubleSpinBox,
    QPushButton,
    QComboBox,
)

from car import Car
from constants import CATEGORIES
from ui.base_window import BaseWindow


class UpdateCarWindow(BaseWindow):
    """Update Car Window"""

    def __init__(self, car_list, title, car):
        self._car = car
        super().__init__(car_list, title)

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

        lbl_kind = QLabel("Kind of Car", self)
        edit_kind = QLineEdit(self)
        edit_kind.setText(self._car.kind)

        lbl_score = QLabel("Score", self)
        spin_box_score = QDoubleSpinBox(self)
        spin_box_score.setRange(0, 10)
        spin_box_score.setValue(float(self._car.score))

        btn_add = QPushButton("Update", self)
        btn_add.clicked.connect(self._update)
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
        grid.addWidget(btn_add, 4, 0)
        grid.addWidget(btn_cancel, 4, 1)

        return {
            "grid": grid,
            "combo_box": box_categories,
            "spin_box": spin_box_score,
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
                "kind": lbl_kind,
            },
        }

    def _update(self):
        """Update the car"""
        owner = self._elements["edits"]["owner"].text()
        category = self._elements["combo_box"].currentText()
        kind = self._elements["edits"]["kind"].text()
        score = str(self._elements["spin_box"].value())

        if self.is_valid(owner, kind):
            car = Car(owner, category, kind, score)
            self._car_list.delete_car(self._car)
            self._car_list.add_car(car)
            self.close()
