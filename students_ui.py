# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 434)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.home_page = QPushButton(self.centralwidget)
        self.home_page.setObjectName(u"home_page")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.home_page)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.label_9)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.cls = QLineEdit(self.centralwidget)
        self.cls.setObjectName(u"cls")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.cls)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.section = QLineEdit(self.centralwidget)
        self.section.setObjectName(u"section")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.section)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.age = QLineEdit(self.centralwidget)
        self.age.setObjectName(u"age")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.age)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.gender = QLineEdit(self.centralwidget)
        self.gender.setObjectName(u"gender")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.gender)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_6)

        self.admno = QLineEdit(self.centralwidget)
        self.admno.setObjectName(u"admno")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.admno)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.delete_btn)

        self.add_data = QPushButton(self.centralwidget)
        self.add_data.setObjectName(u"add_data")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.add_data)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.home_page.setText(QCoreApplication.translate("MainWindow", u"Go Back", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Registration Form", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Admission no.", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete  Student", None))
        self.add_data.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

