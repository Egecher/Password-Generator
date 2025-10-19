import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel, QLineEdit
)
from PyQt5.QtGui import QFont

def create_password():
    """Rastgele 10 haneli parola oluşturur."""
    dizi = np.random.randint(0, 100000, size=(1, 10))
    parola = ''.join(map(str, dizi[0]))
    return parola

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔐Password Generator")
        self.setFixedWidth(450)
        self.setFixedHeight(200)

    def generate_password(self):
        parola = create_password()
        self.password_field.setText(parola)

    def copy_password(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.password_field.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())