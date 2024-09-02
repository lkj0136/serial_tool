from models.automation import AutomationScript

class AutomationController:
    def __init__(self, serial_manager):
        self.script = AutomationScript(serial_manager)

    def start_script(self, interval, data):
        self.script.start_script(interval, data)

    def stop_script(self):
        self.script.stop_script()
