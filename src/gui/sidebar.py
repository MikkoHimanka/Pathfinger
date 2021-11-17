from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QComboBox, QFormLayout, QLabel, QPushButton, QWidget

class EditorSidebar(QWidget):
    def __init__(self, gui_manager):
        super().__init__()
        self.gui_manager = gui_manager

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(10,10,10))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255,255,255))
        self.setPalette(palette)
        self.setMinimumWidth(300)

        self.find_path_button = QPushButton("Find path from A to B")
        

        path_view_button = QPushButton("Path finding")
        path_view_button.clicked.connect(lambda: self.gui_manager.showPathfinding(self.window().data_manager))

        layout = QFormLayout()
        layout.addRow(QLabel("Map editor"))
        layout.addRow(path_view_button)

        self.setLayout(layout)


class PathSidebar(QWidget):
    def __init__(self, gui_manager):
        super().__init__()
        self.gui_manager = gui_manager

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(10,10,10))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255,255,255))
        self.setPalette(palette)
        self.setMinimumWidth(300)

        path_view_button = QPushButton("Map editor")
        path_view_button.clicked.connect(lambda: self.gui_manager.showEditor(self.window().data_manager))
        
        algo_select_dropdown = self.initAlgoSelection()

        find_path_button = QPushButton("Find path")
        find_path_button.clicked.connect(lambda: self.gui_manager.getWidget(0).selectPoints(algo_select_dropdown.currentText()))

        layout = QFormLayout()
        layout.addRow(QLabel("Path finding"))
        layout.addRow(path_view_button)
        layout.addRow(algo_select_dropdown)
        layout.addRow(find_path_button)

        self.setLayout(layout)

    def initAlgoSelection(self):
        select_algo_menu = QComboBox(self)
        select_algo_menu.addItem("Dijkstra")
        select_algo_menu.addItem("Another one")
        
        return select_algo_menu
