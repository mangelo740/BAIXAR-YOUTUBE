# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 220)
        MainWindow.setMinimumSize(QSize(490, 220))
        MainWindow.setMaximumSize(QSize(490, 220))
        MainWindow.setStyleSheet(u"background-color: rgb(139, 0, 0);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lyoutube = QLineEdit(self.centralwidget)
        self.lyoutube.setObjectName(u"lyoutube")
        self.lyoutube.setGeometry(QRect(20, 80, 451, 61))
        font = QFont()
        font.setPointSize(10)
        self.lyoutube.setFont(font)
        self.lyoutube.setStyleSheet(u"QLineEdit {\n"
"	Background: Black;\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"}")
        self.bdownload = QPushButton(self.centralwidget)
        self.bdownload.setObjectName(u"bdownload")
        self.bdownload.setGeometry(QRect(20, 150, 451, 51))
        font1 = QFont()
        font1.setFamily(u"Mistral")
        font1.setPointSize(20)
        self.bdownload.setFont(font1)
        self.bdownload.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255,0,0);\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255,255,0);\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(120,0,0);\n"
"	border-radius: 10px;\n"
"	color: white\n"
"}\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 451, 61))
        font2 = QFont()
        font2.setFamily(u"Mistral")
        font2.setPointSize(36)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	border-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Download - Youtube", None))
        self.bdownload.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Download - Youtube", None))
    # retranslateUi

