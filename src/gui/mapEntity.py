from math import sqrt

from PyQt6.QtGui import QPixmap, QImage, qRgb
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

#: qRgb-vastineet kartan arvoille
COLORS = {
    '0': qRgb(100,100,100),
    '1': qRgb(255,100,100)
}

class MapEntity(QLabel):
    '''Kayttoliittymaluokka kartan renderoimista varten'''

    def __init__(self, infobar, width, height):
        super().__init__()
        self.infobar = infobar
        self.map = ['0'] * width * height

        self.renderMap()

    def __init__(self, infobar, map_as_list):
        super().__init__()
        self.infobar = infobar
        self.map = map_as_list

        self.renderMap()

    def renderMap(self):
        '''Luo QPixmap-olion yksiulotteisesta listasta'''
        if len(self.map) > 0:
            self.map_length = int(sqrt(len(self.map)))

            self.image = self.imageFromList(self.map, self.map_length)
            self.pixmap: QPixmap = QPixmap(self.image)

            self.scalePixmap(self.pixmap)   
        else:
            self.pixmap = QPixmap()

    def imageFromList(self, arr, length):
        '''Generoi QImage-olion yksiulotteisesta listasta'''

        image = QImage(length, length, QImage.Format.Format_RGB32)

        for x in range(length):
            for y in range(length):
                value = arr[(y*length) + x]
                image.setPixel(x, y, COLORS[value])
                
        return image

    def scalePixmap(self, pixmap: QPixmap):
        '''Skaalaa kuvan mahdollisimman isoksi'''

        smaller = min(self.width(), self.height())
        self.setGeometry(0, 0, smaller, smaller)
        self.setPixmap(pixmap.scaled(smaller, smaller, Qt.AspectRatioMode.KeepAspectRatio))

    def resizeEvent(self, e):
        self.scalePixmap(self.pixmap)