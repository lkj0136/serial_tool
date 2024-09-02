from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from ui.port_settings import PortSettings
from ui.data_transfer import DataTransfer
from ui.file_transfer import FileTransfer
from ui.status_bar import StatusBar
from ui.profile_settings import ProfileSettings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Manager")
        self.setGeometry(100, 100, 800, 600)

        self.port_settings = PortSettings()
        self.data_transfer = DataTransfer()
        self.file_transfer = FileTransfer()
        self.status_bar = StatusBar()
        self.profile_settings = ProfileSettings()

        layout = QVBoxLayout()
        layout.addWidget(self.port_settings)
        layout.addWidget(self.data_transfer)
        layout.addWidget(self.file_transfer)
        layout.addWidget(self.profile_settings)
        layout.addWidget(self.status_bar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
