import sys
from PySide6.QtWidgets import QMainWindow, QApplication

import main_ui
import books
import login
import students
import issue_books

class MainWindow(QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login = login.Login()
        self.book = books.AddBooks()
        self.issues = issue_books.Issue()
        self.student = students.Student()
        self.book.home_page.clicked.connect(lambda : self.go_home('book'))
        self.student.home_page.clicked.connect(lambda : self.go_home('student'))
        self.issues.home_page.clicked.connect(lambda : self.go_home('issues'))
        self.setupUi(self)
        self.logout_btn.clicked.connect(self.logout)
        self.add_book.clicked.connect(self.add_books)
        self.add_student.clicked.connect(self.add_students)
        self.issue_book.clicked.connect(self.issue)
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

    def issue(self):
        self.close()
        self.issues.show()

    def go_home(self, btn_name):
        if btn_name == 'book':
            self.book.close()
        elif btn_name == 'student':
            self.student.close()
        elif btn_name == 'issues':
            self.issues.close()
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
