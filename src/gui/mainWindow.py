from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction, QIcon

from gui.infobar import Infobar
from gui.mapEditor import MapEditor
from gui.newMapWidget import NewMapWidget
from gui.pathViewer import PathViewer

class MainWindow(QMainWindow):
    '''Kayttoliittymaluokka ikkunan hallintaan'''

    def __init__(self):
        super().__init__()
        self.show_editor = True
        self.setWindowTitle("Pathfinger")
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)

        self.initMenuBar()

        self.parentLayOut = QVBoxLayout()
        self.parentLayOut.setContentsMargins(0,0,0,0)
        self.parentLayOut.setSpacing(0)

        infobar = Infobar()
        infobar.setAutoFillBackground(True)
        infobar.setFixedHeight(20)
        infobar.setContentsMargins(10, 0, 0, 0)
        
        self.editor_widget = MapEditor(infobar, 'assets/maps/map1.csv')
        #self.path_widget = PathViewer(infobar)

        self.parentLayOut.addWidget(self.editor_widget)

        self.parentLayOut.addWidget(infobar)

        main_widget = QWidget()
        main_widget.setLayout(self.parentLayOut)
        self.setCentralWidget(main_widget)

    def initMenuBar(self):
        '''Alustaa sovelluksen ylapalkin'''

        menu = self.menuBar()
        file_tab = menu.addMenu("File")

        new_file_action = QAction(QIcon("assets/icons/icons8-new-file-16.png"), "New map", self)
        open_file_action = QAction("Open map", self)
        quit_app_action = QAction("Quit", self)

        file_tab.addAction(new_file_action)
        file_tab.addAction(open_file_action)
        file_tab.addSeparator()
        file_tab.addAction(quit_app_action)

    def createMap(self, width, height):
        pass
        

    def showEditor(self):
        '''Vaihtaa nakymaksi karttaeditorin'''

        if not self.show_editor:
            self.layout.replaceWidget(self.path_widget, self.editor_widget)
    
    def showPathView(self):
        '''Vaihtaa nakymaksi polunetsinnan'''
        
        if self.show_editor:
            self.layout.replaceWidget(self.editor_widget, self.path_widget)