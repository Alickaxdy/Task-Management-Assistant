from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Layout for the main window
        layout = QVBoxLayout(self)

        # Original scroll area
        self.original_scroll_area = QScrollArea(self)
        self.original_widget = QWidget()
        self.original_layout = QVBoxLayout(self.original_widget)
        
        # Add some buttons to the original scroll area
        for i in range(5):
            btn = QPushButton(f"Button {i+1}", self)
            self.original_layout.addWidget(btn)
        
        self.original_scroll_area.setWidget(self.original_widget)
        layout.addWidget(self.original_scroll_area)

        # Duplicate button
        duplicate_btn = QPushButton("Duplicate ScrollArea", self)
        duplicate_btn.clicked.connect(self.duplicate_scroll_area)
        layout.addWidget(duplicate_btn)

    def duplicate_scroll_area(self):
        # New scroll area
        new_scroll_area = QScrollArea(self)
        new_widget = QWidget()
        new_layout = QVBoxLayout(new_widget)
        
        # Copy buttons from the original to the new scroll area
        for i in range(self.original_layout.count()):
            original_btn = self.original_layout.itemAt(i).widget()
            new_btn = QPushButton(original_btn.text(), self)
            new_layout.addWidget(new_btn)
        
        new_scroll_area.setWidget(new_widget)
        self.layout().addWidget(new_scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())