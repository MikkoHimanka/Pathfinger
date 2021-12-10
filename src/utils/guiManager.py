from gui.infobar import Infobar

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from gui.mapEditor import MapEditor
from gui.pathViewer import PathViewer
from gui.sidebar import EditorSidebar, PathSidebar


class GUIManager:
    def __init__(self):
        self.infobar = Infobar()
        self.init_layout()
        self.show_visited = True
        self.show_path = True
        self.speed = 0.05

    def init_layout(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.child_layout = QHBoxLayout()
        self.child_layout.addWidget(QWidget())
        self.child_layout.addWidget(QWidget())

        self.infobar.setAutoFillBackground(True)
        self.infobar.setFixedHeight(20)
        self.infobar.setContentsMargins(10, 0, 0, 0)

        self.layout.addLayout(self.child_layout)
        self.layout.addWidget(self.infobar)

    def show_editor(self, data_manager):
        new_widget = MapEditor(self, data_manager)
        old_view_widget = self.get_widget(0)
        old_sidebar_widget = self.get_widget(1)

        self.child_layout.replaceWidget(old_view_widget, new_widget)
        self.child_layout.replaceWidget(old_sidebar_widget, EditorSidebar(self))

        old_view_widget.deleteLater()
        old_sidebar_widget.deleteLater()

    def show_pathfinding(self, data_manager):
        new_widget = PathViewer(self, data_manager)
        old_view_widget = self.get_widget(0)
        old_sidebar_widget = self.get_widget(1)

        self.child_layout.replaceWidget(old_view_widget, new_widget)
        self.child_layout.replaceWidget(old_sidebar_widget, PathSidebar(self))

        old_view_widget.deleteLater()
        old_sidebar_widget.deleteLater()

    def get_widget(self, index):
        return self.child_layout.itemAt(index).widget()
