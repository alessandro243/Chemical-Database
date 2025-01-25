from PySide6.QtWidgets import QLabel, QLineEdit
from PySide6.QtGui import Qt
import datetime

class QLabel_(QLabel):
    def __init__(self, win, row, text="", exit_button = None, line: QLineEdit = None, parent=None):
        super().__init__(text, parent)
        self.win = win
        self.row = row
        self.line = line
        self.bruh = exit_button
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def mousePressEvent(self, ev):
        resume = self.win.principalLayout.leftLayout
        
        id = f'ID: {self.row[0]}'
        nome = f'Nome: {self.row[1]}'
        nome_f = f'Nome farmacêutico: {self.row[2]}'
        lab = f'Laboratório: {self.row[3]}'
        peso = f'Peso líquido: {self.row[4]}'
        validade = f'Validade: {self.row[5]}'

        if self.row[5] != '-':
            
            ano = self.row[5][3:7]
            mes = self.row[5][0:2]

            data = datetime.date(int(ano), int(mes), 1)
            diferenca = data - datetime.date.today()

            if diferenca < datetime.timedelta(days=60):
                    resume.la6.setStyleSheet('color: red;')
            
            else:
                resume.la6.setStyleSheet('color: black;')
        else:
            resume.la6.setStyleSheet('color: black;')
            
        unidade = f'Unidade: {self.row[6]}'
        qtdt = f'Quant. total: {self.row[7]}'
        qtdr = f'Quant. restante: {self.row[8]}'
        pet = f'Pet: {self.row[9]}'
        descrition = 'Descrição'

        resume.la.setText(descrition)
        resume.la.setStyleSheet('font-size: 13px; font-weight: bold')

        self.textConfig(
            [resume.la1, resume.la2, resume.la3, resume.la4, resume.la5, resume.la6, resume.la7, resume.la8, resume.la9, resume.la10],
            [id, nome, nome_f, lab, peso, validade, unidade, qtdt, qtdr, pet],
            )
        if not self.bruh is None or not self.line is None:
            self.line.setText(self.text())
            self.bruh.setFocus()

    def textConfig(self, args, words, weight=None):
        cond = weight == 'n' or weight == 'N'
        for x, y in enumerate(args):
            if cond:
                y.setStyleSheet('font-size: 13px; font-weight: bold')
            y.setText(words[x])




