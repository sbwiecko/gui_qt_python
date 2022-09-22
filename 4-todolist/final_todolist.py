from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton

# main windows
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Docstring ToDoList")

        self.main_layout = QVBoxLayout(self)

        self.lw_todos = QListWidget()
        self.le_task_title = QLineEdit()
        self.le_task_title.setPlaceholderText("Tâche à effectuer...")
        self.btn_clear = QPushButton("Tout supprimer")
        
        self.main_layout.addWidget(self.lw_todos)
        self.main_layout.addWidget(self.le_task_title)
        self.main_layout.addWidget(self.btn_clear)

        self.le_task_title.returnPressed.connect(self.add_todo)
        self.lw_todos.itemDoubleClicked.connect(self.delete_todo) # returns the text of the currentItem !
        self.btn_clear.clicked.connect(self.lw_todos.clear)


    def add_todo(self):
        self.lw_todos.addItem(self.le_task_title.text()) # could also add a true Item, i.e., with format, colors, etc.
        self.le_task_title.clear()
    
    def delete_todo(self, item):
        self.lw_todos.takeItem(self.lw_todos.row(item))

app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
