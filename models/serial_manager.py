import serial
import threading
import logging
from configparser import ConfigParser
from utils.notification import show_notification


class SerialManager:
    def __init__(self):
        self.ports = []
        self.config = ConfigParser()
        self.load_config()

    def load_config(self):
        self.config.read('config.ini')
        # Load port settings from config file

    def save_config(self):
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
        # Save port settings to config file

    def open_port(self, port_name, baudrate):
        try:
            port = serial.Serial(port_name, baudrate)
            self.ports.append(port)
            logging.info(f"Opened port {port_name} at {baudrate} baudrate")
            self.notify_port_status(f"Port {port_name} opened at {baudrate} baudrate")
        except Exception as e:
            logging.error(f"Failed to open port {port_name}: {e}")
            self.notify_port_status(f"Failed to open port {port_name}: {e}")

    def close_ports(self):
        for port in self.ports:
            port.close()
            logging.info(f"Closed port {port.name}")
            self.notify_port_status(f"Port {port.name} closed")
        self.ports = []

    def send_data(self, port, data):
        try:
            port.write(data.encode())
            logging.info(f"Sent data to {port.name}: {data}")
        except Exception as e:
            logging.error(f"Failed to send data to {port.name}: {e}")

    def receive_data(self, port):
        try:
            data = port.read_all().decode()
            logging.info(f"Received data from {port.name}: {data}")
            return data
        except Exception as e:
            logging.error(f"Failed to receive data from {port.name}: {e}")
            return ""

    def send_file(self, port, file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    port.write(line.encode())
            logging.info(f"Sent file {file_path} to {port.name}")
        except Exception as e:
            logging.error(f"Failed to send file {file_path} to {port.name}: {e}")

    def notify_port_status(self, message):
        show_notification("Port Status", message)
