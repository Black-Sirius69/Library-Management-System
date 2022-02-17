# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFormLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(657, 408)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.cls = QLineEdit(self.centralwidget)
        self.cls.setObjectName(u"cls")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cls)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.section = QLineEdit(self.centralwidget)
        self.section.setObjectName(u"section")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.section)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.age = QLineEdit(self.centralwidget)
        self.age.setObjectName(u"age")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.age)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.gender = QLineEdit(self.centralwidget)
        self.gender.setObjectName(u"gender")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.gender)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.admno = QLineEdit(self.centralwidget)
        self.admno.setObjectName(u"admno")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.admno)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.address = QLineEdit(self.centralwidget)
        self.address.setObjectName(u"address")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.address)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.phone = QLineEdit(self.centralwidget)
        self.phone.setObjectName(u"phone")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.phone)

        self.import_data = QPushButton(self.centralwidget)
        self.import_data.setObjectName(u"import_data")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.import_data)

        self.add_data = QPushButton(self.centralwidget)
        self.add_data.setObjectName(u"add_data")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.add_data)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_9)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Section", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Admission no.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.import_data.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.add_data.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"Student Registration Form", None))  # retranslateUi
