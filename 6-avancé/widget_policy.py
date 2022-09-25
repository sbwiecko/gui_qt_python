import sys
from random import randrange

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QSizePolicy
)


class CustomLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

    # supercharge the sizeHint for a custom widget!
    def sizeHint(self):
        return QSize(200, 20)


class MainWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up application's GUI."""
        self.setWindowTitle("Widget policy")
        layout = QHBoxLayout(self)

        line_edit = QLineEdit()
        button = QPushButton("Login")

        # changing the size policy of a widget
        # line_edit.setSizePolicy(
        #     QSizePolicy.Fixed, # import from QtWidgets
        #     QSizePolicy.Expanding
        # )

        layout.addWidget(line_edit)
        layout.addWidget(button)

        # access to the sizeHint and sizePolicy set by default
        # sizeHint is the preferreed size of the widget
        # sizePolicy describes how the size may change when the preferred size cannot be used
        # sizeConstraint are the min and max sizes the widget can be
        print("line_edit sizeHint: ", line_edit.sizeHint())
        print("line_edit sizePolicy:", line_edit.sizePolicy())
        print("button sizeHint:", button.sizeHint())
        print("button sizePolicy:",button.sizePolicy())
        # both widgets have fixed vertical size policy
        # QPushButton has a minimum horizontal size of 75,
        # but with QLineEdit having an expanding horizontal size policy,
        # the QPushButton will never expand and stay at the minimum
        # see also https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QSizePolicy.html#detailed-description

        self.setFocus()
        self.show()
        

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    sys.exit(app.exec())
