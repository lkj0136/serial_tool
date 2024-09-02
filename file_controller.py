import threading
import logging

class FileController:
    def __init__(self, serial_manager):
        self.serial_manager = serial_manager
        self.file_log = []
        self.stop_event = threading.Event()

    def send_file(self, port, file_path):
        self.stop_event.clear()
        threading.Thread(target=self._send_file, args=(port, file_path)).start()

    def _send_file(self, port, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if self.stop_event.is_set():
                        logging.info(f"File transfer to {port.name} stopped")
                        break
                    self.serial_manager.send_data(port, line)
            self.file_log.append((port, file_path))
        except Exception as e:
            logging.error(f"Failed to send file {file_path} to {port.name}: {e}")

    def stop_file_transfer(self):
        self.stop_event.set()
