from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QImage, qRgb

from time import sleep
from math import sqrt
from collections import Counter

#: qRgb-vastineet kartan arvoille ja nimetyille vareille
COLORS = {
    "0": qRgb(0, 0, 0),
    "1": qRgb(255, 100, 100),
    "yellow": qRgb(90, 90, 20),
    "green": qRgb(0, 200, 0),
}


class RenderWorker(QObject):
    finished = pyqtSignal()
    image_signal = pyqtSignal(QImage)

    def __init__(self, map_as_list, path, speed):
        super().__init__()
        self.image = self.image_from_list(map_as_list)
        self.path_nodes = []
        self.visited = []
        if path is not None:
            self.path_nodes = path.path
            self.visited = path.visited
        if len(self.visited) > 0:
            visited_amounts = Counter(self.visited)
            self.max_visited_amount = max(visited_amounts.values())
        self.speed = speed

    def set_stop(self, value):
        self.stop = value

    def run(self):
        self.image_signal.emit(self.image)

        for i in self.visited:
            self.set_pixel(i, "yellow")
            # self.lighten_pixel(self.visited[self.i])
            self.image_signal.emit(self.image)
            sleep(self.speed / 1000)

        self.set_pixels(self.path_nodes, "green")
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

    def lighten_pixel(self, coord):
        delta = int(256 / (self.max_visited_amount + 1)) if len(self.visited) > 0 else 0
        delta = max(delta, 5)
        old_color = self.image.pixelColor(coord[0], coord[1])
        new_color = qRgb(
            min(old_color.red() + delta, 255),
            min(old_color.green() + delta, 255),
            min(old_color.blue() + delta, 255)
        )
        self.image.setPixel(coord[0], coord[1], new_color)
