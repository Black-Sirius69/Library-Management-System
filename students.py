import sys

import sqlalchemy
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit, QFileDialog
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd

import student_ui

Base = automap_base()

#  set the sqlalchemy engine to mysql server and connect
engine = sqlalchemy.create_engine(
    "mysql://vedant:vedant@localhost/library_management")

# Reflect tables
Base.prepare(engine, reflect=True)

Students = Base.classes.students

session = Session(engine)


class Student(QMainWindow, student_ui.Ui_MainWindow):
    def __init__(self):
        super(Student, self).__init__()
        self.setupUi(self)
        self.add_data.clicked.connect(self.add)
        self.setWindowTitle("Cerebrum - Add Students")
        # self.import_data.clicked.connect(self.import_student)

    def add(self):
        try:
            name = self.name.text() if self.name.text() != '' else None
            age = self.age.text() if self.name.text() != '' else None
            cls = self.cls.text() if self.name.text() != '' else None
            section = self.section.text() if self.name.text() != '' else None
            gender = self.gender.text() if self.name.text() != '' else None
            address = self.address.text() if self.name.text() != '' else None
            phone = self.phone.text() if self.name.text() != '' else None
            admno = self.admno.text() if self.name.text() != '' else None
            student = Students(Name=name, admno=admno, age=age, cls=cls, gender=gender, section=section,
                               address=address,
                               phone=phone)
            session.add(student)
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
            error.setText(f"Could Not add data. Duplicate accession number {self.admno.text()}.")
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Icon.Critical)
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
            session.rollback()
        except SQLAlchemyError as e:
            print(e)
            error = QMessageBox()
            error.about(self, "Error", "Could not add data")
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
            session.rollback()

session.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Student()
    win.show()
    sys.exit(app.exec())
