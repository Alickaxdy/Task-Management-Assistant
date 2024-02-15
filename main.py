import os
import sys
import struct
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.uic import load_ui
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer

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
        self.button3.clicked.connect(self.gotoscreen4)
        self.scrollarea = self.findChild(QScrollArea, "scrollArea")
        self.scrollarea.setWidgetResizable(True)
        self.show()
    def grab_date(self):
        dateSelected = self.calendar.selectedDate()
        self.label.setText(str(dateSelected.toString()))
    def gotoscreen2(self):
        widget.setCurrentIndex(1)

    def gotoscreen3(self):
        widget.setCurrentIndex(2)
    def gotoscreen4(self):
        widget.setCurrentIndex(3)
        global scrollarea2
        global parentlayout
        global groupBox2
        global select_button
        print(parentlayout.count())
        global parentlayout2
        parentlayout2 = QGridLayout()
        global button_group2
        parentlayout2.setVerticalSpacing(40)
        global groupBox2
        groupBox2 = QGroupBox()
        new_widget = QWidget()
        parentlayout2 = QGridLayout(new_widget)
        select_button = {}
        for i in range(parentlayout.count()):
            original_btn = parentlayout.itemAt(i).widget()
            self.new_btn = QPushButton(original_btn.text(), self)
            self.new_btn.setFixedSize(180,90)
            self.new_btn.setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                )
            select_button.update({self.new_btn.text() : 0})
            button_group2.addButton(self.new_btn)
            parentlayout2.addWidget(self.new_btn, int(i/2)+1,i%2+1)
        groupBox2.setLayout(parentlayout2)
        scrollarea2.setWidget(groupBox2)
