import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MySQL Connection DEMO')
        self.init_ui()

    def init_ui(self):
        pass
