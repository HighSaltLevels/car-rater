""" Error helper functions """

from PyQt5.QtWidgets import QMessageBox


def show_error(msg):
    """Display a QMessageBox of the {msg}"""
    error = QMessageBox()
    error.setText(msg)
    error.setIcon(QMessageBox.Warning)
    error.setWindowTitle("Error!")
    error.exec_()
