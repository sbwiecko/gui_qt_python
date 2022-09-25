###############################################################################
# See also https://doc.qt.io/qtforpython/tutorials/basictutorial/uifiles.html #
###############################################################################

### OPTION A - LOADING FROM A PYTHON CLASS ###

import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from calculator import Ui_Form # use the name of the correct python file
                               # look also at the correct class name

class MainWindow(QWidget):     # and beware the parent class inhirited from
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()    # here as well, put the correct class name
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


#################################################################################


### OPTION B - LOADING .UI FILE DIRECTLY ###
"""
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "calculator.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())
"""