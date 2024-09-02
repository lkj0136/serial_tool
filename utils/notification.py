from PyQt5.QtWidgets import QMessageBox

def show_notification(title, message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
