from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

class NewMapWidget(QWidget):
    def __init__(self, infobar, parent):
        super().__init__()
        self.parent = parent
        self.is_square = True
        self.infobar = infobar
        self.x_field = QLineEdit()
        self.y_field = QLineEdit()

        self.y_field.setReadOnly(True)
        self.y_field.setFixedWidth(60)
        self.x_field.setFixedWidth(60)
        self.x_field.textChanged.connect(self.parseSize)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.x_field)
        horizontal_layout.addWidget(QLabel("X"))
        horizontal_layout.addWidget(self.y_field)
        horizontal_layout.addStretch()

        self.new_map_button = QPushButton("Create")
        self.new_map_button.setFixedWidth(100)
        self.new_map_button.clicked.connect(self.createMap)
        self.new_map_button.setDisabled(True)

        vertical_layout = QVBoxLayout()
        vertical_layout.addStretch()
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addWidget(self.new_map_button)
        vertical_layout.addStretch()
        vertical_layout.setAlignment(self.new_map_button, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(vertical_layout)

    def parseSize(self, text):
        try:
            value = int(text)
            if value < 8 or value > 256:
                raise ValueError()
            self.new_map_button.setDisabled(False)
            self.infobar.setMessage("")
            self.y_field.setText(text)
        except ValueError:
            self.new_map_button.setDisabled(True)
            self.infobar.setWarning("A map must be in range of 8-256")

    def createMap(self):
        self.parent.createMap(int(self.x_field.text()))
        