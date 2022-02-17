# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 294)
        MainWindow.setMaximumSize(QSize(474, 294))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 60, 211, 41))
        self.label.setStyleSheet(u"")
        self.login_btn = QPushButton(self.centralwidget)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(270, 230, 111, 31))
        self.user = QLineEdit(self.centralwidget)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(340, 130, 113, 22))
        self.Username = QLabel(self.centralwidget)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(220, 130, 91, 20))
        self.passwd = QLineEdit(self.centralwidget)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setGeometry(QRect(340, 180, 113, 22))
        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(220, 180, 91, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 161, 151))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/images/logo.png"))
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Library Mangement Program", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.Username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.Password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_2.setText("")  # retranslateUi
