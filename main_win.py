import sys
from PySide6.QtWidgets import QMainWindow, QApplication

import main_ui
import books
import login
import students

class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login = login.Login()
        self.book = books.AddBooks()
        self.student = students.Student()
        self.book.home_page.clicked.connect(lambda : self.go_home('book'))
        self.student.home_page.clicked.connect(lambda : self.go_home('student'))
        self.setupUi(self)
        self.logout_btn.clicked.connect(self.logout)
        self.add_book.clicked.connect(self.add_books)
        self.add_student.clicked.connect(self.add_students)
        self.setWindowTitle("Cerebrum - Home")

    def logout(self):
        self.close()
        self.login.show()

    def add_books(self):
        self.close()
        self.book.show()

    def add_students(self):
        self.close()
        self.student.show()

    def go_home(self, btn_name):
        if btn_name == 'book':
            self.book.close()
        elif btn_name == 'student':
            self.student.close()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())