from PyQt6.QtWidgets import QFileDialog, QMainWindow, QWidget
from PyQt6.QtGui import QAction, QIcon

from gui.newMapWidget import NewMapWidget
from utils.dataManager import DataManager
from utils.guiManager import GUIManager


class MainWindow(QMainWindow):
    """Kayttoliittymaluokka ikkunan hallintaan"""

    def __init__(self):
        super().__init__()
        self.gui_manager = GUIManager(self)
        self.data_manager = DataManager()
        self.setWindowTitle("Pathfinger")
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)
        self.init_menu_bar()

        main_widget = QWidget()
        main_widget.setLayout(self.gui_manager.layout)
        self.setCentralWidget(main_widget)

    def init_menu_bar(self):
        """Alustaa sovelluksen ylapalkin"""

        menu = self.menuBar()
        file_tab = menu.addMenu("File")

        new_file_action = QAction(
            QIcon("assets/icons/icons8-new-file-16.png"), "New map", self
        )
        new_file_action.triggered.connect(self.show_new_map_dialog)

        open_file_action = QAction("Open map", self)
        open_file_action.triggered.connect(self.show_open_map_dialog)

        quit_app_action = QAction("Quit", self)

        file_tab.addAction(new_file_action)
        file_tab.addAction(open_file_action)
        file_tab.addSeparator()
        file_tab.addAction(quit_app_action)

    def create_map(self, width, height):
        self.data_manager.create_empty(width, height)
        self.gui_manager.show_editor(self.data_manager)
        self.popup.close()

    def show_new_map_dialog(self):
        self.popup = NewMapWidget(self)
        self.popup.show()

    def show_open_map_dialog(self):
        filename = QFileDialog.getOpenFileName(
            self, "Open map", "assets/maps/", "CSV files (*.csv);;MAP files (*.map);;All supported (*.csv *.map)"
        )[0]
        if self.data_manager.open_file(filename, self.gui_manager.infobar):
            self.gui_manager.show_editor(self.data_manager)
