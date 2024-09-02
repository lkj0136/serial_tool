from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel


class DataTransfer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.data_input = QTextEdit()
        self.send_button = QPushButton("Send Data")
        self.multi_send_button = QPushButton("Multi Send Data")

        self.repeat_count_label = QLabel("Repeat Count:")
        self.repeat_count_input = QTextEdit()

        self.repeat_interval_label = QLabel("Repeat Interval (ms):")
        self.repeat_interval_input = QTextEdit()

        self.received_data = QTextEdit()
        self.received_data.setReadOnly(True)

        layout.addWidget(self.data_input)
        layout.addWidget(self.send_button)
        layout.addWidget(self.multi_send_button)
        layout.addWidget(self.repeat_count_label)
        layout.addWidget(self.repeat_count_input)
        layout.addWidget(self.repeat_interval_label)
        layout.addWidget(self.repeat_interval_input)
        layout.addWidget(self.received_data)

        self.setLayout(layout)
