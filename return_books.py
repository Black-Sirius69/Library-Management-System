import sys
from PySide6.QtWidgets import QDialog, QMessageBox, QApplication, QLineEdit
from sqlalchemy import create_engine, ForeignKey, Column, Table, Date
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import delete, select
import return_ui

Base = automap_base()
metadata = Base.metadata

engine = create_engine(
    'mysql://vedant:vedant@localhost/library_management'
)

t_issues = Table(
    'issues', metadata,
    Column('book_no', ForeignKey('books.Acc_no', ondelete='CASCADE', onupdate='CASCADE'), index=True, comment='The Accession number of the book issued'),
    Column('student_id', ForeignKey('students.Admno', ondelete='CASCADE', onupdate='CASCADE'), index=True, comment='The Admission Number of the student who is issuing the book'),
    Column('issue_date', Date, comment='The date of issuing the book'),
    Column('return_date', Date, comment='The date of returning the book'),
    comment='A table for storing info of issued books'
)

Base.prepare(engine, reflect = True)
Book = Base.classes.books
Student = Base.classes.students

session = Session(engine)

class Return(QDialog, return_ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Cerebrum - Return Book")
        self.return_book.clicked.connect(self.return_books)


    def return_books(self):
        book_id = int(self.book_no.text()) if self.book_no.text() != '' else None

        # Validate If Book Issued
        stmt = select(t_issues).filter_by(book_no=book_id)
        result = session.execute(stmt).scalars().all()

        if result:
            statement = delete(t_issues).filter_by(book_no=book_id)
            session.execute(statement)
            success = QMessageBox()
            success.setText("Book Returned")
            success.setWindowTitle("Successful")
            success.setIcon(QMessageBox.Icon.Information)
            success.setStandardButtons(QMessageBox.StandardButton.Ok)
            success = success.exec()
            if success == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
        else:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Book Not issued.")
            error.setIcon(QMessageBox.Icon.Critical)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                self.book_no.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    return_books = Return()
    return_books.show()
    sys.exit(app.exec())


