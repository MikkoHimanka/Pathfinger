from PyQt6.QtGui import QPixmap
from gui.mapEntity import MapEntity
from utils.CSVManager import CSVManager

class MapEditor(MapEntity):
    '''Kayttoliittymaluokka kartan piirtamista varten'''

    def __init__(self, gui_manager, data_manager):
        super().__init__(gui_manager, data_manager)
        self.brush = ''

    def mouseMoveEvent(self, e):
        '''Asettaa pensselin arvoksi vastakkaisen kartan arvon ('0' -> '1' / '1' -> '0') ja asettaa sen listaan'''

        position = self.unscalePosition((e.position().x(), e.position().y()))

        if (position[0] < self.map_length and position[1] < self.map_length
            and position[0] >= 0 and position[1] >= 0):
            map_index = (position[1]*self.map_length) + position[0]

            if self.brush == '':
                self.brush = '1' if self.map[map_index] == '0' else '0'
            
            self.map[map_index] = self.brush

    def mouseReleaseEvent(self, e):
        '''Paivittaa kuvan ja nollaa pensselin arvon'''

        self.image = self.imageFromList(self.map, self.map_length)
        self.pixmap: QPixmap = QPixmap(self.image)

        self.scalePixmap(self.pixmap)   

        self.brush = ''
