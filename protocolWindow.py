# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'protocolWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form,Server):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(396, 300)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 20, 61, 20))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(230, 20, 61, 21))
        self.pushButton.setCheckable(True)
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 120, 381, 171))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 71, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 54, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 80, 121, 16))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 80, 71, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 80, 61, 16))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)
        self.lineEdit.textEdited.connect(Form.slot_set_port)
        self.pushButton.clicked.connect(Form.solt_server_state)
        Server.client_signal.connect(Form.show_client_info)
        Server.data_signal.connect(Form.show_client_data)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"9980", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"START", None))
        self.label.setText(QCoreApplication.translate("Form", u"Local Port:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Client IP:", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Client Port:", None))
        self.label_5.setText("")
    # retranslateUi

