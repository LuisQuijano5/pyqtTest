import mysql.connector
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MySQL Connection Example')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.labelN = QLabel('Enter Name:')
        self.textboxN = QLineEdit()
        self.labelP = QLabel('Enter Price:')
        self.textboxP = QLineEdit()
        self.labelQ = QLabel('Enter Quantity')
        self.textboxQ = QLineEdit()
        self.labelC = QLabel('Enter Color')
        self.textboxC = QLineEdit()
        self.button = QPushButton('Submit')
        self.button.clicked.connect(self.submit)

        layout.addWidget(self.labelN)
        layout.addWidget(self.textboxN)
        layout.addWidget(self.labelP)
        layout.addWidget(self.textboxP)
        layout.addWidget(self.labelQ)
        layout.addWidget(self.textboxQ)
        layout.addWidget(self.labelC)
        layout.addWidget(self.textboxC)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def submit(self):
        nameV = self.textboxN.text()
        priceV = self.textboxP.text()
        quantityV = self.textboxQ.text()
        colorV = self.textboxC.text()

        HOST = 'localhost'
        DATABASE = 'inventory'
        USER = 'topicos'
        PASSWORD = 'TopicosProgra#'

        # Input validation
        if not (nameV and priceV and quantityV and colorV):
            QMessageBox.warning(self, 'Warning', 'Please fill in all fields')
            return

        try:
            priceV = float(priceV)
            quantityV = int(quantityV)
        except ValueError:
            QMessageBox.warning(self, 'Warning', 'Invalid price or quantity')
            return

        # Establishing the connection
        connection = mysql.connector.connect(
            host=HOST,
            database=DATABASE,
            user=USER,
            password=PASSWORD
        )

        cursor = connection.cursor()

        insert_query = "INSERT INTO products (name, price, quantity, color) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (nameV, priceV, quantityV, colorV))

        # Commit the changes
        connection.commit()

        # Close the connection
        connection.close()
        print("Data inserted successfully.")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()