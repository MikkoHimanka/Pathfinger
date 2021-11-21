from math import sqrt

from PyQt6.QtGui import QPixmap, QImage, qRgb
from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtCore import Qt

#: qRgb-vastineet kartan arvoille
COLORS = {"0": qRgb(100, 100, 100), "1": qRgb(255, 100, 100)}


class MapEntity(QLabel):
    """Kayttoliittymaluokka kartan renderoimista varten"""

    # def __init__(self, gui_manager, width, height):
    #     super().__init__()
    #     self.infobar = gui_manager.infobar
    #     self.map = ["0"] * width * height

    #     self.renderMap()

    def __init__(self, gui_manager, data_manager):
        super().__init__()

        self.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        )
        self.infobar = gui_manager.infobar
        self.data_manager = data_manager
        self.map = data_manager.current_map
        self.render_map()

    def render_map(self):
        """Luo QPixmap-olion yksiulotteisesta listasta"""
        if len(self.map) > 0:
            self.map_length = int(sqrt(len(self.map)))

            self.image = self.image_from_list(self.map, self.map_length)
            self.pixmap: QPixmap = QPixmap(self.image)

            self.scale_pixmap(self.pixmap)
        else:
            self.pixmap = QPixmap()

    def image_from_list(self, arr, length):
        """Generoi QImage-olion yksiulotteisesta listasta"""

        image = QImage(length, length, QImage.Format.Format_RGB32)

        for x in range(length):
            for y in range(length):
                value = arr[(y * length) + x]
                image.setPixel(x, y, COLORS[value])

        return image

    def scale_pixmap(self, pixmap: QPixmap):
        """Skaalaa kuvan mahdollisimman isoksi"""

        smaller = min(self.width(), self.height())
        self.setGeometry(0, 0, smaller, smaller)
        self.setPixmap(
            pixmap.scaled(smaller, smaller, Qt.AspectRatioMode.KeepAspectRatio)
        )

    def resizeEvent(self, e):  # noqa: N802
        self.scale_pixmap(self.pixmap)

    def unscale_position(self, position):
        """Palauttaa vastaavat koordinaatit skaalaamattomalla kuvalla"""

        new_position_x = int(position[0] / (self.width() / self.map_length))
        new_position_y = int(position[1] / (self.width() / self.map_length))
        return (new_position_x, new_position_y)
