from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow, QMessageBox
from PyQt6.uic.load_ui import loadUiType
import sys

login, _ = loadUiType('./Login.ui')
main, _ = loadUiType("./main.ui")

class Login(QMainWindow, login):
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
            error = QMessageBox()
            error.about(self, "Could not login", "Incorrect username or password.")
            error.setIcon(QMessageBox.Icon.Information)
            error.show()

class MainWindow(QMainWindow, main):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.logout_btn.clicked.connect(self.logout)

    def logout(self):
        self.login = Login()
        self.close()
        self.login.show()

    def add_books(self):
        "Open the add book ui"
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())
