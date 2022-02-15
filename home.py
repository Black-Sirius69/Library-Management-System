import os
import sys

import MySQLdb
import sqlalchemy
from PySide6.QtWidgets import QLineEdit, QApplication, QMainWindow, QMessageBox, QFileDialog
from pymarc import MARCReader
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import books
import login
import main_win

# import time

Base = automap_base()

#  set the sqlalchemy engine to mysql server and connect
engine = sqlalchemy.create_engine(
    "mysql://vedant:vedant@localhost/library_management")

# Reflect tables
Base.prepare(engine, reflect=True)

Book = Base.classes.books
Student = Base.classes.students

# Create a session
session = Session(engine)


class Login(QMainWindow, login.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_win = None
        self.setupUi(self)
        self.passwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_btn.clicked.connect(self.login)
        self.setWindowTitle("Cerebrum")

    def login(self):
        if self.user.text() == "admin" and self.passwd.text() == "admin":
            self.main_win = MainWindow()
            self.close()
            self.main_win.show()
        else:
            error = QMessageBox()
            error.about(self, "Could not login",
                        "Incorrect username or password.")
            error.setIcon(QMessageBox.Information)
            error.show()


class MainWindow(QMainWindow, main_win.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.login = Login()
        self.book = AddBooks()
        self.setupUi(self)
        self.logout_btn.clicked.connect(self.logout)
        self.add_book.clicked.connect(self.add_books)

    def logout(self):
        self.close()
        self.login.show()

    def add_books(self):
        self.close()
        self.book.show()


class AddBooks(QMainWindow, books.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.title.setFocus()
        self.add_data.clicked.connect(self.add)
        self.import_data.clicked.connect(self.import_book)

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
            book = Book(Title=title, Author_1=author_1, Author_2=author_2, isbn=isbn, call_no=call_num,
                        class_no=class_num, copies=copies, publisher=pub, year_of_publication=yop,
                        edition=edition, subject=subject, Acc_no=acc)
            session.add(book)
            session.commit()
            success = QMessageBox()
            success.about(self, "SUCCESSFUL", "Data Added")
            success.setStandardButtons(QMessageBox.StandardButton.Ok)
            success = success.exec()
            if success == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
        except SQLAlchemyError:
            error = QMessageBox()
            error.about(self, "Error", "Could not add data")
            error.setIcon(QMessageBox.Critical)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()

    def import_book(self):
        skipped = []
        name, _ = QFileDialog.getOpenFileName(self, "Select Marc File", os.getcwd(
        ), "Marc Files (*.mrc);; CSV Files (*.csv);; All Files (*)")
        if name != 0 and name[-4::] == '.mrc':
            with open(name, 'rb') as file:
                reader = MARCReader(file)
                added = 0
                for record in reader:
                    title = record.title()
                    author_1 = record.author()
                    author_2 = None
                    if record['541']:
                        acc_no = record['541']['a']
                        if type(acc_no) == str:
                            pos = acc_no.find('J')
                            acc_no = acc_no[0:pos]
                    elif record['952']:
                        acc_no = record['952']['p']
                        if type(acc_no) == str:
                            pos = acc_no.find('J')
                            acc_no = acc_no[0:pos]
                    else:
                        print("Cannot Enter Data. Accession Number not found.")
                        raise ValueError("Cannot Enter Data without Acc No.")

                    if acc_no is None:
                        skipped.append(record.title())
                        continue

                    if record['700']:
                        author_2 = record['700']['a']
                    publisher = record.publisher()
                    yop = record.pubyear()
                    if type(yop) == str:
                        yop = None
                    sub = None
                    if record.subjects():
                        sub = record.subjects()[0]['a']
                    isbn = record.isbn()
                    class_no = None
                    call_no = None
                    if record['082']:
                        class_no = record['082']['a']
                        call_no = record['082']['b']
                    if type(class_no) == str:
                        class_no = None
                    edition = None
                    if record['250']:
                        edition = record['250']['a']
                    copies = 1
                    if record['562']:
                        copies = record['562']['e']
                    try:
                        book = Book(Acc_no=acc_no, Title=title, Author_1=author_1, Author_2=author_2,
                                    publisher=publisher, isbn=isbn, year_of_publication=yop, class_no=class_no,
                                    call_no=call_no, subject=sub, edition=edition, copies=copies)
                        session.add(book)
                        session.commit()
                        added += 1
                    except MySQLdb.IntegrityError:
                        skipped.append(title)
                        session.rollback()
                    except IntegrityError:
                        skipped.append(title)
                        session.rollback()
                success = QMessageBox()
                success.about(self, "Successful",
                              f'Added {added} books.\n Could not add {len(skipped)} books as they were not compatible.')


session.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())
