from PyQt6 import QtWidgets, QtGui


class Ui_optionsWindow(object):
    def setupUi(self, optionsWindow):
        optionsWindow.setObjectName("optionsWindow")
        optionsWindow.resize(400, 600)
        optionsWindow.setWindowTitle("Options Window")
        optionsWindow.setStyleSheet("background-color:#BEBBBB")

        # Create the label
        label = QtWidgets.QLabel("Selecciona una Opción:", optionsWindow)
        label.setGeometry(50, 50, 350, 40)
        # Style for Label
        font = QtGui.QFont("Arial", 20)  # Create a QFont object
        font.setBold(True)  # Set the font weight to bold
        label.setFont(font)  # Apply the font to the label

        # Create the checkbox for Bisection Method
        checkboxBisecc = QtWidgets.QCheckBox("Método de Bisección", optionsWindow)
        checkboxBisecc.setGeometry(120, 150, 200, 20)
        checkboxBisecc.setFont(QtGui.QFont("Comic Sans", 10))

        # Create the checkbox for Secant Method
        checkboxSecant = QtWidgets.QCheckBox("Método de Secante", optionsWindow)
        checkboxSecant.setGeometry(120, 200, 200, 20)
        checkboxSecant.setFont(QtGui.QFont("Comic Sans", 10))

        # Create the checkbox for Gauss-Jordan Method
        checkboxGJ = QtWidgets.QCheckBox("Método Gauss-Jordan", optionsWindow)
        checkboxGJ.setGeometry(120, 250, 200, 20)
        checkboxGJ.setFont(QtGui.QFont("Comic Sans", 10))

        # Create the checkbox for Gauss-Seidel Method
        checkboxGS = QtWidgets.QCheckBox("Método Gauss-Seidel", optionsWindow)
        checkboxGS.setGeometry(120, 300, 200, 20)
        checkboxGS.setFont(QtGui.QFont("Comic Sans", 10))

        #Create Continue button for this window
        continue_button = QtWidgets.QPushButton("Continuar", optionsWindow)
        continue_button.setGeometry(250, 500, 100, 30)
        continue_button.setFont(QtGui.QFont("Comic",12))
        continue_button.setStyleSheet("background-color:#FD8D8D")

        # Connect the checkbox's stateChanged signal to a handler
        #checkboxBisecc.stateChanged.connect(self.on_checkbox_stateChanged)

"""
    def on_checkbox_stateChanged(self, state):
        # Handle the checkbox state change
        if state == Qt.Checked:
            print("Checkbox is checked")
        else:
            print("Checkbox is unchecked")
"""


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    optionsWindow = QtWidgets.QMainWindow()
    ui = Ui_optionsWindow()
    ui.setupUi(optionsWindow)

    optionsWindow.show()
    sys.exit(app.exec())
