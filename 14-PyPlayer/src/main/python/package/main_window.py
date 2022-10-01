from functools import partial

from PySide6.QtCore import QSize, QStandardPaths # looks to system directories
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget

from PySide6.QtWidgets import (
    QMainWindow, QToolBar, QStyle,
    QFileDialog, QDialog
)

### Note on major changes in recent versions of Qt: https://www.qt.io/blog/qt-multimedia-in-qt-6


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPlayer")

        # default icons included in PySide
        self.open_icon = self.style().standardIcon(QStyle.SP_DriveDVDIcon)
        self.play_icon = self.style().standardIcon(QStyle.SP_MediaPlay)
        self.previous_icon = self.style().standardIcon(QStyle.SP_MediaSkipBackward)
        self.pause_icon = self.style().standardIcon(QStyle.SP_MediaPause)
        self.stop_icon = self.style().standardIcon(QStyle.SP_MediaStop)

        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.video_widget = QVideoWidget() # reads the video
        self.player = QMediaPlayer() # actual player widget
        self.file_menu = self.menuBar().addMenu("Fichier") # menuBar empty at init
        # Note: menuBar could not be seen on some OSs when empty
        self.toolbar = QToolBar() # floating toolbar

        # ACTIONS
        # file menu
        self.act_open = self.file_menu.addAction(self.open_icon, "Ouvrir") # create and add action to menu
        self.act_open.setShortcut("Ctrl+O") # PySide adapt "Ctrl" to the OS automatically
        
        # toolbar
        self.act_play = self.toolbar.addAction(self.play_icon, "Lire")
        self.act_previous = self.toolbar.addAction(self.previous_icon, "Revenir au début")
        self.act_pause = self.toolbar.addAction(self.pause_icon, "Pause")
        self.act_stop = self.toolbar.addAction(self.stop_icon, "Stop")

    def add_widgets_to_layouts(self):
        self.addToolBar(self.toolbar) # Adds the toolbar into the specified area in this main window
        self.setCentralWidget(self.video_widget) # Sets the given widget to be the main window's central widget
        self.player.setVideoOutput(self.video_widget) # link player to video widget
        # Note: A media player can only have one video output attached,
        # so setting this property will replace the previously connected video output.

    def setup_connections(self):
        self.act_open.triggered.connect(self.open_file)
        self.act_play.triggered.connect(self.play)
        self.act_pause.triggered.connect(self.player.pause)
        self.act_stop.triggered.connect(self.player.stop)
        self.act_previous.triggered.connect(
            partial( # doesn't call the method without action, send args to a method with partial
                self.player.setPosition, 0) # beginning of the video
            )
        # self.player.stateChanged.connect(self.update_buttons) # called whenever a button state changes
        self.player.playbackStateChanged.connect(self.update_buttons) # called whenever a button state changes

    def play(self):
        self.player.play()
        self.video_widget.resize(QSize(1, 1)) # refresh size at the end of the video

    def open_file(self):
        file_dialog = QFileDialog(self)
        file_dialog.setMimeTypeFilters(["video/mp4"]) # ~filters
        # see also https://www.oreilly.com/library/view/web-design-in/1565925157/ch04s05.html
        
        movies_dir = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_dir) # "home" user directory by default
        if file_dialog.exec() == QDialog.Accepted:
            # emitted when the dialog has been accepted either by the user or by calling accept() or done()
            movie = file_dialog.selectedUrls()[0]
            # self.player.setMedia(movie)
            self.player.setSource(movie) # new in PyQt6/PySide6
            self.player.play()

    def update_buttons(self, state):
        # e.g., we should't be able to activate play or pause if they're already activated
        # print(state) # e.g., PySide6.QtMultimedia.QMediaPlayer.State.PlayingState
        # QAction::setDisabled(bool b)
        self.act_play.setDisabled(state == QMediaPlayer.PlayingState)
        self.act_pause.setDisabled(state ==QMediaPlayer.PausedState)
        self.act_stop.setDisabled(state == QMediaPlayer.StoppedState)