class Screen3(QDialog):
    def __init__(self):
        super(Screen3,self).__init__()
        uic.loadUi(os.path.join(basedir, "cal3.ui"), self)
        self.button1 = self.findChild(QPushButton, "button")
        self.button1.clicked.connect(self.gotoscreen1)
    def gotoscreen1(self):
        widget.setCurrentIndex(0)
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
        global parentlayout
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
        global parentlayout
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
class Screen4(QDialog):
    def __init__(self):
        global scrollarea2
        global scrollarea3
        global parentlayout
        global parentlayout2
        parentlayout2 = QGridLayout()
        global button_group2
        button_group2 = QButtonGroup()
        parentlayout2.setVerticalSpacing(40)
        global groupBox2
        groupBox2 = QGroupBox()
        global combobox
        global lineedit1
        global lineedit2
        global lineedit3
        global lineedit4
        global maohao1
        global maohao2
        global labelto
        global planlist
        global preparebutton
        global currentbutton
        global addplanbutton
        global planlist
        global allplans
        global plans
        global planbutton_list
        global planbuttongroup
        global planbox
        global planlayout
        global i2
        global deleteplansbutton
        #global deleteplan
        #deleteplan = {}
        i2 = 0
        planbuttongroup = QButtonGroup()
        planlayout = QGridLayout()
        planbox = QGroupBox()
        planbutton_list = {}
        plans = [{}, {}, {}]
        allplans = []
        planlist = [[], [], []]
        currentbutton = ""
        new_widget = QWidget()
        parentlayout2 = QGridLayout(new_widget)
        super(Screen4,self).__init__()
        uic.loadUi(os.path.join(basedir, "cal4.ui"), self)
        scrollarea2 = self.findChild(QScrollArea, "scrollArea")
        scrollarea3 = self.findChild(QScrollArea, "planList")
        lineedit1 = self.findChild(QLineEdit, "lineEdit")
        lineedit2 = self.findChild(QLineEdit, "lineEdit_2")
        lineedit3 = self.findChild(QLineEdit, "lineEdit_3")
        lineedit4 = self.findChild(QLineEdit, "lineEdit_4")
        labelto = self.findChild(QLabel, "label_5")
        maohao1 = self.findChild(QLabel, "label_3")
        maohao2 = self.findChild(QLabel, "label_6")
        preparebutton = self.findChild(QPushButton, "prepareButton")
        addplanbutton = self.findChild(QPushButton, "addPlan")
        deleteplansbutton = self.findChild(QPushButton, "deleteButton")
        lineedit1.setVisible(0)
        lineedit2.setVisible(0)
        lineedit3.setVisible(0)
        lineedit4.setVisible(0)
        labelto.setVisible(0)
        maohao1.setVisible(0)
        maohao2.setVisible(0)
        combobox = self.findChild(QComboBox, "comboBox")
        combobox.currentTextChanged.connect(self.text_changed)
        button_group2.buttonClicked.connect(self.selectbutton)
        current_folder = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_folder, 'down_arrow.png')
        print(image_path)
        image_path = image_path.replace("\\", "/")
        combobox.setStyleSheet(f"""
            QComboBox {{ 
                background-color: rgb(173, 221, 231);
                border-width: 8px; 
                border-style: solid; 
                border-radius: 25px; 
                border-color: rgb(173, 221, 231); 
                font: bold;
            }}
            QComboBox::drop-down {{ 
                border-width: 0px; 
            }}
            QComboBox::down-arrow {{ 
                image: url('{image_path}'); 
                background-color: rgb(0, 221, 231);
                width: 40px; 
                height: 40px;
                margin-right: 10px;
            }}
        """)
        addplanbutton.clicked.connect(self.checkalltext)
        preparebutton.clicked.connect(self.gotoscreen5)
        for button in button_group2.buttons():
            button.clicked.connect(self.on_button_clicked)
        planbuttongroup.buttonClicked.connect(self.deletebuttonfunc2)
        deleteplansbutton.clicked.connect(self.deletescelectedbutton2)
    def text_changed(self, s):
        global currenttype
        currenttype = s
        if s == "Daily Task":
            lineedit1.setVisible(1)
            lineedit2.setVisible(1)
            labelto.setVisible(1)
            maohao1.setVisible(1)
            lineedit3.setVisible(0)
            lineedit4.setVisible(0)
            maohao2.setVisible(0)
            labelto.setText("Hours")
            lineedit1.returnPressed.connect(self.checktext1)
            lineedit2.returnPressed.connect(self.checktext2)
            lineedit3.returnPressed.connect(self.checktext3)
            lineedit4.returnPressed.connect(self.checktext4)
        elif s=="One-Time Task":
            lineedit1.setVisible(1)
            lineedit2.setVisible(1)
            labelto.setVisible(1)
            maohao1.setVisible(1)
            lineedit3.setVisible(1)
            lineedit4.setVisible(1)
            maohao2.setVisible(1)
            labelto.setText("Need Time")
            lineedit1.returnPressed.connect(self.checktext1)
            lineedit2.returnPressed.connect(self.checktext2)
            lineedit3.returnPressed.connect(self.checktext3)
            lineedit4.returnPressed.connect(self.checktext4)
        elif s=="Scheduled Task":
            lineedit1.setVisible(1)
            lineedit2.setVisible(1)
            lineedit3.setVisible(1)
            lineedit4.setVisible(1)
            labelto.setVisible(1)
            maohao1.setVisible(1)
            maohao2.setVisible(1)
            labelto.setText("To")
            lineedit1.returnPressed.connect(self.checktext1)
            lineedit2.returnPressed.connect(self.checktext2)
            lineedit3.returnPressed.connect(self.checktext3)
            lineedit4.returnPressed.connect(self.checktext4)
    def checktext1(self):
        global flag
        try:
            int(lineedit1.text())
            flag=True
            print(int(lineedit1.text()))
        except ValueError:
            print("false")
            flag = False
        if flag == False:
            lineedit1.setStyleSheet(f"""
            * {{background-color: rgb(173, 50, 50);
                color: rgb(34, 137, 146);
                border-width: 9px;
                border-style: solid;
                border-radius: 25px;
                border-color: rgb(173, 50, 50);
                font: bold;
                }}
            """
            )
            lineedit1.setText("")
        else:
            if int(lineedit1.text()) >= 0 and int(lineedit1.text()) <24:
                lineedit1.setStyleSheet(f"""
                * {{background-color: rgb(173, 221, 231);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 221, 231);
                    font: bold;
                    }}
                """)
            else:
                lineedit1.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit1.setText("")
    def checktext2(self):
        global flag2
        try:
            int(lineedit2.text())
            flag2=True
            print(int(lineedit2.text()))
        except ValueError:
            print("false")
            flag2 = False
        if flag2 == False:
            lineedit2.setStyleSheet(f"""
            * {{background-color: rgb(173, 50, 50);
                color: rgb(34, 137, 146);
                border-width: 9px;
                border-style: solid;
                border-radius: 25px;
                border-color: rgb(173, 50, 50);
                font: bold;
                }}
            """
            )
            lineedit2.setText("")
        else:
            if int(lineedit2.text()) >= 0 and int(lineedit2.text()) <60:
                lineedit2.setStyleSheet(f"""
                * {{background-color: rgb(173, 221, 231);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 221, 231);
                    font: bold;
                    }}
                """)
            else:
                lineedit2.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit2.setText("")
    def checktext3(self):
        global flag3
        try:
            int(lineedit3.text())
            flag3=True
            print(int(lineedit3.text()))
        except ValueError:
            print("false")
            flag3 = False
        if flag3 == False:
            lineedit3.setStyleSheet(f"""
            * {{background-color: rgb(173, 50, 50);
                color: rgb(34, 137, 146);
                border-width: 9px;
                border-style: solid;
                border-radius: 25px;
                border-color: rgb(173, 50, 50);
                font: bold;
                }}
            """
            )
            lineedit3.setText("")
        else:
            if int(lineedit3.text()) >= 0 and int(lineedit3.text()) <24:
                lineedit3.setStyleSheet(f"""
                * {{background-color: rgb(173, 221, 231);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 221, 231);
                    font: bold;
                    }}
                """)
            else:
                lineedit3.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit3.setText("")
    def checktext4(self):
        global flag4
        try:
            int(lineedit4.text())
            flag4=True
            print(int(lineedit4.text()))
        except ValueError:
            print("false")
            flag4 = False
        if flag4 == False:
            lineedit4.setStyleSheet(f"""
            * {{background-color: rgb(173, 50, 50);
                color: rgb(34, 137, 146);
                border-width: 9px;
                border-style: solid;
                border-radius: 25px;
                border-color: rgb(173, 50, 50);
                font: bold;
                }}
            """
            )
            lineedit4.setText("")
        else:
            if int(lineedit4.text()) >= 0 and int(lineedit4.text()) <60:
                lineedit4.setStyleSheet(f"""
                * {{background-color: rgb(173, 221, 231);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 221, 231);
                    font: bold;
                    }}
                """)
            else:
                lineedit4.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit4.setText("")
    def checkalltext(self):
        global currenttype
        global currentbutton
        global flag
        global flag2
        global flag3
        global flag4
        global planlist
        global allplans
        global plans
        global planbutton_list
        global i2
        global planbuttongroup
        flag3 = flag4 = True
        try:
            int(lineedit1.text())
            flag=True
            print(int(lineedit1.text()))
        except ValueError:
            print("false")
            flag = False
        if flag == False:
            lineedit1.setStyleSheet(f"""
            * {{background-color: rgb(173, 50, 50);
                color: rgb(34, 137, 146);
                border-width: 9px;
                border-style: solid;
                border-radius: 25px;
                border-color: rgb(173, 50, 50);
                font: bold;
                }}
            """
            )
            lineedit1.setText("")
        else:
            if int(lineedit1.text()) >= 0 and int(lineedit1.text()) <24:
                lineedit1.setStyleSheet(f"""
                * {{background-color: rgb(173, 221, 231);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 221, 231);
                    font: bold;
                    }}
                """)
            else:
                lineedit1.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit1.setText("")
        try:
            int(lineedit2.text())
            flag2=True
            print(int(lineedit2.text()))
        except ValueError:
            print("false")
            flag2 = False
        if flag2 == False:
            lineedit2.setStyleSheet(f"""
            * {{background-color: rgb(173, 50, 50);
                color: rgb(34, 137, 146);
                border-width: 9px;
                border-style: solid;
                border-radius: 25px;
                border-color: rgb(173, 50, 50);
                font: bold;
                }}
            """
            )
            lineedit2.setText("")
        else:
            if int(lineedit2.text()) >= 0 and int(lineedit2.text()) <60:
                lineedit2.setStyleSheet(f"""
                * {{background-color: rgb(173, 221, 231);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 221, 231);
                    font: bold;
                    }}
                """)
            else:
                lineedit2.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit2.setText("")
        if currenttype=="Scheduled Task" or currenttype == "One-Time Task":
            try:
                int(lineedit3.text())
                flag3=True
                print(int(lineedit3.text()))
            except ValueError:
                print("false")
                flag3 = False
            if flag3 == False:
                lineedit3.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit3.setText("")
            else:
                if int(lineedit3.text()) >= 0 and int(lineedit3.text()) <24:
                    lineedit3.setStyleSheet(f"""
                    * {{background-color: rgb(173, 221, 231);
                        color: rgb(34, 137, 146);
                        border-width: 9px;
                        border-style: solid;
                        border-radius: 25px;
                        border-color: rgb(173, 221, 231);
                        font: bold;
                        }}
                    """)
                else:
                    lineedit3.setStyleSheet(f"""
                    * {{background-color: rgb(173, 50, 50);
                        color: rgb(34, 137, 146);
                        border-width: 9px;
                        border-style: solid;
                        border-radius: 25px;
                        border-color: rgb(173, 50, 50);
                        font: bold;
                        }}
                    """
                    )
                    lineedit3.setText("")
            try:
                int(lineedit4.text())
                flag4=True
                print(int(lineedit4.text()))
            except ValueError:
                print("false")
                flag4 = False
            if flag4 == False:
                lineedit4.setStyleSheet(f"""
                * {{background-color: rgb(173, 50, 50);
                    color: rgb(34, 137, 146);
                    border-width: 9px;
                    border-style: solid;
                    border-radius: 25px;
                    border-color: rgb(173, 50, 50);
                    font: bold;
                    }}
                """
                )
                lineedit4.setText("")
            else:
                if int(lineedit4.text()) >= 0 and int(lineedit4.text()) <60:
                    lineedit4.setStyleSheet(f"""
                    * {{background-color: rgb(173, 221, 231);
                        color: rgb(34, 137, 146);
                        border-width: 9px;
                        border-style: solid;
                        border-radius: 25px;
                        border-color: rgb(173, 221, 231);
                        font: bold;
                        }}
                    """)
                else:
                    lineedit4.setStyleSheet(f"""
                    * {{background-color: rgb(173, 50, 50);
                        color: rgb(34, 137, 146);
                        border-width: 9px;
                        border-style: solid;
                        border-radius: 25px;
                        border-color: rgb(173, 50, 50);
                        font: bold;
                        }}
                    """
                    )
                    lineedit4.setText("")
        if flag == True and flag2 == True and flag3 == True and flag4 == 1:
            if currentbutton in allplans:
                self.timer = QTimer()
                self.timer.setSingleShot(True)
                labelto.setText("the plan is already existed")
                self.timer.timeout.connect(self.runouttime)
                self.timer.start(3000)
            else:
                if currenttype == "Daily Task":
                    a = []
                    a.append(lineedit1.text())
                    a.append(lineedit2.text())
                    a.append(lineedit3.text())
                    a.append(lineedit4.text())
                    allplans.append(currentbutton)
                    plans[0].update({currentbutton : a})
                    planbutton_text = f"{currenttype}\n{currentbutton}\n{a[0]} : {a[1]} Hours"
                elif currenttype == "One-Time Task":
                    a = []
                    a.append(lineedit1.text())
                    a.append(lineedit2.text())
                    plans[1].update({currentbutton : a})
                    allplans.append(currentbutton)
                    planbutton_text = f"{currenttype}\n{currentbutton}\n{a[0]} : {a[1]} (24-Hour)"
                elif currenttype == "Scheduled Task":
                    a = []
                    a.append(lineedit1.text())
                    a.append(lineedit2.text())
                    a.append(lineedit3.text())
                    a.append(lineedit4.text())
                    plans[2].update({currentbutton : a})
                    allplans.append(currentbutton)
                    planbutton_text = f"{currenttype}\n{currentbutton}\n{a[0]} : {a[1]}  to  {a[3]} : {a[4]}"
                planbutton_list.update({planbutton_text : [QPushButton(planbutton_text), 0, currentbutton]})
                planbutton_list[planbutton_text][0].setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                "font: 15px;"
                )
                planbutton_list[planbutton_text][0].setFixedSize(300, 100)
                planbuttongroup.addButton(planbutton_list[planbutton_text][0])
                planlayout.addWidget(planbutton_list[planbutton_text][0], i2, 1)
                i2 += 1
                planbox.setLayout(planlayout)
                planbox.update()
                scrollarea3.setWidgetResizable(True)
                scrollarea3.setWidget(planbox)
                
                
    def runouttime(self):
        global labelto
        labelto.setText("To")
    def on_button_clicked(self, button):
        print(button.text())
    def selectbutton(self, button):
        global currentbutton
        global select_button
        global button_group2
        print(select_button[button.text()], button.text())
        if currentbutton == "":
            currentbutton = button.text()
            button.setStyleSheet(
            "background-color: rgb(45, 45, 180);"
            "border-width: 1px;"
            "border-style: solid;"
            "border-radius: 30px;"
            "border-color: rgb(126, 150, 160);"
            )
            select_button[button.text()] = 1
        elif currentbutton == button.text():
            if select_button[button.text()]==0:
                button.setStyleSheet(
                "background-color: rgb(45, 45, 180);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(126, 150, 160);"
                )
                select_button[button.text()]=1
            else:
                button.setStyleSheet(
                    "background-color: rgb(85, 85, 255);"
                    "border-width: 1px;"
                    "border-style: solid;"
                    "border-radius: 30px;"
                    "border-color: rgb(173, 221, 231);"
                    )
                select_button[button.text()]=0
                currentbutton = ""
        elif currentbutton != button.text():
            for buttons in button_group2.buttons():
                select_button[buttons.text()]=0
                buttons.setStyleSheet(
                    "background-color: rgb(85, 85, 255);"
                    "border-width: 1px;"
                    "border-style: solid;"
                    "border-radius: 30px;"
                    "border-color: rgb(173, 221, 231);"
                    )
            currentbutton = button.text()
            button.setStyleSheet(
            "background-color: rgb(45, 45, 180);"
            "border-width: 1px;"
            "border-style: solid;"
            "border-radius: 30px;"
            "border-color: rgb(126, 150, 160);"
            )
            select_button[currentbutton]=1
    def deletebuttonfunc2(self, button):
        if planbutton_list[button.text()][1]==0:
            button.setStyleSheet(
            "background-color: rgb(45, 45, 180);"
            "border-width: 1px;"
            "border-style: solid;"
            "border-radius: 30px;"
            "border-color: rgb(126, 150, 160);"
            "font: 15px;"
            )
            planbutton_list[button.text()][1]=1
        else:
            button.setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                "font: 15px;"
                )
            planbutton_list[button.text()][1]=0
    def deletescelectedbutton2(self):
        global i2
        global planlayout
        global planbox
        global planbuttongroup
        global allplans
        global plans
        global planbutton_list
        global restbutton2
        global deleteplansbutton
        clear_layout(planlayout)
        global deletelist3
        deletelist3 = []
        restbutton2 = []
        #allplans.clear()
        #plans.clear()
        for button in planbutton_list:
            if planbutton_list[button][1] == 1:
                i2 -=1
                deletelist3.append(button)
                planbuttongroup.removeButton(planbutton_list[button][0])
                for o in range(3):
                    try:
                        if planbutton_list[button][2] in plans[o]:
                            plans[o].pop(planbutton_list[button][2])
                    except KeyError():
                        timer = QTimer()
                        timer.setSingleShot(True)
                        deleteplansbutton.setText("No Tasks were deleted")
                        timer.start(5000)
                        timer.timeout.connect(self.runouttime2)
                allplans.remove(planbutton_list[button][2])
        for button in planbuttongroup.buttons():
            for o in range(3):
                try:
                    print("kkkkkuaile", button.text(), plans[o])
                    if planbutton_list[button.text()][2] in plans[o]:
                        #print("kkkuaile", button.text())
                        restbutton2.append([button.text(), o, planbutton_list[button.text()][2]])
                except KeyError():
                    timer = QTimer()
                    deleteplansbutton.setText("No Tasks were deleted")
                    timer.start(5000)
                    timer.timeout.connect(self.runouttime2)
        deletelist3.clear()
        planbutton_list.clear()
        clear_and_delete_buttons_from_group(planbuttongroup)
        for button in restbutton2:
            i2+=1
            print("mmmm", i2)
            self.buttt = QPushButton(button[0])
            self.buttt.setFixedSize(300, 100)
            self.buttt.setStyleSheet(
                "background-color: rgb(85, 85, 255);"
                "border-width: 1px;"
                "border-style: solid;"
                "border-radius: 30px;"
                "border-color: rgb(173, 221, 231);"
                "font: 15px;"
                    )
            planbutton_list.update({self.buttt.text() : [self.buttt, 0, button[2]]})
            planbuttongroup.addButton(self.buttt)
            planlayout.addWidget(self.buttt, i2, 1)
            planbox.setLayout(planlayout)
            scrollarea3.setWidget(planbox)
        print("haha", allplans,"\n",  plans, "\n", planbutton_list)
        i2 += 1
    def tunouttime2(self):
        global deleteplansbutton
        deleteplansbutton.setText("Delete Plans")
    def gotoscreen5(self):
        widget.setCurrentIndex(4)
        global planbutton_list
        global plans
        global timeline
        timeline = []
        counts = 0
        resttime = 24*60
        for i in plans:
            for j in i:
                counts += 1
        for i in range(25*60):
            timeline.append("")
        for i in plans[2]:
            if i[0]==i[2]:
                for j in range(i[1], i[3]+1):
                    timeline[i[0]*60+j] = i
                    resttime -= 1
            else:
                for j in range (i[1], 60):
                    timeline[i[0]*60+j] = i
                    resttime -= 1
                for j in range (i[0]+1, i[2]+1):
                    for k in range (60):
                        timeline[j*60+k] = i
                        resttime -= 1
                for j in range (0, i[3]):
                    timeline[i[2]*60+j] = i
                    resttime -= 1
        sorted_dic = dict(sorted(plans[2].items(), key = lambda item: (item[1][0]*60 + item[1][1])))
        ii = 0
        x = sorted_dic.keys()
        sorted_dic[x[ii]].append(0)
        print(sorted_dic[0])
        for i in range(len(timeline)):
            if i == "":
                if (sorted_dic[x[ii]][2] == 0 and sorted_dic[x[ii]][3] == 0) or i==sorted_dic[x[ii][0]]*60+sorted_dic[x[ii][1]]:
                    while sorted_dic[x[ii]][2] == 0 and sorted_dic[x[ii]][3] == 0 and i<sorted_dic[x[ii][0]]*60+sorted_dic[x[ii][1]]:
                        ii += 1
                elif sorted_dic[x[ii]][3] == 0:
                    sorted_dic[x[ii]][2] -= 1
                    sorted_dic[x[ii]][3] == 59
                    timeline[i] = x[ii]
                    resttime -= 1
                    sorted_dic[x[ii]][4] += 1
                else:
                    sorted_dic[x[ii]][3] -= 1
                    timeline[i] = x[ii]
                    resttime -= 1
                    sorted_dic[x[ii]][4] += 1
        sorted_dic2
        
                    
        

class Screen5(QDialog):
    def __init__(self):
        super(Screen5,self).__init__()
        uic.loadUi(os.path.join(basedir, "cal5.ui"), self)
                
        
app = QApplication(sys.argv)

widget=QtWidgets.QStackedWidget()
UIWindow = UI()
screen2=Screen2()
screen3 = Screen3()
screen4 = Screen4()
screen5 = Screen5()
widget.addWidget(UIWindow)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.addWidget(screen4)
widget.addWidget(screen5)
widget.show()
app.exec()