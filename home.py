from PySide6.QtWidgets import QLineEdit, QApplication, QMainWindow, QMessageBox
import login
import books
import main_win
import sqlalchemy
import sys

engine = sqlalchemy.create_engine("mysql://vedant:vedant@localhost/library_management")
conn = engine.connect()

class Login(QMainWindow, login.Ui_MainWindow):
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

class MainWindow(QMainWindow, main_win.Ui_MainWindow):
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

class Books(QMainWindow, books.Ui_MainWindow):
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
            conn.execute(sqlalchemy.text("INSERT INTO books Values(:x, :a, :y, :z, :c, :e, :g, :f, :b, :d, :h, :i)"), [({"x": acc, "y": author_1, 'z': author_2, "a": title, "b": class_num, "c": pub, "d": subject, "e": isbn, "f": call_num, "g": yop, "h": edition, "i": copies})])
            print("Data Added.")
        except Exception as e:
            print(e)
            print("Could not add data")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())
