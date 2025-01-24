from PySide6.QtWidgets import QLabel, QSpacerItem, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QScrollArea
from buttons_ import Button_

class FristScreenLayout(QHBoxLayout):
    def __init__(self, win, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.leftLayout = LeftLayoutFristScreen(win)
        self.rightLayout = RightLayoutFristScreen()
        
        self.addLayout(self.leftLayout)

class SubGridsMather(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def appendSeveral(self, iterable, args):
        for x in args:
            iterable.append(x)
    
    def addSeveral(self, group):
        for x in group:
            self.addWidget(x)
    
    def configSeveralWH(self, group, W, H):
        for x in group:
            x.setFixedSize(W, H)

class SubVerticalGridsMather(QVBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def appendSeveral(self, iterable, args):
        for x in args:
            iterable.append(x)

    def addSeveral(self, group):
        for x in group:
            self.addWidget(x)

class LeftLayoutFristScreen(SubGridsMather):
    def __init__(self, win, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.labelList = []
        wi = QWidget()
        lay = QVBoxLayout()
        wi.setLayout(lay)
        s = QScrollArea()
        s.setFixedSize(300, 250)
        s.setWidget(wi)
        s.setWidgetResizable(True)
    
        self.b1 = Button_(win, 'Adicionar')
        self.b2 = Button_(win, 'Adicionar pet')
        self.b3 = Button_(win, 'Buscar')
        self.b4 = Button_(win, 'Listar')

        self.configSeveralWH(
            [self.b1, self.b2, self.b3, self.b4],
            300, 50
        )

        self.addSeveral([self.b1, self.b2, self.b3, self.b4])
        self.la0 = QLabel('')
        self.l = QLabel('')
        self.la0.setFixedSize(20, 20)
        self.la = QLabel('Descrição')
        self.la1 = QLabel('')
        self.la2 = QLabel('')
        self.la3 = QLabel('')
        self.la4 = QLabel('')
        self.la5 = QLabel('')
        self.la6 = QLabel('')
        self.la7 = QLabel('')
        self.la8 = QLabel('')
        self.la9 = QLabel('')
        self.la10 = QLabel('')

        lay.addWidget(self.la)
        lay.addWidget(self.la1)
        lay.addWidget(self.la2)
        lay.addWidget(self.la3)
        lay.addWidget(self.la4)
        lay.addWidget(self.la5)
        lay.addWidget(self.la6)
        lay.addWidget(self.la7)
        lay.addWidget(self.la8)
        lay.addWidget(self.la9)
        lay.addWidget(self.la10)
        #lay.addWidget(self.la0, 1, 1)
        #lay.addWidget(self.l, 1, 1)

        self.appendSeveral(
            self.labelList, 
            [self.la, self.la1, self.la2, self.la3, self.la4, self.la5, self.la6, self.la7, self.la8, self.la9, self.la10]
            )
        #self.addSeveral(
            #[self.la, self.la1, self.la2, self.la3, self.la4, self.la5, self.la6, self.la7, self.la8, self.la9, self.la10]
        #)
        self.addWidget(s)

class RightLayoutFristScreen(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class SecondScreenLayout(QHBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.leftLayout = LeftLayoutFristScreen()
        self.rightLayout = RightLayoutSecondScreen()
        self.addLayout(self.leftLayout)
        self.addLayout(self.rightLayout)

class RightLayoutSecondScreen(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        b1 = Button_('Testando2')
        b2 = Button_('Testando3')
        self.addWidget(b1)
        self.addWidget(b2)
    