# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'books.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 582)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.acc_no = QLineEdit(self.centralwidget)
        self.acc_no.setObjectName(u"acc_no")

        self.gridLayout.addWidget(self.acc_no, 5, 2, 1, 1)

        self.author_2 = QLineEdit(self.centralwidget)
        self.author_2.setObjectName(u"author_2")

        self.gridLayout.addWidget(self.author_2, 4, 2, 1, 1)

        self.edition = QLineEdit(self.centralwidget)
        self.edition.setObjectName(u"edition")

        self.gridLayout.addWidget(self.edition, 12, 2, 1, 1)

        self.copies = QLineEdit(self.centralwidget)
        self.copies.setObjectName(u"copies")

        self.gridLayout.addWidget(self.copies, 13, 2, 1, 1)

        self.isbn = QLineEdit(self.centralwidget)
        self.isbn.setObjectName(u"isbn")

        self.gridLayout.addWidget(self.isbn, 6, 2, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.title = QLineEdit(self.centralwidget)
        self.title.setObjectName(u"title")

        self.gridLayout.addWidget(self.title, 2, 2, 1, 1)

        self.class_number = QLineEdit(self.centralwidget)
        self.class_number.setObjectName(u"class_number")

        self.gridLayout.addWidget(self.class_number, 10, 2, 1, 1)

        self.publisher = QLineEdit(self.centralwidget)
        self.publisher.setObjectName(u"publisher")

        self.gridLayout.addWidget(self.publisher, 8, 2, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)

        self.add_data = QPushButton(self.centralwidget)
        self.add_data.setObjectName(u"add_data")

        self.gridLayout.addWidget(self.add_data, 15, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.call_number = QLineEdit(self.centralwidget)
        self.call_number.setObjectName(u"call_number")

        self.gridLayout.addWidget(self.call_number, 11, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 10, 0, 1, 1)

        self.year_of_publication = QLineEdit(self.centralwidget)
        self.year_of_publication.setObjectName(u"year_of_publication")

        self.gridLayout.addWidget(self.year_of_publication, 9, 2, 1, 1)

        self.subject = QLineEdit(self.centralwidget)
        self.subject.setObjectName(u"subject")

        self.gridLayout.addWidget(self.subject, 7, 2, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 1, 1, 2)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 13, 0, 1, 1)

        self.author_1 = QLineEdit(self.centralwidget)
        self.author_1.setObjectName(u"author_1")

        self.gridLayout.addWidget(self.author_1, 3, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.home_page = QPushButton(self.centralwidget)
        self.home_page.setObjectName(u"home_page")

        self.gridLayout.addWidget(self.home_page, 0, 0, 1, 1)

        self.delete_2 = QPushButton(self.centralwidget)
        self.delete_2.setObjectName(u"delete_2")

        self.gridLayout.addWidget(self.delete_2, 15, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.title, self.author_1)
        QWidget.setTabOrder(self.author_1, self.author_2)
        QWidget.setTabOrder(self.author_2, self.acc_no)
        QWidget.setTabOrder(self.acc_no, self.isbn)
        QWidget.setTabOrder(self.isbn, self.subject)
        QWidget.setTabOrder(self.subject, self.publisher)
        QWidget.setTabOrder(self.publisher, self.year_of_publication)
        QWidget.setTabOrder(self.year_of_publication, self.class_number)
        QWidget.setTabOrder(self.class_number, self.call_number)
        QWidget.setTabOrder(self.call_number, self.edition)
        QWidget.setTabOrder(self.edition, self.copies)
        QWidget.setTabOrder(self.copies, self.add_data)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Year of Publication", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ISBN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Author2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Edition", None))
        self.add_data.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Author1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Class Number", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Call Number", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Book Entry Form", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Copies", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Acc. No", None))
        self.home_page.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"Delete Book", None))
    # retranslateUi

