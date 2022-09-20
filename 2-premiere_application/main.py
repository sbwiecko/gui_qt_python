from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QVBoxLayout, QHBoxLayout

# organize the widgets into a class with methods
class MainWindow(QWidget): # inherit all from QWidget
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ma première application !")
        # self.setFixedSize(200,200) # fixed size window
        # self.setMinimumWidth(200) # cannot resize width below 200 px
        # self.setMinimumSize(200,200)
        self.resize(200,300) # with default sizes
        # see document from doc.qt.io/qtforpython/PySide6
        #e.g., QtCore.QObject + QtGui.QPaintDevice -> QWidget -> QAbstractButton -> QPushButton

        # self.setText("text") # only from QPushButton, QLabel and QlineEdit classes
        # self.text() # corresponding getter

        # layouts: QVBoxLayout, QHBoxLayout, QStackedLayout and QGridLayout
        main_layout = QHBoxLayout(self) # pass the parent widget to layout
        # self.setLayout(main_layout) # another way to add layout to the windows/widget

        left_layout = QVBoxLayout()
        middle_layout=QHBoxLayout()
        right_layout= QVBoxLayout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        for i in range(1, 11):
            btn = QPushButton(str(i))
            left_layout.addWidget(btn)

        for i in range(11, 21):
            btn = QPushButton(str(i))
            right_layout.addWidget(btn)

        for i in range(21, 30):
            btn = QPushButton(str(i))
            middle_layout.addWidget(btn)

        right_layout.addLayout(middle_layout)


class WindowList(QListWidget): # inherit all from QListWidget
    def __init__(self):
        super().__init__()

        self.addItem("Item 1")
        self.addItem("Item 2")
        self.addItem("Item 3")

app = QApplication()

main_window = MainWindow()
window_list = WindowList()

main_window.show()
# window_list.show()
app.exec()