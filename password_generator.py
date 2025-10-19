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
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_title = QLabel("Parola Oluşturucu")
        self.label_title.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(self.label_title)

        self.password_field = QLineEdit()
        self.password_field.setReadOnly(True)
        self.password_field.setPlaceholderText("Parola burada görünecek...")
        layout.addWidget(self.password_field)

        self.generate_button = QPushButton("Parola Oluştur")
        self.generate_button.setFont(QFont("Arial", 12))
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.copy_button = QPushButton("Kopyala")
        self.copy_button.setFont(QFont("Arial", 12))
        self.copy_button.clicked.connect(self.copy_password)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

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