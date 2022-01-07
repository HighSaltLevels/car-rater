""" GUI class for the Delete Car Window """

from PyQt5.QtWidgets import QComboBox, QLabel, QGridLayout, QPushButton

from ui.base_window import BaseWindow


class DeleteCarWindow(BaseWindow):
    """Delete Car Window"""

    def __init__(self, car_file, car_list, title):
        self._car_list = car_list
        super().__init__(car_file, title)

    def build_ui(self):
        """Build the UI"""

        grid = QGridLayout()
        self.setLayout(grid)

        lbl = QLabel("Select a Car to Delete", self)
        box = QComboBox(self)
        box.setMinimumWidth(500)
        for car in self._car_list.cars:
            box.addItem(str(car))

        btn_delete = QPushButton("Delete", self)
        btn_delete.clicked.connect(self._delete)
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.clicked.connect(self.close)

        grid.addWidget(lbl, 0, 0, 1, 1)
        grid.addWidget(box, 0, 1, 1, 2)
        grid.addWidget(btn_cancel, 1, 0, 2, 1)
        grid.addWidget(btn_delete, 1, 1, 2, 2)

        return {
            "grid": grid,
            "lbl": lbl,
            "box": box,
            "btn": {
                "delete": btn_delete,
                "cancel": btn_cancel,
            },
        }

    def _delete(self):
        """Delete the selected car from the list"""
        car = self._car_list.cars[self._elements["box"].currentIndex()]
        self._car_list.delete_car(car)
        self.close()
