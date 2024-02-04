import os
import sys
import struct
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.uic import load_ui
from PyQt6.QtWidgets import *

basedir = os.path.dirname(__file__)
ownsatis = {}#saves the goal satisfaction for each day.
goalactual = {}#save the difference satisfaction in each day.
events = {}#save the events in each day.
i = 1
j = 1
c = ""
v = 0
eventlist = {}
deletelist = {}
buttonlist = []
class ScrollableButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the scrollable area

        # Create buttons and add them to the layout

        # Set the layout for the widget
def clear_layout(layout):
# Loop in reverse order to avoid indexing issues
    for i in reversed(range(layout.count())):
        item = layout.itemAt(i)
        
        # Remove the item from layout
        layout.removeItem(item)
        
        # Check if the item is a widget
        if widget := item.widget():
            # Delete the widget
            widget.deleteLater()
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(os.path.join(basedir, "cal.ui"), self)
        self.calendar = self.findChild(QCalendarWidget, "calendar")
        self.label = self.findChild(QLabel, "label")
        self.label2 = self.findChild(QLabel, "label_3")
        self.calendar.selectionChanged.connect(self.grab_date)
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button1.clicked.connect(self.gotoscreen2)
        self.button2.clicked.connect(self.gotoscreen3)
        self.button2.clicked.connect(self.gotoscreen4)
        self.scrollarea = self.findChild(QScrollArea, "scrollArea")
        self.scrollarea.setWidgetResizable(True)
        self.show()
    def gotoscreen2(self):
        widget.setCurrentIndex(1)

    def gotoscreen3(self):
        widget.setCurrentIndex(2)
    def gotoscreen4(self):
        widget.setCurrentIndex(3)
    def grab_date(self):
        dateSelected = self.calendar.selectedDate()
        self.label.setText(str(dateSelected.toString()))
class Screen3(QDialog):
    def __init__(self):
        super(Screen3,self).__init__()
        uic.loadUi(os.path.join(basedir, "cal3.ui"), self)
        self.button1 = self.findChild(QPushButton, "button")
        self.button1.clicked.connect(self.gotoscreen1)
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
class Screen4(QDialog):
    def __init__(self):
        super(Screen4,self).__init__()
class Screen2(QDialog):
    def __init__(self):
        self.parentlayout = QGridLayout()
        self.button_group = QButtonGroup()
        self.parentlayout.setVerticalSpacing(40)
        self.groupBox = QGroupBox()
        button_widget = ScrollableButtonWidget()
        super(Screen2,self).__init__()
        uic.loadUi(os.path.join(basedir, "cal2.ui"), self)
        self.button1 = self.findChild(QPushButton, "button")
        self.lineedit1 = self.findChild(QLineEdit, "lineEdit")
        self.lineedit1.returnPressed.connect(self.settext)
        self.label1 = self.findChild(QLabel, "label")
        self.deletebutton = self.findChild(QPushButton, "pushButton")
        self.button1.clicked.connect(self.gotoscreen1)
        self.deletebutton.clicked.connect(self.deleteselectedbutton)
        global deletelist
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
    def settext(self):
        global v
        global value
        global eventlist
        global buttonlist
        global i
        global j
        global c
        everyspace = 1580
        space = 70
        value = self.lineedit1.text()
        if value in eventlist:
            self.label1.setText("The event already exists!")
        else:
            self.label1.setText("")
            eventlist.update({value : QPushButton(value)})
            eventlist[value].setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                )
            eventlist[value].setFixedSize(180, 90)
            v += 1
            self.button_group.addButton(eventlist[value])
            deletelist.update({eventlist[value]: 0})
            buttonlist.append(eventlist[value])
            self.parentlayout.addWidget(eventlist[value], i, j)
            j += 1
            self.groupBox.setLayout(self.parentlayout)
            self.scrollarea = self.findChild(QScrollArea, "scrollArea")
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setWidget(self.groupBox)
            if j==3:
                i += 1
                j = 1
            self.button_group.buttonClicked.connect(self.deletebuttonfunc)
    def deletebuttonfunc(self, button):
        if deletelist[button]==0:
            button.setStyleSheet(
            "background-color: rgb(45, 45, 180);"
            "border-width: 1px;"
            "border-style: solid;"
            "border-radius: 30px;"
            "border-color: rgb(126, 150, 160);"
            )
            deletelist[button]=1
        else:
            eventlist[value].setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                )
            deletelist[button]=0
    def deleteselectedbutton(self):
        clear_layout(self.parentlayout)
        deletelist2 = []
        for button in deletelist:
            deletelist2.append(button)
            if deletelist[button] == 1:
                print("hhh", deletelist[button])
                self.button_group.removeButton(eventlist[button.text()])
                eventlist.pop(button.text())
        for button in deletelist2:
            deletelist.pop(button)
        i=0
        j=0
        for button in self.button_group.buttons():
            print("hahaha", button.text())
            self.parentlayout.addWidget(button, i, j)
            j += 1
            if j==3:
                i += 1
                j = 1
        self.groupBox.setLayout(self.parentlayout)
        self.scrollarea.setWidget(self.groupBox)
app = QApplication(sys.argv)

widget=QtWidgets.QStackedWidget()
UIWindow = UI()
screen2=Screen2()
screen3 = Screen3()
widget.addWidget(UIWindow)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.show()
app.exec()