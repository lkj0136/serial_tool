import threading
from PyQt5.QtCore import pyqtSignal, QObject

class DataController(QObject):
    data_received = pyqtSignal(str)

    def __init__(self, serial_manager):
        super().__init__()
        self.serial_manager = serial_manager
        self.data_log = []

    def send_data(self, port, data):
        threading.Thread(target=self.serial_manager.send_data, args=(port, data)).start()
        self.data_log.append((port, data))

    def receive_data(self, port):
        threading.Thread(target=self._receive_data, args=(port,)).start()

    def _receive_data(self, port):
        while port.is_open:
            data = self.serial_manager.receive_data(port)
            if data:
                self.data_log.append((port, data))
                self.data_received.emit(data)  # UI 업데이트 로직
