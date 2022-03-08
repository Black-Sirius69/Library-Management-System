# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'issue.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.issue_date = QDateEdit(self.centralwidget)
        self.issue_date.setObjectName(u"issue_date")
        self.issue_date.setCalendarPopup(True)

        self.gridLayout.addWidget(self.issue_date, 3, 1, 1, 1)

        self.ret_date = QDateEdit(self.centralwidget)
        self.ret_date.setObjectName(u"ret_date")
        self.ret_date.setCalendarPopup(True)

        self.gridLayout.addWidget(self.ret_date, 4, 1, 1, 1)

        self.stu_no = QLineEdit(self.centralwidget)
        self.stu_no.setObjectName(u"stu_no")

        self.gridLayout.addWidget(self.stu_no, 1, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.book_no = QLineEdit(self.centralwidget)
        self.book_no.setObjectName(u"book_no")

        self.gridLayout.addWidget(self.book_no, 2, 1, 1, 1)

        self.issue_book = QPushButton(self.centralwidget)
        self.issue_book.setObjectName(u"issue_book")

        self.gridLayout.addWidget(self.issue_book, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.stu_no, self.book_no)
        QWidget.setTabOrder(self.book_no, self.issue_date)
        QWidget.setTabOrder(self.issue_date, self.ret_date)
        QWidget.setTabOrder(self.ret_date, self.issue_book)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Book No.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Issue A Book", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Return Date", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Student No.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Issue Date", None))
        self.issue_book.setText(QCoreApplication.translate("MainWindow", u"Issue book", None))
    # retranslateUi

