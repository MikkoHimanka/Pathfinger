from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPalette, QColor

class InfoBar(QLabel):
    def __init__(self):
        super().__init__()
        self.message_palette = self.palette()
        self.warning_palette = self.palette()
        self.message_palette.setColor(QPalette.ColorRole.Window, QColor(75,75,75,255))
        self.message_palette.setColor(QPalette.ColorRole.WindowText, QColor(255,255,255,255))

        self.warning_palette.setColor(QPalette.ColorRole.Window, QColor(75,75,75,255))
        self.warning_palette.setColor(QPalette.ColorRole.WindowText, QColor(255,75,75,255))

        self.setMessage("Ready")

    def setWarning(self, text):
        self.setPalette(self.warning_palette)
        self.setText(text)

    def setMessage(self, text):
        self.setPalette(self.message_palette)
        self.setText(text)
