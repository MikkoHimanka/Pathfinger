import PyQt6
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QCheckBox, QComboBox, QFormLayout, QLabel, QPushButton, QSlider, QWidget

from gui.pathViewer import PathViewer


class EditorSidebar(QWidget):
    def __init__(self, gui_manager):
        super().__init__()
        self.gui_manager = gui_manager

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(10, 10, 10))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setMinimumWidth(300)

        self.find_path_button = QPushButton("Find path from A to B")

        path_view_button = QPushButton("Path finding")
        path_view_button.clicked.connect(
            lambda: self.gui_manager.show_pathfinding(self.window().data_manager)
        )

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
        palette.setColor(QPalette.ColorRole.Window, QColor(10, 10, 10))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setMinimumWidth(300)

        path_view_button = QPushButton("Map editor")
        path_view_button.clicked.connect(
            lambda: self.gui_manager.show_editor(self.window().data_manager)
        )

        algo_select_dropdown = self.init_algo_selection()

        find_path_button = QPushButton("Find path")
        find_path_button.clicked.connect(
            lambda: self.gui_manager.get_widget(0).select_points(
                algo_select_dropdown.currentText()
            )
        )

        self.allow_diagonal = QCheckBox("Allow diagonal movement")
        self.allow_diagonal.stateChanged.connect(
            lambda: self.window().data_manager.set_diagonal(self.allow_diagonal.isChecked())
        )

        speed_slider = QSlider(PyQt6.QtCore.Qt.Orientation.Horizontal)
        speed_slider.setMinimum(-100)
        speed_slider.setMaximum(-1)
        speed_slider.setSingleStep(1)
        speed_slider.setValue(-50)
        speed_slider.valueChanged.connect(
            self.change_speed
        )

        benchmark_button = QPushButton("Benchmark")
        benchmark_button.clicked.connect(self.gui_manager.handle_benchmark)

        layout = QFormLayout()
        layout.addRow(QLabel("Path finding"))
        layout.addRow(path_view_button)
        layout.addRow(algo_select_dropdown)
        layout.addRow(find_path_button)
        layout.addRow(self.allow_diagonal)
        layout.addRow(speed_slider)
        layout.addRow(benchmark_button)

        self.setLayout(layout)

    def init_algo_selection(self):
        select_algo_menu = QComboBox(self)
        select_algo_menu.addItem("Dijkstra")
        select_algo_menu.addItem("Greedy Best-First")
        select_algo_menu.addItem("A*")
        # select_algo_menu.addItem("IDA*")
        select_algo_menu.addItem("JPS")

        select_algo_menu.currentTextChanged.connect(self.handle_algo_select)

        return select_algo_menu

    def change_speed(self, value):
        self.gui_manager.speed = abs(value)

    def handle_algo_select(self, value):
        if value == "JPS":
            self.allow_diagonal.setChecked(True)
            self.allow_diagonal.hide()
        else:
            self.allow_diagonal.show()
