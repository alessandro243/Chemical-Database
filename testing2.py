from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Simples")
        
        # Remove o cabeçalho e define o estilo da janela como um quadrado simples
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Cria um QLineEdit na janela
        self.line_edit = QLineEdit(self)
        
        # Cria um botão na janela
        self.close_button = QPushButton("Fechar", self)
        self.close_button.clicked.connect(self.close)
        
        # Layout da janela
        layout = QVBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

