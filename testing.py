from PySide6.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QLabel, QGridLayout, QWidget, QMainWindow
from PySide6.QtCore import Qt
from db_utils import selectall2, selectPet, selectMed2, selectPet2
from db_ import SGM_DB, TABELA_, TABELA

class Qlab_(QLabel):
    def __init__(self, exit_button, line: QLineEdit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line = line
        self.bruh = exit_button
        
    def mousePressEvent(self, ev):
        self.line.clearGrid()
        self.line.setText(self.text())
        self.bruh.setFocus()
        self.line.update_label()

class OtherEdit(QLineEdit):
    def __init__(self, window, lay, win: QGridLayout, lf: QVBoxLayout, exit_button, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.window_ = window
        self.lf = lf
        self.wi = QWidget()
        self.nlay = QGridLayout()
        self.ns = lay
        self.wind = win
        self.lay = QGridLayout()
        self.wi.setLayout(self.lay)
        self.wi.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.ex_button = exit_button
        self.setFixedWidth(200)
        self.setReadOnly(True)
        self.textChanged.connect(self.update_label)
        self.labelsList = []
        self.i = 3
        
        if len(self.labelsList) > 0:
            self.clearLabels()

        for row in selectPet(SGM_DB, TABELA_):
            self.lay.addWidget(Qlab_(self.ex_button, self, row[0]))

    def clearGrid(self):
        for i in range(self.nlay.count()):
            widget = self.nlay.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def clearLabels(self):
        label = self.labelsList.pop()
        self.wind.removeWidget(label)
        label.deleteLater()

    def focusInEvent(self, event):
        global_pos = self.mapToGlobal(self.rect().bottomLeft())
        self.wi.move(global_pos)
        self.wi.show()
        self.lf.b1.setEnabled(False)
        self.lf.b2.setEnabled(False)
        self.lf.b3.setEnabled(False)
        self.lf.b4.setEnabled(False)
        super().focusInEvent(event)

    def focusOutEvent(self, event):

        self.wi.hide()
        self.lf.b1.setEnabled(True)
        self.lf.b2.setEnabled(True)
        self.lf.b3.setEnabled(True)
        self.lf.b4.setEnabled(True)
        #self.window_.setWindowFlags(Qt.Window)
        """Detecta quando o QLineEdit perde foco"""
        super().focusOutEvent(event)
    
    def update_label(self):
        i = 0
        self.ns.setLayout(self.nlay)
        lista = []
        nomePet = self.text()

        if len(self.text()) < 1:
            return

        for row in selectMed2(SGM_DB, TABELA, self.text()):
            lista.append(row)

        if len(self.labelsList) > 0:
            self.clearLabels()
            self.clearGrid()
            self.labelsList.clear()
        
        resultados = selectall2(nomePet, TABELA)
        for x in resultados:
            i += x[6]
            
        msg = QLabel(f'Foram encontrados {i} remédios para esse pet:')
        msg.setStyleSheet('font-weight: bold;')
        
        resultados2 = selectPet2(nomePet, TABELA_)
        nome = QLabel('Nome')
        peso = QLabel('Peso')
        cor = QLabel('Cor')
        nome.setStyleSheet('font-weight: bold;')
        peso.setStyleSheet('font-weight: bold;')
        cor.setStyleSheet('font-weight: bold;')

        n = QLabel(f'{resultados2[0][1]}')
        spc = QLabel('')
        p = QLabel(f'{resultados2[0][2]}')
        spc2 = QLabel('')
        c = QLabel(f'{resultados2[0][3]}')
        space = QLabel('')
        spc3 = QLabel('')
        spc4 = QLabel('')
        spc5 = QLabel('')
        spc6 = QLabel('')
        self.nlay.addWidget(msg, 1, 1)
        self.nlay.addWidget(space, 2, 1)
        self.nlay.addWidget(n, 2, 7)
        self.nlay.addWidget(spc, 1, 8)
        self.nlay.addWidget(p, 2, 9)
        self.nlay.addWidget(spc2, 1, 10)
        self.nlay.addWidget(c, 2, 11)
        self.nlay.addWidget(nome, 1, 7)
        self.nlay.addWidget(peso, 1, 9)
        self.nlay.addWidget(cor, 1, 11)
        self.nlay.addWidget(spc3, 1, 3)
        self.nlay.addWidget(spc4, 1, 4)
        self.nlay.addWidget(spc5, 1, 5)
        self.nlay.addWidget(spc6, 1, 6)
        edit_b = QPushButton('📝')

        edit_b.setStyleSheet("""
QPushButton {
    background-color: #ffffff;  /* Cor de fundo */
    color: white;  /* Cor do texto */
    border: none;  /* Sem borda */
    border-radius: 15px;  /* Arredondamento das bordas */
    padding: 0;  /* Remover preenchimento extra */
    font-size: 15px;
}
""")
        self.nlay.addWidget(edit_b, 1, 12)
        edit_b.clicked.connect(self.make(self.window_.upPets,[n.text(),p.text().replace('kg', ''),c.text()]))
        for x, y in enumerate(lista):

            p = QLabel('')
            p.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.nlay.addWidget(p, self.i, 1)
            self.labelsList.append(p)
            self.i+=1
        
        for t, y in enumerate(self.labelsList):
            y.setText(f'            • {lista[t][1]}')
        
        lista.clear()

    def make(self, func, args):
        def inter():
            return func(args)
        return inter

class SimpleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela Simples")
        self.setGeometry(100, 100, 400, 300)  # Define a posição e o tamanho da janela
        self.center = QWidget()
        self.layout_ = QGridLayout()
        self.center.setLayout(self.layout_)
        self.setCentralWidget(self.center)
        self.wid = QWidget()
        self.wie = QWidget()
        b2 = QLineEdit()
        self.layout_.addWidget(b2)
        b3 = OtherEdit(b2, self.wid, '')
        self.layout_.addWidget(b3)
        self.b1 = OtherEdit(b2, self.wie, '')
        self.layout_.addWidget(self.b1)

