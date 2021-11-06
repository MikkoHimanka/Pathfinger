from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction, QIcon

from gui.infobar import InfoBar
from gui.newMapWidget import NewMapWidget
from gui.mapPainter import MapPainter

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pathfinger")
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)

        self.initMenuBar()

        self.parentLayOut = QVBoxLayout()
        self.parentLayOut.setContentsMargins(0,0,0,0)
        self.parentLayOut.setSpacing(0)

        infobar = InfoBar()
        infobar.setAutoFillBackground(True)
        infobar.setFixedHeight(20)
        infobar.setContentsMargins(10, 0, 0, 0)

        self.new_map_widget = NewMapWidget(infobar, self)

        self.parentLayOut.addWidget(self.new_map_widget)
        self.parentLayOut.addWidget(infobar)

        main_widget = QWidget()
        main_widget.setLayout(self.parentLayOut)
        self.setCentralWidget(main_widget)

    def initMenuBar(self):
        menu = self.menuBar()
        file_tab = menu.addMenu("File")

        new_file_action = QAction(QIcon("assets/icons/icons8-new-file-16.png"), "New map", self)
        open_file_action = QAction("Open map", self)
        quit_app_action = QAction("Quit", self)

        file_tab.addAction(new_file_action)
        file_tab.addAction(open_file_action)
        file_tab.addSeparator()
        file_tab.addAction(quit_app_action)

    def createMap(self, size):
        new_map = MapPainter() 
        self.parentLayOut.replaceWidget(self.new_map_widget, new_map)
        
        self.new_map_widget.close()
        del self.new_map_widget
        