from functools import partial

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout,       # main parts
    QToolBar, QTreeView, QListView, QSlider, # actual widgets
    QHeaderView, QFileSystemModel            # system
)


# noinspection PyAttributeOutsideInit
class MainWindow(QMainWindow):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setWindowTitle("PyExplorer")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.add_actions_to_toolbar()
        self.setup_connections()
        self.create_file_model()

    def create_widgets(self):
        self.toolbar = QToolBar()
        self.tree_view = QTreeView()
        self.list_view = QListView()
        self.sld_iconSize = QSlider()
        self.main_widget = QWidget() # central widget in the main window

    def modify_widgets(self):
        css_file = self.ctx.get_resource("style.css") # use of application context
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())
        ### icons
        self.list_view.setViewMode(QListView.IconMode) # icons instead of list
        self.list_view.setUniformItemSizes(True) # reduce text under the icons
        self.list_view.setIconSize(QtCore.QSize(48, 48)) # Qt Core Size required
        self.sld_iconSize.setRange(48, 256) # min and max values for slider, i.e., icon size
        self.sld_iconSize.setValue(48) # default value
        ### tree view
        self.tree_view.setSortingEnabled(True) # sort alphabetical
        self.tree_view.setAlternatingRowColors(True) # alternating color for consecutive rows
        self.tree_view.header().setSectionResizeMode(
            QHeaderView.ResizeToContents) # resize header of the tree view to content

    def create_layouts(self):
        self.main_layout = QHBoxLayout(self.main_widget) # toolbar is "floating"

    def add_widgets_to_layouts(self):
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar) # default top location
        
        self.setCentralWidget(self.main_widget)
        
        self.main_layout.addWidget(self.tree_view)
        self.main_layout.addWidget(self.list_view)
        self.main_layout.addWidget(self.sld_iconSize)

    def add_actions_to_toolbar(self):
        # use the main directories
        locations = ["home", "desktop", "documents", "movies", "pictures", "music"]
        for location in locations:
            icon = self.ctx.get_resource(f"{location}.svg") # look up ./resources/base/
            action = self.toolbar.addAction(QtGui.QIcon(icon), location.capitalize()) # tooltip
            action.triggered.connect(partial(self.change_location, location))

    def setup_connections(self):
        self.tree_view.clicked.connect(self.treeview_clicked)
        self.list_view.clicked.connect(self.listview_clicked)
        self.list_view.doubleClicked.connect(self.listview_double_clicked)
        self.sld_iconSize.valueChanged.connect(self.change_icon_size) # slider

    def change_icon_size(self, value):
        self.list_view.setIconSize(QtCore.QSize(value, value))

    def change_location(self, location):
        # see also https://doc.qt.io/qt-6/qstandardpaths.html
        path = eval(f"QtCore.QStandardPaths().standardLocations(QtCore.QStandardPaths.{location.capitalize()}Location)")
        path = path[0] # path is a list of paths, e.g., temp may have multiple directories
        self.tree_view.setRootIndex(self.model.index(path))
        self.list_view.setRootIndex(self.model.index(path))

    def create_file_model(self):
        # same model for both views -> synchronization
        self.model = QFileSystemModel() # tree management
        root_path = QtCore.QDir.rootPath() # root path
        self.model.setRootPath(root_path) # root in the model
        self.tree_view.setModel(self.model)
        self.list_view.setModel(self.model)
        self.list_view.setRootIndex(self.model.index(root_path)) # starting point of the lv
        self.tree_view.setRootIndex(self.model.index(root_path)) # starting point of the tv

    def treeview_clicked(self, index):
        """
        Update the content of the listView depending on the item selected in the treeView.
        """
        # QModelIndex returned by the click signal, e.g., (3,0,0x755148660,QFileSystemModel(...))
        if self.model.isDir(index):
            self.list_view.setRootIndex(index)
        else:
            # if file clicked, show its parent directory
            self.list_view.setRootIndex(index.parent())

    def listview_clicked(self, index):
        """
        Update the content of the treeView depending on the item selected in the listView.
        """
        selection_model = self.tree_view.selectionModel()
        selection_model.setCurrentIndex(index, QtCore.QItemSelectionModel.ClearAndSelect)

    def listview_double_clicked(self, index):
        self.list_view.setRootIndex(index)
