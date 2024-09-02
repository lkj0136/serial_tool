from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QProgressBar, QLabel


class FileView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.file_path_label = QLabel("File Path:")
        self.file_path_input = QTextEdit()
        self.file_path_input.setReadOnly(True)

        self.start_transfer_button = QPushButton("Start File Transfer")
        self.stop_transfer_button = QPushButton("Stop File Transfer")

        self.progress_bar = QProgressBar()

        layout.addWidget(self.file_path_label)
        layout.addWidget(self.file_path_input)
        layout.addWidget(self.start_transfer_button)
        layout.addWidget(self.stop_transfer_button)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)
