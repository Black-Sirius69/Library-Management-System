from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox

import login_ui
import main_win


class Login(QMainWindow, login_ui.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_win = None
        self.setupUi(self)
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_btn.clicked.connect(self.login)
        self.setWindowTitle("Cerebrum - Login")

    def login(self):
        if self.user.text() == "admin" and self.passwd.text() == "admin":
            self.main_win = main_win.MainWindow()
            self.close()
            self.main_win.show()
        else:
            error = QMessageBox()
            error.about(self, "Could not login",
                        "Incorrect username or password.")
            error.setIcon(QMessageBox.Information)
            error.show()
