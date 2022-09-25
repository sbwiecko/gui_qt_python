import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QPushButton, QHBoxLayout

# organize the widgets into a class with methods
class MainWindow(QWidget): # inherit all from QWidget
    def __init__(self):
        super().__init__()
    #     self.initializeUI() # recommended

    # def initializeUI(self): # recommended
    #     """Set up application's GUI."""
        self.setWindowTitle("Signaux Qt")

        main_layout = QHBoxLayout(self) # pass the parent widget to layout

        self.button = QPushButton("Click !") # link the button to the instance of the object
                                             # to manipulate it in other methods, e.g., in button_checked()
        self.button.setCheckable(True)

        main_layout.addWidget(self.button) # add button to layout

        ### SLOTS ###
        self.button.clicked.connect(self.button_clicked) # connect action to method
        # see also the documenation, the clicked signal send a check=False by default

        # button.pressed.connect(self.button_pressed)
        # button.released.connect(self.button_released)
    
    # def button_pressed(self):
    #     print("Le bouton a bien été pressé.")
    
    # def button_released(self):
    #     print("Le bouton a bien été relâché.")

        self.show() # widget not displayed by default
        
    def button_clicked(self, checked):
        print("Le bouton a bien été cliqué.")
        self.button.setText("CHECKED") if checked else self.button.setText("Click !")

if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    # main_window.show() # considere showing the widget/window in the class
    sys.exit(app.exec()) # handle the app exit by the system optimally
    # app.exec()
