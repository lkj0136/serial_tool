from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class ProfileSettings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.profile_name_label = QLabel("Profile Name:")
        self.profile_name_input = QLineEdit()

        self.save_button = QPushButton("Save Profile")
        self.load_button = QPushButton("Load Profile")

        layout.addWidget(self.profile_name_label)
        layout.addWidget(self.profile_name_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)

        self.setLayout(layout)
