from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader
import sys

class Library(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        loader = QUiLoader();
        self.ui = loader.load('./Library.ui', None)
        self.ui.passwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.login_btn.clicked.connect(self.login)
        self.ui.show()
    
    def login(self):
        if self.ui.user.text() == "admin" and self.ui.passwd.text() == 'admin':
            print("Login Successfull.")
        else:
            print("Login UnSuccessful.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Library()
    sys.exit(app.exec())
