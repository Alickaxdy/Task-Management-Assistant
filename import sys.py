import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QScrollArea

class ScrollableButtonWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for the scrollable area
        layout = QVBoxLayout(self)

        # Create buttons and add them to the layout
        for i in range(20):
            button = QPushButton(f"Button {i+1}")
            layout.addWidget(button)

        # Set the layout for the widget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create the widget with buttons
        button_widget = ScrollableButtonWidget()

        # Set the widget as the scroll area's widget
        scroll_area.setWidget(button_widget)

        # Set the scroll area as the central widget
        self.setCentralWidget(scroll_area)

        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Scrollable Buttons Example")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()