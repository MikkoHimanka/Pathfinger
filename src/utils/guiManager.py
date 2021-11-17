from gui.infobar import Infobar

from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

from gui.mapEditor import MapEditor
from gui.pathViewer import PathViewer
from gui.sidebar import EditorSidebar, PathSidebar

class GUIManager():
    def __init__(self):
        self.infobar = Infobar()
        self.init_layout()

    def init_layout(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)

        self.childLayout = QHBoxLayout()
        self.childLayout.addWidget(QWidget())
        self.childLayout.addWidget(QWidget())

        self.infobar.setAutoFillBackground(True)
        self.infobar.setFixedHeight(20)
        self.infobar.setContentsMargins(10, 0, 0, 0)

        self.layout.addLayout(self.childLayout)
        self.layout.addWidget(self.infobar)

    def showEditor(self, data_manager):
        new_widget = MapEditor(self, data_manager)
        old_view_widget = self.getWidget(0)
        old_sidebar_widget = self.getWidget(1)
        
        self.childLayout.replaceWidget(old_view_widget, new_widget)
        self.childLayout.replaceWidget(old_sidebar_widget, EditorSidebar(self))

        old_view_widget.deleteLater()
        old_sidebar_widget.deleteLater()

    def showPathfinding(self, data_manager):
        new_widget = PathViewer(self, data_manager)
        old_view_widget = self.getWidget(0)
        old_sidebar_widget = self.getWidget(1)

        self.childLayout.replaceWidget(old_view_widget, new_widget)
        self.childLayout.replaceWidget(old_sidebar_widget, PathSidebar(self))

        old_view_widget.deleteLater()
        old_sidebar_widget.deleteLater()

    def getWidget(self, index):
        return self.childLayout.itemAt(index).widget()
