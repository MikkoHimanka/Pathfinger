from PyQt6.QtWidgets import (
    QPushButton,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt


class NewMapWidget(QWidget):
    """Kayttoliittymaluokka uuden kartan luomiseen"""

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.is_square = True
        self.infobar = window.gui_manager.infobar
        self.x_field = QLineEdit()
        self.y_field = QLineEdit()

        self.y_field.setReadOnly(True)
        self.y_field.setFixedWidth(60)
        self.x_field.setFixedWidth(60)
        self.x_field.textChanged.connect(self.parse_size)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.x_field)
        horizontal_layout.addWidget(QLabel("X"))
        horizontal_layout.addWidget(self.y_field)
        horizontal_layout.addStretch()

        self.new_map_button = QPushButton("Create")
        self.new_map_button.setFixedWidth(100)
        self.new_map_button.clicked.connect(self.create_map)
        self.new_map_button.setDisabled(True)

        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch()
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.new_map_button)
        vertical_layout.addStretch()
        vertical_layout.setAlignment(self.new_map_button, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vertical_layout)

    def parse_size(self, text):
        """Tarkistaa etta annettu koko on hyva numeerinen
        arvo ja kytkee "Create"-napin paalle tai pois"""

        try:
            value = int(text)
            if value < 8 or value > 512:
                raise ValueError()
            self.new_map_button.setDisabled(False)
            self.infobar.set_message("")
            self.y_field.setText(text)
        except ValueError:
            self.new_map_button.setDisabled(True)
            self.infobar.set_warning("A map must be in range of 8-256")

    def create_map(self):
        """Luo uuden kartan"""

        self.window.create_map(int(self.x_field.text()), int(self.y_field.text()))
