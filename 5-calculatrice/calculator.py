from PySide6 import QtCore
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QWidget, QGridLayout,
    QLineEdit, QPushButton, QSizePolicy
)

BUTTONS = {
    "C": (1,0,1,1), # text of the button and its coordinates
    "/": (1,3,1,1), # as a tuple in the format of QGridLayout
    "7": (2,0,1,1), # y-coordinate, x-coordinate, heigth, width
    "8": (2,1,1,1), # with top-left of the grid (0,0)
    "9": (2,2,1,1),
    "x": (2,3,1,1),
    "4": (3,0,1,1),
    "5": (3,1,1,1),
    "6": (3,2,1,1),
    "-": (3,3,1,1),
    "1": (4,0,1,1),
    "2": (4,1,1,1),
    "3": (4,2,1,1),
    "+": (4,3,1,1),
    "0": (5,0,1,2), # 2 squares in width
    ".": (5,2,1,1),
    "=": (5,3,1,1),
}

OPERATIONS = ["+", "-", "/", "x"]


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculatrice")
        self.setStyleSheet( # CSS-like
            """
            background-color: rgb(20,20,20); /*background*/
            color: rgb(220,220,220);         /*font color*/
            font-size: 20 px;                /*font size*/
            """
        )
        self.main_layout = QGridLayout(self)

        self.le_result = QLineEdit("0") # default text "0"
        self.le_result.setEnabled(False) # cannot edit directly, need to use buttons or shortcuts

        self.main_layout.addWidget(self.le_result, 0, 0, 1, 4)
        
        ### styling widgets ###
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.le_result.setMinimumHeight(50) # px
        self.le_result.setAlignment(QtCore.Qt.AlignRight) # left align by default
        self.le_result.setStyleSheet(
            """
            border: none;                           /*no border*/
            border-bottom: 2px solid rgb(30,30,30); /*add border bottom*/
            padding: 0 8px;                         /*no vertical padding, only horizontal*/
            font-size: 24px;                        /*font size*/
            font-weight: bold;                      /*font weight*/
            """
        )

        self.buttons = {} # dict to keep track of all buttons created
        # go through each button encoded in the BUTTONS dict
        for button_text, button_position in BUTTONS.items():
            button = QPushButton(button_text)
            
            ### styling buttons ###
            button.setMinimumSize(48,48)
            button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding) # vertical, horizontal; Expanding vertical only by default
            button.setStyleSheet( # double curly bracket in f-string to get an actual curly bracket in the CSS
                f"""
                QPushButton {{
                    border: none; /*no border*/
                    font: bold;   /*font weight*/
                    background-color: {'#1e1e2d' if button_text in OPERATIONS else 'none'};
                    }}
                QPushButton:pressed {{
                    background-color: '#f31d58';
                    }}
                """
            )
            
            # unpack the coordinates of the button position
            self.main_layout.addWidget(button, *button_position)
            self.buttons[button_text] = button # keep track of each button
            # create the connection for each button in the loop
            if button_text not in ["=", "C"]: # connect to method if not special buttons
                button.clicked.connect(self.number_or_operation_pressed)
        
        # connection to special actions
        self.buttons["C"].clicked.connect(self.clear_result)
        self.buttons["="].clicked.connect(self.compute_result)
        self.buttons["="].setStyleSheet("background-color: #f31d58;")
        self.connect_keyboard_shortcuts()

    @property
    # simplify the call of the text() method on le_result by making it a property
    def le_content(self):
        return self.le_result.text()

    def number_or_operation_pressed(self):
        # first check if last character in the box is an operation symbol
        # sender() magical methods to get the identity of the button clicked/actionated
        if self.sender().text() in OPERATIONS:
            # if there is already a sign operation in the le_result box
            # or there is nothing yet in the box, AND the sign is different from '-'
            # so that we can still start with negative numbers, then we stop typing
            if self.le_content[-1] in OPERATIONS or (self.le_content=="0" and self.sender().text()!="-"):
                return
        
        # when we start a new operation, clear the le_result first
        #if self.le_result.text() == "0":
        if self.le_content == "0":
            self.le_result.clear()
        # refresh the le_result text with a concatenation of the current text
        # with the text of the button clicked, if not "C" or "="
        self.le_result.setText(
            #self.le_result.text() + self.sender().text()
            self.le_content + self.sender().text()
        )

    def compute_result(self):
        try: # save the program from crashing because of syntax error
            result = eval(
                #self.le_result.text().replace('x', '*') # replace 'x' symbol
                self.le_content.replace('x', '*') # replace 'x' symbol
            )
        except SyntaxError:
            return # exit from method without throwing error
        
        self.le_result.setText(str(result)) # refresh le with str transform of the evaluated calc

    def clear_result(self):
        self.le_result.setText("0") # back to default text

    def remove_last_character(self):
        # take all the content of le_result except the last character, and put it back in le_result
        # if length is zero, we put back the initial "0" in the box
        self.le_result.setText(
            #self.le_result.text()[:-1] if len(self.le_result.text()) > 1 else "0"
            self.le_content[:-1] if len(self.le_content) > 1 else "0"
        )

    def connect_keyboard_shortcuts(self):
        """
        connect the keyboard to the corresponding buttons
        """
        for button_text, button in self.buttons.items():
            QShortcut(
                QKeySequence(              # sequence mandatory even for one key
                    button_text            # string format
                ),
                self,                      # parent object
                button.clicked.emit        # simulates a click on the corresponding button
            )
        
        # connect the RETURN key to the compute_result method
        # could also connect to the sequence in the string format, e.g., "return"
        QShortcut(QKeySequence(QtCore.Qt.Key_Return), self, self.compute_result)
        # could also bind other key, e.g., "*" and "=" from the numeric pad
        QShortcut(QKeySequence(QtCore.Qt.Key_Backspace), self, self.remove_last_character)

app = QApplication()
win = Calculator()
win.show()
app.exec()