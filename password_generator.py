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