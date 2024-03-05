import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QListWidget

# App data
class Model:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To do List")
        self.setGeometry(500, 100, 300, 400)

        self.centralWidget = QWidget() # needed cuz mainwindow expects a central widget
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet("color: rgb(255, 255, 255);"
                                         "background-color: rgb(10, 10, 10);"
                                         "font: 25pt \"Arial\" bold;")

        #layout (used to manage positioning and sizing of widgets)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        #input
        self.taskInput = QLineEdit()
        self.taskInput.setStyleSheet("border: 3px solid #ffffff")
        self.layout.addWidget(self.taskInput)
        self.add_button = QPushButton("Add Task")
        self.layout.addWidget(self.add_button)

        self.taskList = QListWidget()
        self.taskList.setStyleSheet("border: 3px solid #ffffff")
        self.layout.addWidget(self.taskList)


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.add_button.clicked.connect(self.add_task)  # connection between the signal and method

    def add_task(self):
        task = self.view.taskInput.text()
        if task: #checks that theres a task indeed
            self.model.add_task(task)
            self.update_view()

    def update_view(self):
        self.view.taskList.clear()
        for task in self.model.get_tasks():
            self.view.taskList.addItem(task)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec())