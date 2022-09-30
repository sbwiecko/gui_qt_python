from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import (
    QWidget, QPushButton, QListWidget, QListWidgetItem,
    QTextEdit, QGridLayout, QInputDialog
)

# will be called from main.py that is in the same directory than package
from package.api.note import Note, get_notes


class MainWindow(QWidget): # no need to create a full window with status and tool bars
    def __init__(self, ctx): # pass in a context to load a stylesheet from main.py
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("PyNotes")

        self.setup_ui()
        self.populate_notes()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        # keep the order, first create layout and widgets, and then add widgets to layout
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_createNote = QPushButton("Créer une note")
        self.lw_notes = QListWidget()
        self.te_contenu = QTextEdit()

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css") # beware the folder structure
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

    def create_layouts(self):
        self.main_layout = QGridLayout(self)
        # set as a squared grid, but the QPushButton won't extend by heigth

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_createNote, 0, 0, 1, 1)
        self.main_layout.addWidget(self.lw_notes, 1, 0, 1, 1)
        self.main_layout.addWidget(self.te_contenu, 0, 1, 2, 1)

    def setup_connections(self):
        self.btn_createNote.clicked.connect(self.create_note)
        self.te_contenu.textChanged.connect(self.save_note) # save everytime the text changes (no dedicated button)
        # connect to change in the selection of the item in lw:
        self.lw_notes.itemSelectionChanged.connect(self.populate_note_content)
        QShortcut(
            QKeySequence("Backspace"), # action
            self.lw_notes,             # widget linked to shortcut
            self.delete_selected_note  # slot/method called
        )

    # END UI

    def add_note_to_listwidget(self, note):
        lw_item = QListWidgetItem(note.title)
        lw_item.note = note # creating a dynamic "note" attribute on the lw_item instance
        self.lw_notes.addItem(lw_item)

    def create_note(self):
        titre, resultat = QInputDialog.getText(
            self,
            "Ajouter une note",
            "Titre: "
        )
        # QInputDialog returns 0 if cancel or quit, 1 otherwise
        # also check if titre is not None
        if resultat and titre:
            note = Note(title=titre)
            note.save()
            self.add_note_to_listwidget(note)

    def delete_selected_note(self):
        selected_item = self.get_selected_lw_item()
        if selected_item: # if not None
            resultat = selected_item.note.delete() # delete from disk; API method
            if resultat:
                self.lw_notes.takeItem(
                    self.lw_notes.row(selected_item) # row from the lw
                ) # remove from lw

    def get_selected_lw_item(self):
        selected_items = self.lw_notes.selectedItems() # get all items selected
        if selected_items: # if list not empty
            return selected_items[0]
        return None

    def populate_notes(self):
        notes = get_notes()
        for note in notes:
            self.add_note_to_listwidget(note)

    def populate_note_content(self):
        selected_item = self.get_selected_lw_item()
        if selected_item:
            self.te_contenu.setText(selected_item.note.content)
        # if no item selected in the list, clear text edit not to show previous content
        else:
            self.te_contenu.clear()

    def save_note(self):
        selected_item = self.get_selected_lw_item()
        if selected_item:
            selected_item.note.content = self.te_contenu.toPlainText()
            selected_item.note.save()

