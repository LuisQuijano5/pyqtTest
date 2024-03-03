import sys

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication  # importing from pyqt package


def runQML():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load("..\\Model\\model.qml")

    if not engine.rootObjects():
        return -1

    with open("..\\Styles\\styles.css", "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)

    print("Holaaaa")

    return app.exec()

if __name__ == "__main__":
    sys.exit(runQML())





