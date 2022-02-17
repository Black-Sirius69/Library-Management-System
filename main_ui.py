# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QPalette)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget)
import library_management_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 683)
        MainWindow.setMaximumSize(QSize(1024, 683))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1024, 683))
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.frame_2.setPalette(palette)
        self.frame_2.setStyleSheet(u"QFrame {\n"
                                   "background-image: url(:/images/back.jpeg);\n"
                                   "background-repeat: no-repeat;\n"
                                   "}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
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
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 100, 351, 61))
        self.label.setStyleSheet(u"font: 75 20pt \"Ubuntu Condensed\";\n"
                                 "background: transparent;\n"
                                 "gridline-color: rgb(255, 255, 255);\n"
                                 "color: rgb(255, 255, 255);")
        self.add_book.raise_()
        self.issue_book.raise_()
        self.return_book.raise_()
        self.logout_btn.raise_()
        self.add_student.raise_()
        self.search.raise_()
        self.label.raise_()

        self.vboxLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.issue_book.setText(QCoreApplication.translate("MainWindow", u"Issue AddBooks", None))
        self.return_book.setText(QCoreApplication.translate("MainWindow", u"Return AddBooks", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.add_book.setText(QCoreApplication.translate("MainWindow", u"Add AddBooks", None))
        self.add_student.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.search.setText("")
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"Library Mangement Program", None))  # retranslateUi
