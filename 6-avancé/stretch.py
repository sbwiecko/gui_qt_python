import sys

from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton
)


class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up application's GUI."""
        self.setWindowTitle("Strech")
        layout = QHBoxLayout(self)

        button1= QPushButton("1")
        button2= QPushButton("2")
        button3= QPushButton("3")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # the stretching of the widgets is defined in the layout
        # with setStrech(index, stretch), index is 0-indexed widget
        # and stretch the factor of stretching, relative to each index
        # at initialization, the size defined in sizeHint is applied
        layout.setStretch(0, 5)
        layout.setStretch(1, 1)
        layout.setStretch(2, 10)

        self.setFocus()
        self.show()
        

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    sys.exit(app.exec())
