from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QWidget, QApplication)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stretch")
        self.layout = QHBoxLayout(self)
        previous = QPushButton("<<")
        titre = QLabel("Introduction à Python")
        titre.setAlignment(Qt.AlignCenter)
        next = QPushButton(">>")

        print(previous.sizePolicy())

        # # Solution 1
        self.layout.addWidget(previous)
        # self.layout.addStretch() # adds kind of stretch that push the left button to the left
        self.layout.addWidget(titre)
        # self.layout.addStretch() # and here push the right button to the right
        self.layout.addWidget(next)

        # # Solution 2
        # previous.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # next.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # # Solution 3
        # # though it doesn't really keep the original button size
        # self.layout.setStretch(0, 1)
        # self.layout.setStretch(1, 100)
        # self.layout.setStretch(2, 1)

        # # Solution 4
        # # a derivate of Solution 2
        # previous.setMaximumWidth(previous.sizeHint().width())
        # next.setMaximumWidth(next.sizeHint().width())

        # Solution 5
        # works since sizePolicy of QPushButton set to minimum by default
        # and sizePolicy of QLabel set to Preferred
        # with 'Preferred', sizeHint is best, and no advantage to be larger
        # with 'Exanding', widget should get as much space as possible
        # see also https://doc.qt.io/qt-6/qsizepolicy.html
        titre.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.setFocus()


app = QApplication()
win = MainWindow()
win.show()
app.exec()