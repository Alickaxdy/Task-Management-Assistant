import os
import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.uic import load_ui
from PyQt6.QtWidgets import *
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("cal.ui", self)
        self.calendar = self.findChild(QCalendarWidget, "calendar")
        self.label = self.findChild(QLabel, "label")
        self.calendar.selectionChanged.connect(self.grab_date)
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button1.clicked.connect(self.gotoscreen2)
        self.show()
    def gotoscreen2(self):
        widget.setCurrentIndex(1)
    def grab_date(self):
        dateSelected = self.calendar.selectedDate()
        self.label.setText(str(dateSelected.toString()))
class Screen2(QDialog):
    def __init__(self):
        super(Screen2,self).__init__()
        uic.loadUi("cal2.ui",self)
        self.button1 = self.findChild(QPushButton, "button")
        self.button1.clicked.connect(self.gotoscreen1)
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
app = QApplication(sys.argv)

widget=QtWidgets.QStackedWidget()
UIWindow = UI()
screen2=Screen2()
widget.addWidget(UIWindow)
widget.addWidget(screen2)
widget.show()
app.exec()