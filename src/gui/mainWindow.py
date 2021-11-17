from PyQt6.QtWidgets import QFileDialog, QMainWindow, QWidget
from PyQt6.QtGui import QAction, QIcon

from gui.newMapWidget import NewMapWidget
from utils.dataManager import DataManager
from utils.guiManager import GUIManager

class MainWindow(QMainWindow):
    '''Kayttoliittymaluokka ikkunan hallintaan'''

    def __init__(self):
        super().__init__()
        self.gui_manager = GUIManager()
        self.data_manager = DataManager()
        self.setWindowTitle("Pathfinger")
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)
        self.initMenuBar()

        main_widget = QWidget()
        main_widget.setLayout(self.gui_manager.layout)
        self.setCentralWidget(main_widget)

    def initMenuBar(self):
        '''Alustaa sovelluksen ylapalkin'''

        menu = self.menuBar()
        file_tab = menu.addMenu("File")

        new_file_action = QAction(QIcon("assets/icons/icons8-new-file-16.png"), "New map", self)
        new_file_action.triggered.connect(self.showNewMapDialog)

        open_file_action = QAction("Open map", self)
        open_file_action.triggered.connect(self.showOpenMapDialog)

        quit_app_action = QAction("Quit", self)

        file_tab.addAction(new_file_action)
        file_tab.addAction(open_file_action)
        file_tab.addSeparator()
        file_tab.addAction(quit_app_action)

    def create_map(self, width, height):
        print("YAY!")

    def showNewMapDialog(self):
        self.popup = NewMapWidget(self)
        self.popup.show()

    def showOpenMapDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open map', 'assets/maps/', "CSV files (*.csv)")[0]
        if self.data_manager.openFile(filename, self.gui_manager.infobar):
            self.gui_manager.showEditor(self.data_manager)

    def showEditor(self):
        '''Vaihtaa nakymaksi karttaeditorin'''

        if not self.show_editor:
            self.layout.replaceWidget(self.path_widget, self.editor_widget)
    
    def showPathView(self):
        '''Vaihtaa nakymaksi polunetsinnan'''
        
        if self.show_editor:
            self.layout.replaceWidget(self.editor_widget, self.path_widget)