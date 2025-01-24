from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Signal

class Button_(QPushButton):
    mouse_hovered = Signal()
    def __init__(self, win, *args, **kwags):
        super().__init__(*args, **kwags)
        self.state = False
        self.win = win

        if self.text() == 'Adicionar':
            self.mouse_hovered.connect(self.win[0])
        
        if self.text() == 'Adicionar pet':
            self.mouse_hovered.connect(self.win[1])
        
        if self.text() == 'Listar':
            self.mouse_hovered.connect(self.win[2])

        if self.text() == 'Buscar':
            self.mouse_hovered.connect(self.win[3])

    def make(self, func, args):
        def inter():
            return func(args)
        return inter

    def enterEvent(self, event):

        if not self.isEnabled():
            event.ignore()  # Ignora o evento se o botão estiver desativado
        else:
    
        #Emite o sinal quando o mouse entra na área do botão
            self.mouse_hovered.emit()
            super().enterEvent(event)

    def leaveEvent(self, event):
        # Emite o sinal quando o mouse sai da área do botão
        self.state = False
        super().leaveEvent(event)

        