from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

# organize the widgets into a class with methods
class MainWindow(QWidget): # inherit all from QWidget
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Connecter les widgets directement")

        main_layout = QVBoxLayout(self)

        self.le_text = QLineEdit()
        self.lbl_text= QLabel("...")
        self.btn_clear=QPushButton("Clear")

        main_layout.addWidget(self.le_text)
        main_layout.addWidget(self.lbl_text)
        main_layout.addWidget(self.btn_clear)
        # direct connection to a widget method
        # textChanged returns the value of the text in the QLineEdit box
        # and is sent to the setText method of the 
        self.le_text.textChanged.connect(self.lbl_text.setText)

        self.btn_clear.clicked.connect(self.clear_text)

    def clear_text(self): # interesting when we have > 1 action to connect
        self.le_text.clear() # direct method
        self.lbl_text.setText("...")


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
