# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'return.ui'
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
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.home_page = QPushButton(Dialog)
        self.home_page.setObjectName(u"home_page")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.home_page)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.book_no = QLineEdit(Dialog)
        self.book_no.setObjectName(u"book_no")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.book_no)

        self.return_book = QPushButton(Dialog)
        self.return_book.setObjectName(u"return_book")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.return_book)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.home_page.setText(QCoreApplication.translate("Dialog", u"Go Back", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Book no", None))
        self.return_book.setText(QCoreApplication.translate("Dialog", u"Return Book", None))
    # retranslateUi

