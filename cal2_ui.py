# Form implementation generated from reading ui file '/Users/mj/Desktop/Task-Management-Assistant/cal2.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1680, 1050)
        Dialog.setStyleSheet("color: rgb(70, 255, 153);\n"
"background-color: rgb(85, 170, 255);")
        self.button = QtWidgets.QPushButton(parent=Dialog)
        self.button.setGeometry(QtCore.QRect(1350, 740, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Charter")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setStyleSheet("* {background-color: rgb(173, 221, 231);\n"
"color: rgb(34, 137, 146);\n"
"border-width: 9px;\n"
"border-style: solid;\n"
"border-radius: 25px;\n"
"border-color: rgb(173, 221, 231);\n"
"}")
        self.button.setObjectName("button")
        self.scrollArea = QtWidgets.QScrollArea(parent=Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(60, 40, 1551, 381))
        self.scrollArea.setStyleSheet("* {background-color: rgb(173, 221, 231);\n"
"border-width: 12px;\n"
"border-style: solid;\n"
"border-radius: 40px;\n"
"border-color: rgb(173, 221, 231);\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background-color: rgb(88, 182, 255);\n"
"    width: 16px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 8px;\n"
"}\n"
"/* Handle Bar Vertical*/\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(98, 161, 232);\n"
"    min-height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(173, 244, 179);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(128, 217, 129);\n"
"}\n"
"/*button top scrollbar*/\n"
"QScrollBar::sub-line:vertical{\n"
"    border: none;\n"
"    background-color:  rgb(110, 248, 243);\n"
"    height: 15;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: rgb(0, 161, 118);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color: rgb(0, 140, 103);\n"
"}\n"
"\n"
"/*button bottom  scrollbar*/\n"
"QScrollBar::add-line:vertical{\n"
"    border: none;\n"
"    background-color:  rgb(110, 248, 243);\n"
"    height: 15;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color: rgb(0, 161, 118);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background-color: rgb(0, 140, 103);\n"
"}\n"
"/*Reset Arrow*/\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background-color: rgb(225, 215, 222);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background-color: rgb(0, 239, 115);\n"
"    margin: 0px 15 0px 15;\n"
"    hieght: 14px;\n"
"}\n"
"/* Handle Bar Horizontal*/\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(0, 189, 95);\n"
"    min-width: 30px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(0, 161, 118);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgb(0, 140, 103);\n"
"}\n"
"/*button top scrollbar*/\n"
"QScrollBar::sub-line:horizontal{\n"
"    border: none;\n"
"    background-color:  rgb(0, 239, 115);\n"
"    width: 15;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    background-color: rgb(0, 161, 118);\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    background-color: rgb(0, 140, 103);\n"
"}\n"
"/*button bottom  scrollbar*/\n"
"QScrollBar::add-line:horizontal{\n"
"    border: none;\n"
"    background-color:  rgb(0, 239, 115);\n"
"    width: 15;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    background-color: rgb(0, 161, 118);\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"    background-color: rgb(0, 140, 103);\n"
"}\n"
"/*Reset Arrow*/\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background-color: rgb(0, 207, 152);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1527, 524))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=self.scrollAreaWidgetContents)
        self.widget.setMinimumSize(QtCore.QSize(0, 500))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button.setText(_translate("Dialog", "DONE!"))
