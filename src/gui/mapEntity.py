from math import sqrt

from PyQt6.QtGui import QPixmap, QImage, qRgb
from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtCore import Qt


#: qRgb-vastineet kartan arvoille
COLORS = {
    "0": qRgb(100, 100, 100),
    "1": qRgb(255, 100, 100),
    "yellow": qRgb(170, 170, 50),
    "green": qRgb(0, 200, 0),
}


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
        data_manager.path_manager.map_changed = True
        self.gui_manager = gui_manager
        self.infobar = gui_manager.infobar
        self.data_manager = data_manager
        self.map = data_manager.current_map
        self.render_map()

    def restore_image(self):
        self.map = self.data_manager.current_map
        self.render_map()

    def render_map(self):
        """Luo QPixmap-olion yksiulotteisesta listasta"""
        if len(self.map) > 0:
            self.map_length = int(sqrt(len(self.map)))

            self.image = self.image_from_list(self.map, self.map_length)
            self.data_manager.init_graph()

            if self.gui_manager.show_visited:
                self.set_pixels(
                    self.image,
                    self.data_manager.current_visited,
                    "yellow",
                )
            if self.gui_manager.show_path:
                self.set_pixels(
                    self.image,
                    self.data_manager.current_path,
                    "green"
                )

            self.pixmap: QPixmap = QPixmap(self.image)
            self.scale_pixmap(self.pixmap)
        else:
            self.pixmap = QPixmap()

        self.data_manager.map_changed = False
        self.data_manager.path_changed = False

    def set_pixels(self, image, coordinates, color):
        for coord in coordinates:
            image.setPixel(coord[0], coord[1], COLORS[color])

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
