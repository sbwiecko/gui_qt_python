import sys
from random import randrange
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout
)

### Our own class for a custmoized QPushButton
class RandomButton(QPushButton): # inherits from QPushButton
    def __init__(self, size=48, flat=True): # some default values
        super().__init__()
        self.setText(str(randrange(999))) # here self is the instance of RandomButton
        self.setMinimumSize(size,size)
        self.setFlat(flat)
        self.setCheckable(True)
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")

        self.clicked.connect(self.random_color)
    
    def random_color(self):
        self.setStyleSheet(f"color: rgb({randrange(255)}, {randrange(255)}, {randrange(255)});")


class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up application's GUI."""
        self.setWindowTitle("Custom Button")

        layout = QHBoxLayout(self)

        for _ in range(10):
            button = RandomButton(size=randrange(10,80), flat=True)
            layout.addWidget(button)

        self.show()
        

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    sys.exit(app.exec())
