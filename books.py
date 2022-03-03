import sys

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

from PySide6.QtWidgets import QLineEdit, QMainWindow, QMessageBox, QFileDialog, QApplication
import book_ui

Base = automap_base()

#  set the sqlalchemy engine to mysql server and connect
engine = sqlalchemy.create_engine(
    "mysql://vedant:vedant@localhost/library_management")

# Reflect tables
Base.prepare(engine, reflect=True)

Book = Base.classes.books

# Create a session
session = Session(engine)


class AddBooks(QMainWindow, book_ui.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.title.setFocus()
        self.add_data.clicked.connect(self.add)
        self.setWindowTitle("Cerebrum - Add Books")

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
            success.setText("Data Added")
            success.setWindowTitle("Successful")
            success.setIcon(QMessageBox.Icon.Information)
            success.setStandardButtons(QMessageBox.StandardButton.Ok)
            success = success.exec()
            if success == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
        except IntegrityError:
            error = QMessageBox()
            error.setText(f"Could Not add data duplicate accession number {self.acc_no.text()}.")
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Icon.Critical)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
        except SQLAlchemyError:
            error = QMessageBox()
            error.setText("Could not add data")
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Icon.Critical)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()

session.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AddBooks()
    win.show()
    sys.exit(app.exec())
