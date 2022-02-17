from PySide6.QtWidgets import QMainWindow

import main_ui
import books
import login


class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login = login.Login()
        self.book = books.AddBooks()
        self.setupUi(self)
        self.logout_btn.clicked.connect(self.logout)
        self.add_book.clicked.connect(self.add_books)
        self.setWindowTitle("Cerebrum - Home")

    def logout(self):
        self.close()
        self.login.show()

    def add_books(self):
        self.close()
        self.book.show()
