from math import sqrt

from PyQt6.QtGui import QPixmap, QImage, qRgb
from PyQt6.QtWidgets import QLabel, QSizePolicy
from PyQt6.QtCore import QObject, QThread, Qt, pyqtSignal

from time import sleep


#: qRgb-vastineet kartan arvoille ja nimetyille vareille
COLORS = {
    "0": qRgb(100, 100, 100),
    "1": qRgb(255, 100, 100),
    "yellow": qRgb(170, 170, 50),
    "green": qRgb(0, 200, 0),
}


class RenderWorker(QObject):
    finished = pyqtSignal()
    image_signal = pyqtSignal(QImage)

    def __init__(self, map_as_list, path, visited, speed, index=0):
        super().__init__()
        self.image = self.image_from_list(map_as_list)
        self.path = path
        self.visited = visited
        self.speed = speed
        self.i = index

    def run(self):
        self.image_signal.emit(self.image)

        while self.i < len(self.visited):
            self.set_pixel(self.visited[self.i], "yellow")
            self.image_signal.emit(self.image)
            sleep(self.speed / 1000)
            self.i += 1

        self.set_pixels(self.path, "green")
        self.image_signal.emit(self.image)

        self.finished.emit()

    def image_from_list(self, arr):
        """Generoi QImage-olion yksiulotteisesta listasta"""

        length = int(sqrt(len(arr)))
        image = QImage(length, length, QImage.Format.Format_RGB32)

        for x in range(length):
            for y in range(length):
                value = arr[(y * length) + x]
                image.setPixel(x, y, COLORS[value])

        return image

    def set_pixels(self, coordinates, color):
        for coord in coordinates:
            self.image.setPixel(coord[0], coord[1], COLORS[color])

    def set_pixel(self, coord, color):
        self.image.setPixel(coord[0], coord[1], COLORS[color])


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
        self.render_map()

    def restore_image(self):
        self.data_manager.clear_path()

    def render_map(self):
        """Aloittaa QImage-olion tekemisen toisella threadilla"""
        self.render_thread = QThread()
        self.render_worker = RenderWorker(
            self.map,
            self.data_manager.current_path,
            self.data_manager.current_visited,
            self.gui_manager.speed
        )
        self.render_worker.moveToThread(self.render_thread)

        self.render_thread.started.connect(self.render_worker.run)
        self.render_worker.finished.connect(self.render_thread.quit)
        self.render_worker.finished.connect(self.render_worker.deleteLater)
        self.render_thread.finished.connect(self.render_thread.deleteLater)
        self.render_worker.image_signal.connect(self.set_pixmap)

        self.render_thread.start()

    def lighten_pixel(self, image, coord):
        old_color = image.pixelColor(coord[0], coord[1])
        new_color = qRgb(old_color.red() + 10, old_color.green() + 10, old_color.blue() + 10)
        image.setPixel(coord[0], coord[1], new_color)

    def set_pixmap(self, image):
        """Paivittaa widgetin QPixmap-olion"""
        self.image = image
        self.pixmap: QPixmap = QPixmap(self.image)
        self.scale_pixmap(self.pixmap)

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
        if self.image is not None:
            self.setPixmap(
                pixmap.scaled(smaller, smaller, Qt.AspectRatioMode.KeepAspectRatio)
            )

    def resizeEvent(self, e):  # noqa: N802
        """Kutsuu skaalausfunktiota, kun ikkunan kokoa muutetaan"""
        if self.image is not None:
            self.scale_pixmap(self.pixmap)

    def unscale_position(self, position):
        """Palauttaa vastaavat koordinaatit skaalaamattomalla kuvalla"""
        map_length = int(sqrt(len(self.data_manager.current_map)))

        new_position_x = int(position[0] / (self.width() / map_length))
        new_position_y = int(position[1] / (self.width() / map_length))
        return (new_position_x, new_position_y)
