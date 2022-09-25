import sys
from random import randrange
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QHBoxLayout
)

class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.windows = {} # keep track of all windows created
        self.initializeUI()

    def initializeUI(self):
        """Set up application's GUI."""
        self.setWindowTitle("Multi windows")
        self.resize(600,400)
        layout = QHBoxLayout(self) # layout doesn't need to be self.layout

        self.button = QPushButton("New window")
        self.button.clicked.connect(self.create_new_window)
        layout.addWidget(self.button)

        self.show() # widget not displayed by default
        
    def create_new_window(self):
        """Create a new window with a random number."""
        window_number = randrange(999) # simulate an unique window
        self.windows[f"window{window_number}"] = QWidget()
        self.windows[f"window{window_number}"].setWindowTitle(f"Fenêtre #{window_number}")
        self.windows[f"window{window_number}"].show()
        # if the window created wasn't put in the Global space, i.e., attached to the application,
        # the Python garbage collector would delete the widget immediately at the end of the function
        # and if the same variable was used to create the widget, it would replace the previous one.

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    sys.exit(app.exec())
