from PyQt5.QtWidgets import QMainWindow
from ui.main_window import MainWindow
from models.serial_manager import SerialManager
from controllers.port_controller import PortController
from controllers.data_controller import DataController
from controllers.file_controller import FileController
from controllers.automation_controller import AutomationController
from controllers.profile_controller import ProfileController


class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.serial_manager = SerialManager()
        self.port_controller = PortController(self.serial_manager)
        self.data_controller = DataController(self.serial_manager)
        self.file_controller = FileController(self.serial_manager)
        self.automation_controller = AutomationController(self.serial_manager)
        self.profile_controller = ProfileController()
        self.main_window = MainWindow()
        self.main_window.show()

        self.main_window.port_settings.open_button.clicked.connect(self.open_ports)
        self.main_window.port_settings.close_button.clicked.connect(self.close_ports)
        self.main_window.profile_settings.save_button.clicked.connect(self.save_profile)
        self.main_window.profile_settings.load_button.clicked.connect(self.load_profile)

        self.data_controller.data_received.connect(self.update_received_data)

    def open_ports(self):
        port_name = self.main_window.port_settings.port_combo.currentText()
        baudrate = int(self.main_window.port_settings.baudrate_combo.currentText())
        self.port_controller.open_port(port_name, baudrate)

    def close_ports(self):
        self.port_controller.close_ports()

    def save_profile(self):
        profile_name = self.main_window.profile_settings.profile_name_input.text()
        settings = {
            "port": self.main_window.port_settings.port_combo.currentText(),
            "baudrate": self.main_window.port_settings.baudrate_combo.currentText()
        }
        self.profile_controller.save_profile(profile_name, settings)

    def load_profile(self):
        profile_name = self.main_window.profile_settings.profile_name_input.text()
        settings = self.profile_controller.load_profile(profile_name)
        if settings:
            self.main_window.port_settings.port_combo.setCurrentText(settings["port"])
            self.main_window.port_settings.baudrate_combo.setCurrentText(settings["baudrate"])

    def update_received_data(self, data):
        self.main_window.data_transfer.received_data.append(data)
