from PyQt6.QtGui import QPainter, QColor

from gui.mapEntity import MapEntity


class PathViewer(MapEntity):
    """Kayttoliittymaluokka polkujen etsintaa varten"""

    def __init__(self, gui_manager, data_manager):
        super().__init__(gui_manager, data_manager)
        self.data_manager.init_graph()
        self.current_algorithm = ""
        self.algo_selection_active = False
        self.points_selected = False
        self.points = [(-1, -1), (-1, -1)]
        self.painter = QPainter()
        self.render_map()

    def select_points(self, algorithm=None):
        self.restore_image()
        self.render_map()
        self.points = [(-1, -1), (-1, -1)]
        self.current_algorithm = None
        if algorithm is not None:
            self.current_algorithm = algorithm
        self.points_selected = False
        self.infobar.set_message("Select starting point")
        self.algo_selection_active = True

    def mousePressEvent(self, e):  # noqa: N802
        if self.algo_selection_active:
            mouse_position = (e.position().x(), e.position().y())
            if self.points[0] == (-1, -1):
                self.points[0] = self.unscale_position(mouse_position)
                self.infobar.set_message("Select end point")
            elif self.points[1] == (-1, -1):
                self.points[1] = self.unscale_position(mouse_position)
                self.infobar.clear()
                self.algo_selection_active = False
                self.points_selected = True
                if self.current_algorithm is not None:
                    self.data_manager.set_path(
                        self.current_algorithm, self.points
                    )
                    self.render_map()
                else:
                    self.data_manager.run_benchmark(self.points)
