from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPalette, QColor


class Infobar(QLabel):
    """Kayttoliittymaluokka infopalkkia varten"""

    def __init__(self):
        super().__init__()
        self.message_palette = self.palette()
        self.warning_palette = self.palette()
        self.message_palette.setColor(
            QPalette.ColorRole.Window, QColor(75, 75, 75, 255)
        )
        self.message_palette.setColor(
            QPalette.ColorRole.WindowText, QColor(255, 255, 255, 255)
        )

        self.warning_palette.setColor(
            QPalette.ColorRole.Window, QColor(75, 75, 75, 255)
        )
        self.warning_palette.setColor(
            QPalette.ColorRole.WindowText, QColor(255, 75, 75, 255)
        )

        self.set_message("Ready")

    def set_warning(self, text):
        """Asettaa palkkiin annetun tekstin punaisella"""

        self.setPalette(self.warning_palette)
        self.setText(text)

    def set_message(self, text):
        """Asettaa palkkiin annetun tekstin valkoisella"""

        self.setPalette(self.message_palette)
        self.setText(text)
