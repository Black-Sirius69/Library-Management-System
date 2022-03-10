import sys

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import sqlalchemy
from backend import session, Book

from PySide6.QtWidgets import QLineEdit, QMainWindow, QMessageBox, QApplication
import book_ui
import delete


class AddBooks(QMainWindow, book_ui.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.delete_ui = delete.Delete()
        self.title.setFocus()
        self.add_data.clicked.connect(self.add)
        self.setWindowTitle("Cerebrum - Add Books")
        self.delete_btn.clicked.connect(lambda : self.delete_ui.show_ui("Admission", self.delete_func))

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
            book = Book(Title=title, Author_1=author_1, Author_2=author_2, ISBN=isbn, Call_no=call_num,
                        Class_no=class_num, copies=copies, publisher=pub, Year_of_publication=yop,
                        Edition=edition, Subject=subject, Acc_no=acc)
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

    def delete_func(self):
        id = int(self.delete_ui.id.text()) if self.delete_ui.id.text() != '' else None

        # Check if student is present
        stmt = sqlalchemy.select(Book).filter_by(Acc_no=id)
        result = session.execute(stmt).scalars().all()
        if result:
            stmt = sqlalchemy.delete(Book).filter_by(Acc_no=id)
            session.execute(stmt)
            session.commit()
            success = QMessageBox()
            success.setText("Book Record deleted")
            success.setWindowTitle("Successful")
            success.setIcon(QMessageBox.Icon.Information)
            success.setStandardButtons(QMessageBox.StandardButton.Ok)
            success = success.exec()
            self.delete_ui.id.clear()
        else :
            error = QMessageBox()
            error.setText("Book not found")
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Icon.Critical)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                self.delete_ui.id.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AddBooks()
    win.show()
    sys.exit(app.exec())
