from models.port import Port

class PortController:
    def __init__(self, serial_manager):
        self.serial_manager = serial_manager

    def add_port(self, name, baudrate, databits, stopbits, parity):
        port = Port(name, baudrate, databits, stopbits, parity)
        self.serial_manager.ports.append(port)

    def open_port(self, port_name, baudrate):
        self.serial_manager.open_port(port_name, baudrate)

    def close_ports(self):
        self.serial_manager.close_ports()
