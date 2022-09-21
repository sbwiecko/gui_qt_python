from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from functools import partial # see https://docs.python.org/3/library/functools.html

# organize the widgets into a class with methods
class MainWindow(QWidget): # inherit all from QWidget
    def __init__(self):
        super().__init__()

        self.setWindowTitle("connections avec partial")

        main_layout = QHBoxLayout(self)

        self.btn_left = QPushButton("Left")
        self.btn_right = QPushButton("Right")

        main_layout.addWidget(self.btn_left)
        main_layout.addWidget(self.btn_right)

        self.btn_left.clicked.connect(
            partial(
                self.button_clicked, # call a common method
                "Bouton de gauche"   # and pass it a specific arg
            )
        )
        # note that self.button_clicked(message)
        # would be called automatically
        # returning None to the connection

        self.btn_right.clicked.connect(
            partial(
                self.button_clicked,
                "Bouton de droite"
            )
        )

        # partial avoids calling two very similar methods
        # self.btn_left.clicked.connect(self.button_left_clicked)
        # self.btn_right.clicked.connect(self.button_right_clicked)
    # with
    # def button_left_clicked(self):
    #    print("Bouton de gauche")
    #
    # def button_right_clicked(self):
    #    print("Bouton de droite")

    def button_clicked(self, message):
        print(message)


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
