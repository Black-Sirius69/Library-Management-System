# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import library_management_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: url(:/images/back.jpeg);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.issue_book = QPushButton(self.frame_2)
        self.issue_book.setObjectName(u"issue_book")
        self.issue_book.setGeometry(QRect(330, 240, 111, 31))
        self.issue_book.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.return_book = QPushButton(self.frame_2)
        self.return_book.setObjectName(u"return_book")
        self.return_book.setGeometry(QRect(540, 240, 111, 31))
        self.return_book.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.logout_btn = QPushButton(self.frame_2)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setGeometry(QRect(430, 360, 111, 31))
        self.logout_btn.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.add_book = QPushButton(self.frame_2)
        self.add_book.setObjectName(u"add_book")
        self.add_book.setGeometry(QRect(330, 300, 111, 31))
        self.add_book.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.add_student = QPushButton(self.frame_2)
        self.add_student.setObjectName(u"add_student")
        self.add_student.setGeometry(QRect(540, 300, 111, 31))
        self.add_student.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.search = QLineEdit(self.frame_2)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(330, 180, 321, 31))
        self.search.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(290, 340, 86, 25))
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 110, 291, 61))
        self.label.setStyleSheet(u"font: 75 20pt \"Ubuntu Condensed\";\n"
"background: transparent;\n"
"gridline-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.issue_book.setText(QCoreApplication.translate("MainWindow", u"Issue Books", None))
        self.return_book.setText(QCoreApplication.translate("MainWindow", u"Return Books", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.add_book.setText(QCoreApplication.translate("MainWindow", u"Add Books", None))
        self.add_student.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.search.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Library Mangement Program", None))
    # retranslateUi

