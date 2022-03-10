from PySide6.QtWidgets import QDialog
import delete_ui

class Delete(QDialog, delete_ui.Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

    def show_ui(self, id_type: str, func):
        self.label.setText(f"{id_type} No")
        self.delete_btn.clicked.connect(func)
        self.show()

        
