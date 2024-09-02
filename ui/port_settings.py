from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton


class PortSettings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.port_label = QLabel("Port:")
        self.port_combo = QComboBox()
        self.port_combo.addItems(["NONE", "COM1", "COM2", "COM3", "COM4"])

        self.baudrate_label = QLabel("Baudrate:")
        self.baudrate_combo = QComboBox()
        self.baudrate_combo.addItems(["9600", "19200", "115200"])

        self.open_button = QPushButton("Open Ports")
        self.close_button = QPushButton("Close Ports")

        layout.addWidget(self.port_label)
        layout.addWidget(self.port_combo)
        layout.addWidget(self.baudrate_label)
        layout.addWidget(self.baudrate_combo)
        layout.addWidget(self.open_button)
        layout.addWidget(self.close_button)

        self.setLayout(layout)
