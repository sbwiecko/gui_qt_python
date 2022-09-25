# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(355, 357)
        Form.setStyleSheet(u"background-color: rgb(20,20,20); /*background*/\n"
"color: rgb(220,220,220);         /*font color*/\n"
"font-size: 20 px;                /*font size*/")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setStyleSheet(u"border: none;                           /*no border*/\n"
"border-bottom: 2px solid rgb(30,30,30); /*add border bottom*/\n"
"padding: 0 8px;                         /*no vertical padding, only horizontal*/\n"
"font-size: 24px;                        /*font size*/\n"
"font-weight: bold;                      /*font weight*/")
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(48, 48))
        self.pushButton.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton.setFlat(True)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(48, 48))
        self.pushButton_2.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"background-color: \"#1e1e2d\";")
        self.pushButton_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(48, 48))
        self.pushButton_6.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_6.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(48, 48))
        self.pushButton_5.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_5.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(48, 48))
        self.pushButton_4.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_4.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_4, 2, 2, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(48, 48))
        self.pushButton_3.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"background-color: \"#1e1e2d\";")
        self.pushButton_3.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_3, 2, 3, 1, 1)

        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(48, 48))
        self.pushButton_10.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_10.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(48, 48))
        self.pushButton_8.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_8.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(48, 48))
        self.pushButton_9.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_9.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(48, 48))
        self.pushButton_7.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"background-color: \"#1e1e2d\";")
        self.pushButton_7.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_7, 3, 3, 1, 1)

        self.pushButton_11 = QPushButton(Form)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(48, 48))
        self.pushButton_11.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_11, 4, 0, 1, 1)

        self.pushButton_13 = QPushButton(Form)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QSize(48, 48))
        self.pushButton_13.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_13.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_13, 4, 1, 1, 1)

        self.pushButton_14 = QPushButton(Form)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QSize(48, 48))
        self.pushButton_14.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_14.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_14, 4, 2, 1, 1)

        self.pushButton_12 = QPushButton(Form)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QSize(48, 48))
        self.pushButton_12.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"background-color: \"#1e1e2d\";")
        self.pushButton_12.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_12, 4, 3, 1, 1)

        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QSize(48, 48))
        self.pushButton_17.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_17.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_17, 5, 0, 1, 2)

        self.pushButton_15 = QPushButton(Form)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QSize(48, 48))
        self.pushButton_15.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"")
        self.pushButton_15.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_15, 5, 2, 1, 1)

        self.pushButton_18 = QPushButton(Form)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QSize(48, 48))
        self.pushButton_18.setStyleSheet(u"border: none; /*no border*/\n"
"font: bold;   /*font weight*/\n"
"background-color: #f31d58;")
        self.pushButton_18.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_18, 5, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"C", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

