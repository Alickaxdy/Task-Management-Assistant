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
restbutton = []
def clear_and_delete_buttons_from_group(button_group):
    for button in button_group.buttons():
        button_group.removeButton(button)
        button.deleteLater()
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
        global parentlayout
        global i
        global j
        parentlayout = QGridLayout()
        global button_group
        button_group = QButtonGroup()
        parentlayout.setVerticalSpacing(40)
        global groupBox
        groupBox = QGroupBox()
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
        self.scrollarea = self.findChild(QScrollArea, "scrollArea")
        global deletelist
        button_group.buttonClicked.connect(self.deletebuttonfunc)
        
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
    def settext(self):
        global i
        global j
        global v
        global value
        global eventlist
        global buttonlist
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
            button_group.addButton(eventlist[value])
            deletelist.update({eventlist[value]: 0})
            buttonlist.append(eventlist[value])
            parentlayout.addWidget(eventlist[value], i, j)
            j += 1
            groupBox.update()  # Refresh groupBox display
            groupBox.setLayout(parentlayout)
            self.scrollarea.update()  # Refresh scroll area display
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setWidget(groupBox)
            if j==3:
                i += 1
                j = 1
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
            button.setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                )
            deletelist[button]=0
    def deleteselectedbutton(self):
        global i
        global j
        i=1
        j=1
        groupBox.update()  # Refresh groupBox display
        self.scrollarea.update()  # Refresh scroll area display
        clear_layout(parentlayout)
        deletelist2 = []
        for button in deletelist:
            print("hhh", deletelist[button])
            if deletelist[button] == 1:
                deletelist2.append(button)
                button_group.removeButton(button)
        x=0
        for button in button_group.buttons():
            #print("hahaha", button in deletelist, button.text())
            restbutton.append(button.text())
        deletelist.clear()
        eventlist.clear()
        clear_and_delete_buttons_from_group(button_group)
        for button in restbutton:
            x+=1
            print("kuaile", x)
            self.buttt = QPushButton(button)
            self.buttt.setFixedSize(180, 90)
            self.buttt.setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                )
            eventlist.update({self.buttt.text() : self.buttt})
            button_group.addButton(self.buttt)
            deletelist.update({self.buttt: 0})
            buttonlist.append(self.buttt)
            parentlayout.addWidget(self.buttt, i, j)
            j += 1
            if j==3:
                i += 1
                j = 1
            groupBox.setLayout(parentlayout)
            self.scrollarea.update()  # Refresh scroll area display
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setWidget(groupBox)
        restbutton.clear()
        
        
        
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