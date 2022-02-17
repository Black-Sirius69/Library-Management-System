import sys

import sqlalchemy
from PySide6.QtWidgets import QMainWindow, QApplication
from sqlalchemy.ext.automap import automap_base

import student_ui

Base = automap_base()

#  set the sqlalchemy engine to mysql server and connect
engine = sqlalchemy.create_engine(
    "mysql://vedant:vedant@localhost/library_management")

# Reflect tables
Base.prepare(engine, reflect=True)

students = Base.classes.students


class Student(QMainWindow, student_ui.Ui_MainWindow):
    def __init__(self):
        super(Student, self).__init__()
        self.setupUi(self)
        self.add_data.clicked.connect(self.add)
        self.setWindowTitle("Cerebrum - Add Students")

    def add(self):
        try:
            pass
        except Exception:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Student()
    win.show()
    sys.exit(app.exec())
