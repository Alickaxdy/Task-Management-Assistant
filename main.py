import os
import sys
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("cal.ui", self)
        self.calendar = self.findChild(QCalendarWidget, "calendar")
        self.label = self.findChild(QLabel, "label")
        self.calendar.selectionChanged.connect(self.grab_date)
        self.show()
    def grab_date(self):
        dateSelected = self.calendar.selectedDate()
        self.label.setText(str(dateSelected.toString()))
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()