import os
import sys
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
class ScrollableButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the scrollable area

        # Create buttons and add them to the layout

        # Set the layout for the widget
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
        self.parentlayout.setVerticalSpacing(40)
        self.groupBox = QGroupBox()
        button_widget = ScrollableButtonWidget()
        super(Screen2,self).__init__()
        uic.loadUi(os.path.join(basedir, "cal2.ui"), self)
        self.button1 = self.findChild(QPushButton, "button")
        self.lineedit1 = self.findChild(QLineEdit, "lineEdit")
        self.lineedit1.returnPressed.connect(self.settext)
        self.label1 = self.findChild(QLabel, "label")
        self.button1.clicked.connect(self.gotoscreen1)
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
    def settext(self):
        global v
        self.button_group = QButtonGroup(self)
        global value
        global eventlist
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
            self.button_group.addButton(eventlist[value],v)
            self.parentlayout.addWidget(eventlist[value], i, j*2-1)
            j += 1
            self.groupBox.setLayout(self.parentlayout)
            self.scrollarea = self.findChild(QScrollArea, "scrollArea")
            self.scrollarea.setWidgetResizable(True)
            self.scrollarea.setWidget(self.groupBox)
            if j==3:
                i += 1
                j = 1
            print(i)
            self.button_group.buttonClicked.connect(lambda: self.showDeleteButton(c))
    def showDeleteButton(self):
        # Create a delete
        button = self.button_group.id(button)
        delete_button = QPushButton('Delete')
        delete_button.clicked.connect(lambda: self.deleteButtonClicked(x, button, delete_button))

        # Find the position of the clicked button in the grid layout
        position = [i, j]

        # Create a layout for the delete button

        # Add the delete button layout next to the clicked button in the grid layout
        self.parentlayout.addWidget(delete_button, position[0], position[1]*2)
    def deleteButtonClicked(self, x, original_button, delete_button):
        # Handle delete button click here
        print(f"Delete button clicked for {original_button.text()}")

        # Remove the delete button layout
        delete_layout = delete_button.parent().layout()
        delete_layout.removeWidget(delete_button)
        delete_button.setParent(None)
        delete_layout = original_button.parent().layout()
        delete_layout.removeWidget(original_button)
        original_button.setParent(None)
        eventlist.pop(x)
        
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