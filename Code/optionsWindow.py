# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtWidgets


class Ui_optionsWindow(object):
    def setupUi(self, optionsWindow):
        optionsWindow.setObjectName("optionsWindow")
        optionsWindow.resize(388, 600)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    optionsWindow = QtWidgets.QMainWindow()
    ui = Ui_optionsWindow()
    ui.setupUi(optionsWindow)
    optionsWindow.show()
    sys.exit(app.exec())
