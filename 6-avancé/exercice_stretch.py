import sys

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
)


class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up application's GUI."""
        self.setWindowTitle("Exercice 1 -- Strech")
        layout = QHBoxLayout(self)

        button_left = QPushButton("<<")
        label_center= QLabel("Introduction à Python")
        label_center.setAlignment(QtCore.Qt.AlignCenter)
        button_right= QPushButton(">>")

        layout.addWidget(button_left)
        layout.addWidget(label_center)
        layout.addWidget(button_right)

        layout.setStretch(0, 1)
        layout.setStretch(1, 10)
        layout.setStretch(2, 1)

        self.show()


if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    sys.exit(app.exec())
