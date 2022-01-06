""" GUI class for the Select Car Window """

from PyQt5.QtWidgets import QGridLayout, QLabel, QComboBox, QPushButton

from ui.base_window import BaseWindow


class SelectCarWindow(BaseWindow):
    """Select Car Window"""

    def __init__(self, car_list, title):
        super().__init__(car_list, title)
        self._selected_car = None

    def build_ui(self):
        """Build the UI"""
        grid = QGridLayout()
        self.setLayout(grid)

        lbl = QLabel("Select a Car to Delete", self)
        box = QComboBox(self)
        box.setMinimumWidth(500)
        for car in self._car_list.cars:
            box.addItem(str(car))

        btn_select = QPushButton("Select", self)
        btn_select.clicked.connect(self._select)
        btn_cancel = QPushButton("Cancel", self)
        btn_cancel.clicked.connect(self.close)

        grid.addWidget(lbl, 0, 0, 1, 1)
        grid.addWidget(box, 0, 1, 1, 2)
        grid.addWidget(btn_cancel, 1, 0, 2, 1)
        grid.addWidget(btn_select, 1, 1, 2, 2)

        return {
            "grid": grid,
            "box": box,
            "btn": {
                "select": btn_select,
                "cancel": btn_cancel,
            },
        }

    @property
    def selected_car(self):
        """Property for exposing the selected car"""
        return self._selected_car

    def _select(self):
        """Select the Car"""
        self._selected_car = self._car_list.cars[self._elements["box"].currentIndex()]
        self.close()
