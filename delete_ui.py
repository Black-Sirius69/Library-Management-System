# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.delete_btn = QPushButton(Dialog)
        self.delete_btn.setObjectName(u"delete_btn")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.delete_btn)

        self.id = QLineEdit(Dialog)
        self.id.setObjectName(u"id")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.id)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.go_home = QPushButton(Dialog)
        self.go_home.setObjectName(u"go_home")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.go_home)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.delete_btn.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.go_home.setText(QCoreApplication.translate("Dialog", u"Go Back", None))
    # retranslateUi

