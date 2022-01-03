from math import sqrt

from PyQt6.QtGui import QPixmap, qRgb
from PyQt6.QtWidgets import QLabel, QSizePolicy, QWidget
from PyQt6.QtCore import QThread, Qt, pyqtSignal

from gui.renderWorker import RenderWorker


class MapEntity(QLabel):
    """Kayttoliittymaluokka kartan renderoimista varten"""

    def __init__(self, gui_manager, data_manager):
        super().__init__()

        self.image = None
        self.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        )
        self.gui_manager = gui_manager
        self.infobar = gui_manager.infobar
        self.data_manager = data_manager
        self.map = data_manager.current_map
        self.render_thread = None

    def restore_image(self):
        self.render_worker.visited.clear()
        self.render_worker.path_nodes.clear()
        self.data_manager.clear_path()

    def render_map(self):
        """Aloittaa QImage-olion tekemisen toisella threadilla"""
        self.render_thread = QThread()
        self.render_worker = RenderWorker(
            self.map,
            self.data_manager.current_path,
            self.gui_manager.speed
        )
        self.render_worker.moveToThread(self.render_thread)

        self.render_thread.started.connect(self.render_worker.run)
        self.render_worker.finished.connect(self.render_thread.quit)
        self.render_worker.finished.connect(self.render_worker.deleteLater)
        self.render_thread.finished.connect(self.render_thread.deleteLater)
        self.render_worker.image_signal.connect(self.set_pixmap)

        self.render_thread.start()

    def set_pixmap(self, image):
        """Paivittaa widgetin QPixmap-olion"""
        self.image = image
        self.pixmap: QPixmap = QPixmap(self.image)
        self.scale_pixmap(self.pixmap)

    def scale_pixmap(self, pixmap: QPixmap):
        """Skaalaa kuvan mahdollisimman isoksi"""

        smaller = min(self.width(), self.height())
        self.setGeometry(0, 0, smaller, smaller)
        if self.image is not None:
            self.setPixmap(
                pixmap.scaled(smaller, smaller, Qt.AspectRatioMode.KeepAspectRatio)
            )

    def resizeEvent(self, e):  # noqa: N802
        """Kutsuu skaalausfunktiota, kun ikkunan kokoa muutetaan"""
        if self.image is not None:
            self.scale_pixmap(self.pixmap)
        QWidget.resizeEvent(self, e)

    def unscale_position(self, position):
        """Palauttaa vastaavat koordinaatit skaalaamattomalla kuvalla"""
        map_length = int(sqrt(len(self.data_manager.current_map)))

        new_position_x = int(position[0] / (self.width() / map_length))
        new_position_y = int(position[1] / (self.width() / map_length))
        return (new_position_x, new_position_y)
