import login
import sys
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = login.Login()
    win.show()
    sys.exit(app.exec())
