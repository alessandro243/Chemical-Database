from PySide6.QtWidgets import QLineEdit, QPushButton
from win_utils import verifiedstring, verifiedNumber, verifiedData
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QGridLayout

class NumberEdits(QLineEdit):
    def __init__(self, label, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(350, 30)
        self.label = label
    
    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.label.setText('')
    
    def focusOutEvent(self, event):
        super().focusOutEvent(event)

    def make(self, func, args):
        def inter():
            return func(args)
        return inter

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.center = QWidget()
        self.lay = QGridLayout()
        self.center.setLayout(self.lay)
        self.setCentralWidget(self.center)
        self.b1 = QPushButton('Submit')
        self.connectButtonClicked(self.b1, self.permitido)
        
        self.lay.addWidget(self.b1)
        
        self.lab = QLabel('')
        self.lab2 = QLabel('estou aqui')
        self.lab3 = QLabel('')
        self.lab4 = QLabel('')

        self.lay.addWidget(self.lab, 2, 1)
        self.lay.addWidget(self.lab3, 4, 1)
        self.lay.addWidget(self.lab4, 6, 1)
        
        self.lay.addWidget(self.lab2, 1, 3)

        self.edit = OtherEdits(self.lab, self.lab2, verifiedstring)
        self.edit2 = OtherEdits(self.lab3, self.lab2, verifiedstring)
        self.edit3 = OtherEdits(self.lab4, self.lab2, verifiedstring)
        
        self.lay.addWidget(self.edit, 1, 1)
        self.lay.addWidget(self.edit2, 3, 1)
        self.lay.addWidget(self.edit3, 5, 1)
        
    def connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def permitido(self):
        if self.edit.state and self.edit2.state and self.edit3.state:
            return

class OtherEdits(QLineEdit):
    def __init__(self, label, func, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(350, 30)
        self.label = label
        self.func = func
        self.state = False
        self.textChanged.connect(self.make(self.function, self.func))
    
    def function(self, fun):
        
        texto = self.text()
        #self.remove_acentos_simples(texto)

        if fun(texto, self.label):
            self.state = True
        else:
            self.state = False

    
    def bruh(self, label):
        if self.function(self.func):
            label.setText('válido')
            

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.label.setText('')
    
    def focusOutEvent(self, event):
        super().focusOutEvent(event)

    def make(self, func, args):
        def inter():
            return func(args)
        return inter
    
    #def remove_acentos_simples(self, palavra):
        acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
        'ç': 'c',
    }
        for acento, sem_acento in acentos.items():
            palavra = palavra.replace(acento, sem_acento)
        return palavra


if __name__ ==  '__manin__':
    app = QApplication()
    wind = MainWindow()

    wind.show()
    app.exec()