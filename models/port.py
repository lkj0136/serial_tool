class Port:
    def __init__(self, name, baudrate, databits, stopbits, parity):
        self.name = name
        self.baudrate = baudrate
        self.databits = databits
        self.stopbits = stopbits
        self.parity = parity
        self.is_open = False

    def open(self):
        # 포트 열기 로직
        self.is_open = True

    def close(self):
        # 포트 닫기 로직
        self.is_open = False
