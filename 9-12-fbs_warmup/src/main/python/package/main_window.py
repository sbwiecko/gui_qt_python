from PySide6 import QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_clique = QtWidgets.QPushButton("click !")

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_clique)

    def setup_connections(self):
        self.btn_clique.clicked.connect(self.bouton_clicked)

    def bouton_clicked(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("congratulations!")
        message_box.setText("you successfully created a customized app")
        message_box.exec()
