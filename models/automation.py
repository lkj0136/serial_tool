import threading
import time

class AutomationScript:
    def __init__(self, serial_manager):
        self.serial_manager = serial_manager
        self.running = False

    def start_script(self, interval, data):
        self.running = True
        self.thread = threading.Thread(target=self.run_script, args=(interval, data))
        self.thread.start()

    def run_script(self, interval, data):
        while self.running:
            for port in self.serial_manager.ports:
                if port.is_open:
                    self.serial_manager.send_data(port, data)
            time.sleep(interval)

    def stop_script(self):
        self.running = False
        self.thread.join()
