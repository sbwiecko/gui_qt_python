import sys
from PySide6.QtWidgets import QApplication, QWidget #, QPushButton
# windows inherit from the QWidget class
# can also from PySide6 import QtWidgets
# and all the widgets needed are neceassrily prefixed with QtWidgets
# e.g., app = QtWidgets.QApplication()

# app = QApplication()
# app = QApplication([]) # empty list was minimally required in previous versions of PySide
app = QApplication(sys.argv) # take flags from the command line, e.g., python application -style Fusion

win = QWidget()
# win = QPushButton("Click me!") # inherits from QWidget, can be shown as a window...
# win2 = QWidget()

win.show() # not shown by default!
# win2.show() # 2 windows for a single app

app.exec() # also app.exec_() as from python2
# as long as the app runs, the script is running
