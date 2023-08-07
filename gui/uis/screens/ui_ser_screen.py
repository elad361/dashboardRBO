# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ser_screengXIdxn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_serScreen(QWidget):
    def __init__(
        self,
        copyright,
        version,
        bg_two,
        font_family,
        text_size,
        text_description_color,
        radius = 8,
        padding = 10
    ):
        super().__init__()

        # PROPERTIES
        self._copyright = copyright
        self._version = version
        self._bg_two = bg_two
        self._font_family = font_family
        self._text_size = text_size
        self._text_description_color = text_description_color
        self._radius = radius
        self._padding = padding

        # SETUP UI
        self.setupUi()



    def setupUi(self):
        serScreen = self
        if not serScreen.objectName():
            serScreen.setObjectName(u"serScreen")
        serScreen.resize(819, 512)
        self.gridLayout_2 = QGridLayout(serScreen)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(serScreen)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.textEdit_3 = QTextEdit(serScreen)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.gridLayout.addWidget(self.textEdit_3, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 4, 4)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(serScreen)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_6 = QLabel(serScreen)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBox_1 = QComboBox(serScreen)
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.setObjectName(u"comboBox_1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox_1)

        self.label_7 = QLabel(serScreen)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.comboBox_2 = QComboBox(serScreen)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox_2)

        self.label_11 = QLabel(serScreen)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_11)

        self.pushButton_4 = QPushButton(serScreen)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pushButton_4)

        self.comboBox = QComboBox(serScreen)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox)

        self.label_12 = QLabel(serScreen)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)


        self.gridLayout_2.addLayout(self.formLayout, 0, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(serScreen)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(serScreen)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(serScreen)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(serScreen)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.progressBar = QProgressBar(serScreen)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.textEdit = QTextEdit(serScreen)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 4, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(serScreen)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(serScreen)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_5)


        self.gridLayout_2.addLayout(self.formLayout_2, 2, 4, 2, 1)

        self.label_9 = QLabel(serScreen)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)

        self.textEdit_2 = QTextEdit(serScreen)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_2.addWidget(self.textEdit_2, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(serScreen)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 4, 2, 1, 1)

        self.pushButton_5 = QPushButton(serScreen)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 4, 3, 1, 1)

        self.label = QLabel(serScreen)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 4, 4, 1, 1)


        self.retranslateUi(serScreen)

        QMetaObject.connectSlotsByName(serScreen)
    # setupUi

    def retranslateUi(self, serScreen):
        serScreen.setWindowTitle(QCoreApplication.translate("serScreen", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("serScreen", u"Gathering / Sending Data (Rx/Tx)", None))
        self.label_2.setText(QCoreApplication.translate("serScreen", u"PORT Name:", None))
        self.label_6.setText(QCoreApplication.translate("serScreen", u"Baud Rate:", None))
        self.comboBox_1.setItemText(0, QCoreApplication.translate("serScreen", u"Select...", None))
        self.comboBox_1.setItemText(1, QCoreApplication.translate("serScreen", u"1200", None))
        self.comboBox_1.setItemText(2, QCoreApplication.translate("serScreen", u"2400", None))
        self.comboBox_1.setItemText(3, QCoreApplication.translate("serScreen", u"4800", None))
        self.comboBox_1.setItemText(4, QCoreApplication.translate("serScreen", u"9600", None))
        self.comboBox_1.setItemText(5, QCoreApplication.translate("serScreen", u"19200", None))
        self.comboBox_1.setItemText(6, QCoreApplication.translate("serScreen", u"38400", None))
        self.comboBox_1.setItemText(7, QCoreApplication.translate("serScreen", u"57600", None))
        self.comboBox_1.setItemText(8, QCoreApplication.translate("serScreen", u"115200", None))

        self.label_7.setText(QCoreApplication.translate("serScreen", u"Length (B):", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("serScreen", u"Select...", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("serScreen", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("serScreen", u"4", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("serScreen", u"8", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("serScreen", u"16", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("serScreen", u"32", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("serScreen", u"64", None))

        self.label_11.setText(QCoreApplication.translate("serScreen", u"-", None))
        self.pushButton_4.setText(QCoreApplication.translate("serScreen", u"Save", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("serScreen", u"Select...", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("serScreen", u"0", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("serScreen", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("serScreen", u"4", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("serScreen", u"6", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("serScreen", u"8", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("serScreen", u"10", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("serScreen", u"15", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("serScreen", u"20", None))

        self.label_12.setText(QCoreApplication.translate("serScreen", u"Timelimit", None))
        self.label_10.setText(QCoreApplication.translate("serScreen", u"Connection Options:", None))
        self.pushButton_2.setText(QCoreApplication.translate("serScreen", u"STOP", None))
        self.pushButton.setText(QCoreApplication.translate("serScreen", u"START", None))
        self.label_8.setText(QCoreApplication.translate("serScreen", u"Connection Percentage Status:", None))
        self.label_4.setText(QCoreApplication.translate("serScreen", u"Port Status", None))
        self.label_5.setText(QCoreApplication.translate("serScreen", u"Not Connected", None))
        self.label_9.setText(QCoreApplication.translate("serScreen", u"Send DATA:", None))
        self.pushButton_3.setText(QCoreApplication.translate("serScreen", u"SEND", None))
        self.pushButton_5.setText(QCoreApplication.translate("serScreen", u"Save as .txt", None))
        self.label.setText(QCoreApplication.translate("serScreen", u"github.com/mcagriaksoy", None))
    # retranslateUi

