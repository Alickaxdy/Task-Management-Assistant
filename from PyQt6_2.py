from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QButtonGroup, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget and layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Create a button group
        self.buttonGroup = QButtonGroup()

        # Create and add buttons to the button group
        for i in range(5):  # Example: Create 5 buttons
            button = QPushButton(f"Button {i+1}", centralWidget)  # Set centralWidget as parent
            self.buttonGroup.addButton(button, i)  # The second parameter is an optional id
            print(f"Adding {button.text()}")  # Debugging output

        # Loop through the button group and add each button to the layout
        for button in self.buttonGroup.buttons():
            layout.addWidget(button)
            print(f"Added {button.text()} to layout")  # Debugging output

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()