# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 596)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 461, 31))

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.user = QLineEdit(self.frame_2)
        self.user.setObjectName(u"user")
        self.user.setGeometry(QRect(260, 150, 113, 22))
        self.passwd = QLineEdit(self.frame_2)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setGeometry(QRect(260, 240, 113, 22))
        self.login_btn = QPushButton(self.frame_2)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(280, 340, 111, 41))
        self.Username = QLabel(self.frame_2)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(146, 150, 91, 20))
        self.Password = QLabel(self.frame_2)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(150, 240, 91, 20))

        self.verticalLayout.addWidget(self.frame_2)

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
    # retranslateUi

