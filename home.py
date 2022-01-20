from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow
from PyQt6.uic.load_ui import loadUiType
import sys

login, _ = loadUiType('./Library.ui')
main, _ = loadUiType("./main.ui")

class Library(QMainWindow, login):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_btn.clicked.connect(self.login)

    def login(self):
        if self.user.text() == 'admin' and self.passwd.text() == 'admin':
            self.main_win = MainWindow()
            self.close()
            self.main_win.show()
        else:
            print("Not ")

class MainWindow(QMainWindow, main):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logout_btn.clicked.connect(self.logout)

    def logout(self):
        self.login = Library()
        self.close()
        self.login.show()

    def add_book(self):
        "Open the add book ui"
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Library()
    win.show()
    sys.exit(app.exec())
