from PySide6.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QGridLayout, QWidget, QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer
from db_utils import selectPet, selectMed2
import sqlite3
from db_ import SGM_DB, TABELA_, TABELA

class Qlab_(QLabel):
    def __init__(self, exit_button, line: QLineEdit, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.line = line
        self.bruh = exit_button
        
    def mousePressEvent(self, ev):
        self.line.setText(self.text())
        self.bruh.setFocus()

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

        self.clearGrid()
        

        
        if len(self.labelsList) > 0:
            self.clearLabels()

        for row in selectPet(SGM_DB, TABELA_):
            self.lay.addWidget(Qlab_(self.ex_button, self, row[0]))
            #self.labelsList.append(row[0])

    def clearGrid(self):
    # Remove todos os widgets da grid
        for i in range(self.nlay.count()):
            widget = self.nlay.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def clearLabels(self):
        label = self.labelsList.pop()
        self.wind.removeWidget(label)  # Remove do layout
        label.deleteLater()

    def focusInEvent(self, event):
        global_pos = self.mapToGlobal(self.rect().bottomLeft())
        self.wi.move(global_pos)
        self.wi.show()
        self.lf.b1.setEnabled(False)
        self.lf.b2.setEnabled(False)
        self.lf.b3.setEnabled(False)
        self.lf.b4.setEnabled(False)
        #self.window_.setWindowFlags(self.windowFlags() & ~Qt.WindowTitleHint)
        """Detecta quando o QLineEdit recebe foco"""
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
    
    def update_label(self, text):
        self.ns.setLayout(self.nlay)
        lista = []
        nomePet = self.text()

        if len(self.text()) < 1:
            return

        for row in selectMed2(SGM_DB, TABELA, self.text()):
            lista.append(row)

        if len(self.labelsList) > 0:
            print(123)
            self.clearLabels()
            self.clearGrid()
            self.labelsList.clear()
            print(len(self.labelsList))
        
        msg = QLabel(f'Lista de remédios para o Pet:')
        msg.setStyleSheet('font-weight: bold;')
        space = QLabel('')
        space2 = QLabel('')
        self.nlay.addWidget(msg, 1, 1)
        self.nlay.addWidget(space, 2, 1)


        for x, y in enumerate(lista):

            p = QLabel('')
            p.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.nlay.addWidget(p, self.i, 1)
            self.labelsList.append(p)
            self.i+=1
        
        for t, y in enumerate(self.labelsList):
            y.setText(f'            • {lista[t][1]}')
        
        lista.clear()

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

