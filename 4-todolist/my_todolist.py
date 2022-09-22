from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLineEdit, QPushButton

# main windows
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application ToDoList")
        self.resize(200,300)

        #self.task_list = [] # the core task list that contain the individual tasks

        ### CREATE WIDGETS
        # QListWidget that contains all the tasks entered
        self.lst = QListWidget()
        
        # QLineEdit to add a new task to the list
        self.le = QLineEdit()
        
        # QPushButton to clear the entire list
        self.btn = QPushButton("Tout supprimer")
        
        ### PREPARE LAYOUT
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.lst)
        main_layout.addWidget(self.le)
        main_layout.addWidget(self.btn)

        ### CONNECT ACTIONS
        # entering <ENTER> in the LineEdit saves the task to the List
        self.le.returnPressed.connect(self.onPressed)
        
        # <double-click> on a task in the List deleted the task
        self.lst.doubleClicked.connect(self.deleteSelection)

        # <CLICK> on the Button remove ALL the tasks in the List
        self.btn.clicked.connect(self.lst.clear) # connect direct to widget method
    
    def onPressed(self):
        task = self.le.text()
        if task != "":             # if not empty line
            self.lst.addItem(task) # transfer the current task from le to lst
            self.le.clear()        # clear the le
    
    def deleteSelection(self):
        # suppose there is only one task selected for deletion
        item = self.lst.currentRow()
        self.lst.takeItem(item)
        del(item) # Items removed from a list widget will not be managed by Qt, and will need to be deleted manually.


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
