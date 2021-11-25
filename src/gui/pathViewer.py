from PyQt6.QtGui import QPainter, QColor

from gui.mapEntity import MapEntity

from pathfinding.pathManager import PathManager


class PathViewer(MapEntity):
    """Kayttoliittymaluokka polkujen etsintaa varten"""

    def __init__(self, gui_manager, data_manager):
        super().__init__(gui_manager, data_manager)
        self.current_algorithm = ""
        self.selection_active = False
        self.points_selected = False
        self.points = [(-1, -1), (-1, -1)]
        self.painter = QPainter()
        self.path_manager = PathManager(self.map)

    def select_points(self, algorithm):
        self.restore_image()
        self.data_manager.clear_path()
        self.current_algorithm = algorithm
        self.points = [(-1, -1), (-1, -1)]
        self.points_selected = False

        self.infobar.set_message("Select starting point")
        self.selection_active = True

    def mousePressEvent(self, e):  # noqa: N802
        if self.selection_active:
            mouse_position = (e.position().x(), e.position().y())
            if self.points[0] == (-1, -1):
                self.points[0] = self.unscale_position(mouse_position)
                self.infobar.set_message("Select end point")
            elif self.points[1] == (-1, -1):
                self.points[1] = self.unscale_position(mouse_position)
                self.infobar.clear()
                self.selection_active = False
                self.points_selected = True
                self.path = self.path_manager.get_path(
                    self.current_algorithm, self.points
                )

    def paintEvent(self, e):  # noqa: N802
        super().paintEvent(e)
        if not self.selection_active and self.points_selected:
            if len(self.path) < 2:
                self.infobar.set_warning("No path found")
                return

            self.painter.begin(self.pixmap)
            self.painter.setPen(QColor(0, 255, 0, 255))

            for i in range(len(self.path) - 1):
                self.painter.drawLine(
                    self.path[i][0],
                    self.path[i][1],
                    self.path[i + 1][0],
                    self.path[i + 1][1],
                )

            self.painter.end()
