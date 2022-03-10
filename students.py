import sys

import sqlalchemy
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QLineEdit
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import students_ui
import delete


Base = automap_base()

#  set the sqlalchemy engine to mysql server and connect
engine = sqlalchemy.create_engine(
    "mysql://vedant:vedant@localhost/library_management")

# Reflect tables
Base.prepare(engine, reflect=True)

Students = Base.classes.students

session = Session(engine)


class Student(QMainWindow, students_ui.Ui_MainWindow):
    def __init__(self):
        super(Student, self).__init__()
        self.setupUi(self)
        self.delete_ui = delete.Delete()
        self.add_data.clicked.connect(self.add)
        self.setWindowTitle("Cerebrum - Add Students")
        self.delete_btn.clicked.connect(lambda : self.delete_ui.show_ui("Admission", self.delete_func))

    def add(self):
        try:
            name = self.name.text() if self.name.text() != '' else None
            age = int(self.age.text()) if self.name.text() != '' else None
            cls = int(self.cls.text()) if self.name.text() != '' else None
            section = self.section.text() if self.name.text() != '' else None
            gender = self.gender.text() if self.name.text() != '' else None
            admno = int(self.admno.text()) if self.name.text() != '' else None
            student = Students(Name=name, Admno=admno, Age=age, Class=cls, Gender=gender, Section=section)
            session.add(student)
            session.commit()

            success = QMessageBox()
            success.setText("Data Added")
            success.setWindowTitle("Successful")
            success.setStandardButtons(QMessageBox.StandardButton.Ok)
            success = success.exec()
            if success == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
        except IntegrityError:
            error = QMessageBox()
            error.setText(f"Could Not add data. Duplicate accession number {self.admno.text()}.")
            error.setWindowTitle("Error")
            error.setStandardButtons(QMessageBox.StandardButton.Ok)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
            session.rollback()
        except SQLAlchemyError as e:
            print(e)
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Could not add data")
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                for widget in self.findChildren(QLineEdit):
                    widget.clear()
            session.rollback()
    
    def delete_func(self):
        id = int(self.delete_ui.id.text()) if self.delete_ui.id.text() != '' else None

        # Check if student is present
        stmt = sqlalchemy.select(Students).filter_by(Admno=id)
        result = session.execute(stmt).scalars().all()
        if result:
            stmt = sqlalchemy.delete(Students).filter_by(Admno=id)
            session.execute(stmt)
            session.commit()
            success = QMessageBox()
            success.setText("Student Record deleted")
            success.setWindowTitle("Successful")
            success.setIcon(QMessageBox.Icon.Information)
            success.setStandardButtons(QMessageBox.StandardButton.Ok)
            success = success.exec()
            self.delete_ui.id.clear()
        else :
            error = QMessageBox()
            error.setText("Student not found")
            error.setWindowTitle("Error")
            error.setIcon(QMessageBox.Icon.Critical)
            error = error.exec()
            if error == QMessageBox.StandardButton.Ok:
                self.delete_ui.id.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Student()
    win.show()
    sys.exit(app.exec())
