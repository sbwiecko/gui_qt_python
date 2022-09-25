import sys
from random import randrange
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout
)

class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up application's GUI."""
        self.setWindowTitle("Surcharge")

        layout = QHBoxLayout(self)

        #~~ peronalize two buttons
        button = QPushButton(str(randrange(999)))
        button.setMinimumSize(48,48)
        button.setFlat(True)
        button.setCheckable(True)
        button.setStyleSheet(f"color: rgb(255,0,0);")

        layout.addWidget(button)

        button = QPushButton(str(randrange(999)))
        button.setMinimumSize(48,48)
        button.setFlat(True)
        button.setCheckable(True)
        button.setStyleSheet(f"color: rgb(0,255,0);")

        layout.addWidget(button)
        self.setFocus() # focus on widget/window
                        # great when multiple windows are showns
                        # or for more interactivity

        self.show() # widget not displayed by default
        

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    sys.exit(app.exec())
