from PyQt6.QtWidgets import QLineEdit, QApplication, QMainWindow, QMessageBox
from PyQt6.uic.load_ui import loadUiType
import mysql.connector as mc
import sys

login, _ = loadUiType('./Login.ui')
main, _ = loadUiType("./main.ui")
book, _ = loadUiType('./books.ui')

con = mc.connect(host='localhost', user='vedant', passwd='vedant', database='library_management')
cur = con.cursor()

class Login(QMainWindow,login):
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
        self.add_book.clicked.connect(self.add_books)

    def logout(self):
        self.login = Login()
        self.close()
        self.login.show()

    def add_books(self):
        """
        Open the books ui
        """
        self.book = Books()
        self.close()
        self.book.show()

class Books(QMainWindow, book):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.title.setFocus()
        self.add_data.clicked.connect(self.add)

    def add(self):
        try:
            title = self.title.text()
            author_1 = self.author_1.text()
            author_2 = self.author_2.text()
            isbn = self.isbn.text()
            pub = self.publisher.text()
            subject = self.subject.text()
            yop = self.year_of_publication.text()
            acc = self.acc_no.text()
            class_num = self.class_number.text()
            call_num = self.call_number.text()
            edition = self.edition.text()
            copies = self.copies.text()
            cur.execute(f"INSERT INTO BOOKS VALUES({acc}, {author_1}, {author_2}, {title}, {class_num}, {pub}, {subject}, {isbn}, {call_num}, {yop}, {edition}, {copies})")
            con.commit()
            print("Data Added.")
        except Exception as e:
            print(e)
            print("Could not add data")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())
