from PyQt6.QtGui import QPixmap
from gui.mapEntity import MapEntity


class MapEditor(MapEntity):
    """Kayttoliittymaluokka kartan piirtamista varten"""

    def __init__(self, gui_manager, data_manager):
        super().__init__(gui_manager, data_manager)
        self.brush = ""

    def mouseMoveEvent(self, e):  # noqa: N802
        """Asettaa pensselin arvoksi vastakkaisen kartan arvon
        ('0' -> '1' / '1' -> '0') ja asettaa sen listaan"""

        position = self.unscale_position((e.position().x(), e.position().y()))

        if (
            position[0] < self.map_length
            and position[1] < self.map_length
            and position[0] >= 0
            and position[1] >= 0
        ):
            map_index = (position[1] * self.map_length) + position[0]

            if self.brush == "":
                self.brush = "1" if self.map[map_index] == "0" else "0"

            self.map[map_index] = self.brush

    def mouseReleaseEvent(self, e):  # noqa: N802
        """Paivittaa kuvan ja nollaa pensselin arvon"""

        self.image = self.image_from_list(self.map, self.map_length)
        self.pixmap: QPixmap = QPixmap(self.image)

        self.scale_pixmap(self.pixmap)

        self.brush = ""

        self.data_manager.map_changed = True
