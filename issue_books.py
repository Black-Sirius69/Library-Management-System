import sys
import dateutil.parser as dparser
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QApplication, QMainWindow
from sqlalchemy import (Column, Date, Integer, String, Table,
                        create_engine, insert, select)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import issue_ui

Base = automap_base()
engine = create_engine("mysql://vedant:vedant@localhost/library_management")
t_loan = Table(
    "loans",
    Base.metadata,
    Column("book_no", String(50), nullable=False),
    Column("student_id", Integer, nullable=False),
    Column("issue_date", Date),
    Column("return_date", Date),
)
Base.prepare(engine, reflect=True)
Book = Base.classes.books
Student = Base.classes.students


session = Session(engine)


class Issue(QMainWindow, issue_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.issue_date.setDate(QDate.currentDate())
        self.ret_date.setDate(QDate.currentDate().addDays(6))
        self.issue_book.clicked.connect(self.issue)

    def issue(self):
        student_id = int(self.stu_no.text())
        book_id = self.book_no.text()

        # Validate Student and Book
        statement = select(Student).filter_by(admno=student_id)
        result = session.execute(statement).scalars().all()
        if result:
            print("Found Student")
        else:
            print("Student Not Found")

        iss_date = dparser.parse(
            self.issue_date.text(), fuzzy=True, ignoretz=True).date()
        return_date = dparser.parse(
            self.issue_date.text(), fuzzy=True, ignoretz=True).date()

        try:
            stmt = insert(t_loan).values(
                book_no=book_id, student_id=student_id, issue_date=iss_date, return_date=return_date)
            result = session.execute(stmt)
            session.commit()
        except IntegrityError:
            session.rollback()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Issue()
    win.show()
    sys.exit(app.exec())
