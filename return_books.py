import sys
from PySide6.QtWidgets import QDialog, QMessageBox, QApplication, QLineEdit
from sqlalchemy.sql.expression import delete, select
from backend import t_issues, session
import return_ui


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
            session.commit()
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


