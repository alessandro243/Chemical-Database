from PySide6.QtWidgets import QMessageBox, QLabel, QMainWindow, QLabel, QWidget, QScrollArea, QPushButton
from labels_ import QLabel_
from testing import OtherEdit
from PySide6.QtCore import QTimer, Signal
from line_edits import OtherEdits
from PySide6.QtGui import Qt, QKeyEvent, QIcon
from variables import TABELA, SGM_DB, LISTA, TABELA_
from db_utils import update_, insert_med, insert_pet, selectMed, up, up2, selectMed3, contar, selectall, makeList, upP
from win_utils import verifiedstring, verifiedNumber, verifiedData, verifiedcient, verifiedPeso, verifiedLab
import datetime
from layout_ import FristScreenLayout

class  MainWindow(QMainWindow):
    enterPressed = Signal()
    escPressed = Signal()
    move_ = Signal()
    def __init__(self, *args, **kwags):
        super().__init__(*args, **kwags)

        self.principalLayout = FristScreenLayout([self.makeAddGrid, self.makeAddPetGrid, self.makeUpdateGrid, self.foundOp])
        self.setFixedSize(990, 500)
        self.datas = []
        self.editList = []
        self.editList2 = []
        self.editList3 = []
        self.setFixedSize(975, 490)
        self.labelsList_ = []
        self.principalLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.center = QWidget()
        self.setCentralWidget(self.center)
        self.center.setLayout(self.principalLayout)
        self.widget_ = QWidget()
        wid = QWidget()
        wid.setLayout(self.principalLayout.rightLayout)
        self.scroll_ = QScrollArea()
        self.scroll_.setWidgetResizable(True)
        self.scroll_.setWidget(wid)
        self.principalLayout.addWidget(self.scroll_)
        self.makeUpdateGrid()
        self.ll = []
        self.escPressed.connect(self.makeUpdateGrid)
        self.setWindowTitle('Chemical Database')
        self.setWindowIcon(QIcon("images.ico"))
    
    def moveEvent(self, event):
        # Este evento é disparado quando a janela muda de posição
        new_position = event.pos()
        self.move_.emit()
        try:

            self.ob.wi.hide()
            self.ob.clearFocus()
        except AttributeError:
            ...

    def keyPressEvent(self, event: QKeyEvent) -> None:
        texto = event.text().strip()
        key = event.key()

        isEnter = key == 16777220
        isEsc = key == 16777216

        if isEnter:
            self.enterPressed.emit()
            return event.ignore()

        if isEsc:
            self.escPressed.emit()
            return event.ignore()

    def makeUpdateGrid(self):
        self.ol = []
        self.editList.clear()
        self.clearGrid()
        LISTA.clear()
        self.datas.clear()
        self.labelsList_.clear()
        self.editList2.clear()
        self.editList3.clear()
        self.principalLayout.leftLayout.la3.setStyleSheet('font-weight: normal;')

        for row in makeList(SGM_DB, TABELA):

            if row not in LISTA:
                if not row[5] == '-':
                    LISTA.append(row)
                else:
                    self.ol.append(row)

        for x, y in enumerate(LISTA):
            try:
                LISTA.sort(key=lambda item: datetime.date(int(item[5][3:7]), int(item[5][0:2]), 1))
            except ValueError as e:
                print(f"Erro ao processar datas: {e}")
        
        for x in self.ol:
            LISTA.append(x)
        
        label1 = QLabel("Nome do remédio")
        label2 = QLabel("Peso líquido")
        label3 = QLabel("Unidade")
        label4 = QLabel("Quantidade total")
        label5 = QLabel("Quantidade restante")
        label6 = QLabel("Validade")
        label7 = QLabel("Pet")

        self.configureLabels([label1, label2, label3, label4, label5, label6, label7])
        self.addToLayout(0, [label1, label2, label3, label4, label5, label6, label7], 4)

        for x, y in enumerate(LISTA):
            
            datas = (y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7], y[8], y[9])
            nome = QLabel_(self, datas, y[1])
            lab = QLabel_(self, datas, str(y[6]))
            val = QLabel_(self, datas, y[5])
            nome_f = QLabel_(self, datas, y[4])
            qtd_total = QLabel_(self, datas, str(y[7]))
            qtd_restant = QLabel_(self, datas, str(y[8]))
            pet = QLabel_(self, datas, str(y[9]))
            
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
            self.connectButtonClicked(edit_b, self.make(self.editgrid, datas))
            hoje = datetime.date.today()
            ano = val.text()[3:7]
            mes = val.text()[0:2]
            if y[5] != '-':
                data = datetime.date(int(ano), int(mes), 1)
                diferenca = data - hoje

                if diferenca < datetime.timedelta(days=60):
                    nome.setStyleSheet('color: red;')
                    lab.setStyleSheet('color: red;')
                    val.setStyleSheet('color: red;')
                    nome_f.setStyleSheet('color: red;')
                    qtd_total.setStyleSheet('color: red;')
                    qtd_restant.setStyleSheet('color: red;')
                    pet.setStyleSheet('color: red;')

            self.addToLayout(x+1, [edit_b])
            self.addToLayout(x+1, [nome, nome_f, lab, qtd_total, qtd_restant, val, pet], 4)
        
        LISTA.clear()

    def editgrid(self, args):
        self.clearGrid()
        
        b1 = QLabel('Nome:')
        b2 = QLabel('Nome farmacêutico:')
        b3 = QLabel('Laboratório:')
        b4 = QLabel('Peso líquido:')
        b5 = QLabel('Validade:')
        b6 = QLabel('Unidade:')
        b7 = QLabel('Quantidade total:')
        b8 = QLabel('Quantidade restante:')
        b9 = QLabel('Nome do pet:')

        lab = QLabel('')
        lab1 = QLabel('')
        lab2 = QLabel('')
        lab3 = QLabel('')
        lab4 = QLabel('')
        lab5 = QLabel('')
        lab6 = QLabel('')
        lab7 = QLabel('')
        lab8 = QLabel('')
        lab9 = QLabel('')

        l1 = OtherEdits(lab1, verifiedstring)
        l2 = OtherEdits(lab2, verifiedcient)
        l3 = OtherEdits(lab3, verifiedLab)
        l4 = OtherEdits(lab4, verifiedPeso)
        l5 = OtherEdits(lab5, verifiedData)
        l6 = OtherEdits(lab6, verifiedNumber)
        l7 = OtherEdits(lab7, verifiedNumber)
        l8 = OtherEdits(lab8, verifiedNumber)
        l9 = OtherEdits(lab9, verifiedstring)
        
        l1.setText(str(args[1]))
        l2.setText(str(args[2]))
        l3.setText(str(args[3]))
        l4.setText(str(args[4].replace('mg', '')))
        l5.setText(str(args[5]))
        l6.setText(str(args[6]))
        l7.setText(str(args[7]))
        l8.setText(str(args[8]))
        l9.setText(str(args[9]))

        update = QPushButton('Update')
        update.setFixedSize(200, 40)
        update.setStyleSheet('font-size: 13px;')

        self.enterPressed.connect(update, self.make(self.upd2, [[lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab], [l1, l2, l3, l4, l5, l6, l7, l8, l9], args]))
        self.connectButtonClicked(update, self.make(self.upd2, [[lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab], [l1, l2, l3, l4, l5, l6, l7, l8, l9], args]))
        
        self.configureLabels([b1, b2, b3, b4, b5, b6, b7,  b8, b9])
        self.addToVerticalLayout([b1, b2, b3, b4, b5, b6, b7,  b8, b9], 0, 0, 2)
        self.addToVerticalLayout([l1, l2, l3, l4, l5, l6, l7, l8, l9], 0, 1, 2)
        self.addToVerticalLayout([lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9], 1, 1, 2)
        self.buttonsSize(
            [b1, b2, b3, b4, b5, b6, b7, b8, b9],
            150, 40
        )
 
        self.principalLayout.rightLayout.addWidget(update, 20, 0)
        self.principalLayout.rightLayout.addWidget(lab, 20, 1)
        l1.setFocus()
        
    def upd2(self, args):
            
        if args[1][0].state and args[1][1].state and args[1][2].state and args[1][3].state and args[1][4].state and args[1][5].state and args[1][6].state and args[1][7].state and args[1][8].state:
            try:
                
                up2(SGM_DB, TABELA, args, args[2])

            except IndexError:
                self._showError('Medicamento não registrado')
            
            finally:
                ...
            args[0][-1].setText('Registrado com sucesso!')
            QTimer.singleShot(3000, args[0][-1].hide)

            self.makeUpdateGrid()

    def makeAddPetGrid(self):
        resume = self.principalLayout.leftLayout
        resume.la6.setStyleSheet('color: black;')
        path_ = self.principalLayout.rightLayout.addWidget
        self.clearGrid()
        self.editList.clear()
        self.editList2.clear()
        self.labelsList_.clear()

        lf = self.principalLayout.leftLayout
        bold_ = 'font-weight: bold;'
        spaces_ = 10*' '

        resultados = contar(SGM_DB, TABELA_)

        self.principalLayout.leftLayout.la.setText('Registro de pets:')
        self.principalLayout.leftLayout.la1.setText(f'{spaces_}Há um total de {resultados[0][0]} pets registrados.' )
        lf.la3.setText('Função Adicionar pets:')
        lf.la3.setStyleSheet(bold_)
        lf.la4.setText(f'{spaces_} Fução que permite ao usuário adicionar')
        lf.la5.setText(f'{spaces_} novos pets ao sistema')
        lf.la6.setText(f'{spaces_} fornecendo os dados requeridos.')
        lf.la7.setText(f'{spaces_} É necessária para adição de medicamentos')
        lf.la8.setText(f'{spaces_} para novos pets.')

        lab14 = QLabel('')
        lab13 = QLabel('')
        lab12 = QLabel('')
        lab11 = QLabel('')        
        lab10 = QLabel('')
        lab9 = QLabel('')
        lab8 = QLabel('')
        lab7 = QLabel('')
        lab1 = QLabel('Nome:')
        lab1.setStyleSheet('font-size: 13px; font-weight: bold')
        lab2 = QLabel('')
        lab2.setStyleSheet('color: red;')
        lab3 = QLabel('Peso:')
        lab3.setStyleSheet('font-size: 13px; font-weight: bold')
        lab4 = QLabel('')
        lab4.setStyleSheet('color: red;')
        lab5 = QLabel('Cor:')
        lab5.setStyleSheet('font-size: 13px; font-weight: bold')
        lab6 = QLabel('')
        lab6.setStyleSheet('color: red;')
        self.labelsList_.append(lab2)
        self.labelsList_.append(lab4)
        self.labelsList_.append(lab6)
        line1 = OtherEdits(lab2, verifiedstring)
        line2 = OtherEdits(lab4, verifiedNumber)
        line3 = OtherEdits(lab6, verifiedstring)

        self.editList2.append(line1)
        self.editList2.append(line2)
        self.editList2.append(line3)

        send = QPushButton('Send')
        self.enterPressed.connect(send, self.make(self.send_, [lab2, lab4, lab6]))
        self.connectButtonClicked(send, self.make(self.send_, [lab2, lab4, lab6]))

        path_(lab14, 1, 1)
        lab14.setFixedSize(150, 150)
        path_(lab13, 1, 2)
        path_(lab12, 2, 2)
        path_(lab11, 3, 2)
        path_(lab10, 4, 2)
        path_(lab9, 5, 2)
        path_(lab8, 6, 2)
        path_(lab7, 7, 2)
        path_(lab1, 8, 2)
        path_(lab2, 9, 3)
        path_(lab3, 10, 2)
        path_(lab4, 11, 3)
        path_(lab5, 12, 2)
        path_(lab6, 13, 3)
        path_(line1, 8, 3)
        path_(line2, 10, 3)
        path_(line3, 12, 3)
        path_(send, 12, 4)
        line1.setFocus()
        line1.setText('a')
        line2.setText('a')
        line3.setText('a')
        line1.clear()
        line2.clear()
        line3.clear()

    def send_(self, args):
        self.principalLayout.leftLayout.la.setText('Registro de Remédios')
        
        nome = self.editList2[0].text()
        peso = self.editList2[1].text()
        cor = self.editList2[2].text()

        if self.editList2[0].state and self.editList2[1].state and self.editList2[2].state:
            
            for x in self.labelsList_:
                x.setText('')
            
            for x in self.editList2:
                x.clear()

            insert_pet(SGM_DB , TABELA_, (nome.capitalize(), float(peso), cor.capitalize()))

            args[0].setText('')
            args[1].setText('')
            args[2].setText('Registrado com sucesso!')
            args[2].setStyleSheet('color: black;')

    def bruh(self, args):
        args[0].setText('')
        args[1].setText('')
        args[2].setText('')

        self.editList2[0].setText('a')
        self.editList2[1].setText('a')
        self.editList2[2].setText('a')
        self.editList2[0].clear()
        self.editList2[1].clear()
        self.editList2[2].clear()

    def makeAddGrid(self):
        resume = self.principalLayout.leftLayout
        resume.la6.setStyleSheet('color: black;')
        self.labelsList_.clear()
        self.clearGrid()
        lf = self.principalLayout.leftLayout
        bold_ = 'font-weight: bold;'
        total = 0
        spaces_ = 10*' '

        for resultado in selectall(SGM_DB, TABELA):
            total += resultado[6]

        self.principalLayout.leftLayout.la.setText('Registro de remédios:')
        self.principalLayout.leftLayout.la.setStyleSheet('font-weight: bold;')
        self.principalLayout.leftLayout.la1.setText(f'{spaces_}Há um total de {total} remédios registrados.' )
        lf.la3.setText('Função Adicionar remédios:')
        lf.la3.setStyleSheet(bold_)
        lf.la4.setText(f'{spaces_} Fução que permite ao usuário adicionar')
        lf.la5.setText(f'{spaces_} novos medicamentos ao sistema')
        lf.la6.setText(f'{spaces_} fornecendo os dados requeridos.')
        lf.la7.setText(f'{spaces_} Não será permitido o registro')
        lf.la8.setText(f'{spaces_} cujos nomes dos pets não estiverem')
        lf.la9.setText(f'{spaces_} registrados no sistema.')

        b1 = QLabel('Nome:')
        b2 = QLabel('Nome farmacêutico:')
        b3 = QLabel('Laboratório:')
        b4 = QLabel('Peso líquido:')
        b5 = QLabel('Validade:')
        b6 = QLabel('Unidade:')
        b7 = QLabel('Quantidade total:')
        b8 = QLabel('Quantidade restante:')
        b9 = QLabel('Nome do pet:')

        lab1 = QLabel('')
        self.labelsList_.append(lab1)
        lab2 = QLabel('')
        self.labelsList_.append(lab2)
        lab3 = QLabel('')
        self.labelsList_.append(lab3)
        lab4 = QLabel('')
        self.labelsList_.append(lab4)
        lab5 = QLabel('A validade deve seguir a máscara: MM/YYYY')
        self.labelsList_.append(lab5)
        lab6 = QLabel('')
        self.labelsList_.append(lab6)
        lab7 = QLabel('')
        self.labelsList_.append(lab7)
        lab8 = QLabel('')
        self.labelsList_.append(lab8)
        lab9 = QLabel('')
        self.labelsList_.append(lab9)
        lista = []

        l1 = OtherEdits(lab1, verifiedstring)
        l2 = OtherEdits(lab2, verifiedcient)
        l3 = OtherEdits(lab3, verifiedLab)
        l4 = OtherEdits(lab4, verifiedPeso)
        l5 = OtherEdits(lab5, verifiedData)
        l6 = OtherEdits(lab6, verifiedNumber)
        l7 = OtherEdits(lab7, verifiedNumber)
        l8 = OtherEdits(lab8, verifiedNumber)
        l9 = OtherEdits(lab9, verifiedstring)

        lista.append(l1)
        lista.append(l2)
        lista.append(l3)
        lista.append(l4)
        lista.append(l5)
        lista.append(l6)
        lista.append(l7)
        lista.append(l8)
        lista.append(l9)

        submit = QPushButton('Submit')
        submit.setFixedSize(200, 40)
        submit.setStyleSheet('font-size: 13px;')
        self.enterPressed.connect(submit, self.make(self.submit_, [[l1, l2, l3, l4, l5, l6, l7, l8, l9], lista]))
        self.connectButtonClicked(submit, self.make(self.submit_, [[l1, l2, l3, l4, l5, l6, l7, l8, l9], lista]))
        
        self.configureLabels([b1, b2, b3, b4, b5, b6, b7,  b8, b9])
        self.addToVerticalLayout([b1, b2, b3, b4, b5, b6, b7,  b8, b9], 0, 0, 2)
        self.addToVerticalLayout([l1, l2, l3, l4, l5, l6, l7, l8, l9], 0, 1, 2)
        self.addToVerticalLayout([lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9], 1, 1, 2)
        self.buttonsSize(
            [b1, b2, b3, b4, b5, b6, b7, b8, b9],
            150, 40
        )

        for x in lista:
            x.setText('a')
            x.clear()
        l1.setFocus()

        self.principalLayout.rightLayout.addWidget(submit, 20, 0)

    def inclui(self, args):
        texto = args[0][-1].text().capitalize()
        path_ = self.principalLayout.rightLayout.addWidget
        args[1][0].hide()
        
        if args[0][-1].state:

            resultado = selectMed(SGM_DB, TABELA, texto)
            args[0][-1].clear()
            args[0][-1].hide()
            args[1][-1].hide()
            args[1][-2].hide()

            try:
                consulta = resultado[0]
                self.datas.append(consulta)

            except IndexError:
                self._showError('Medicamento não registrado', 'O medicamento que você pesquisou não consta no sistema!')
                self.makeUpdateGrid()
                return
            
            args[0][0].setText(f'{consulta[0]}')
            args[0][1].setText(f'{consulta[1]}')
            args[0][2].setText(f'{consulta[2]}')
            args[0][3].setText(f'{consulta[3]}')
            args[0][4].setText(f'{consulta[4]}')
            args[0][5].setText(f'{consulta[5]}')
            args[0][6].setText(f'{consulta[6]}')
            args[0][7].setText(f'{consulta[7]}')
            args[0][8].setText(f'{consulta[8]}')
            args[0][9].setText(f'{consulta[9]}')

            edit = QPushButton('📋')
        
            edit.setFixedSize(30, 30)
            edit.setStyleSheet("""
QPushButton {
    background-color: #ffffff;  /* Cor de fundo */
    color: white;  /* Cor do texto */
    border: none;  /* Sem borda */
    border-radius: 15px;  /* Arredondamento das bordas */
    padding: 0;  /* Remover preenchimento extra */
    font-size: 15px;
}
""")    
            self.connectButtonClicked(edit, self.make(self.edit_, consulta))
            path_(edit, 1, 3)

    def make(self, func, args):
            def inter():
                func(args)
            return inter

    def edit_(self, consulta):
        self.clearGrid()

        b1 = QLabel('Nome:')
        b2 = QLabel('Nome farmacêutico:')
        b3 = QLabel('Laboratório:')
        b4 = QLabel('Peso líquido:')
        b5 = QLabel('Validade:')
        b6 = QLabel('Unidade:')
        b7 = QLabel('Quantidade total:')
        b8 = QLabel('Quantidade restante:')
        b9 = QLabel('Nome do pet:')

        lab = QLabel('')
        lab1 = QLabel('')
        lab2 = QLabel('')
        lab3 = QLabel('')
        lab4 = QLabel('')
        lab5 = QLabel('')
        lab6 = QLabel('')
        lab7 = QLabel('')
        lab8 = QLabel('')
        lab9 = QLabel('')

        l1 = OtherEdits(lab1, verifiedstring)
        l2 = OtherEdits(lab2, verifiedcient)
        l3 = OtherEdits(lab3, verifiedLab)
        l4 = OtherEdits(lab4, verifiedPeso)
        l5 = OtherEdits(lab5, verifiedData)
        l6 = OtherEdits(lab6, verifiedNumber)
        l7 = OtherEdits(lab7, verifiedNumber)
        l8 = OtherEdits(lab8, verifiedNumber)
        l9 = OtherEdits(lab9, verifiedstring)
        
        l1.setText(str(consulta[1]))
        l2.setText(str(consulta[2]))
        l3.setText(str(consulta[3]))
        l4.setText(str(consulta[4].replace('mg', '')))
        l5.setText(str(consulta[5]))
        l6.setText(str(consulta[6]))
        l7.setText(str(consulta[7]))
        l8.setText(str(consulta[8]))
        l9.setText(str(consulta[9]))

        update = QPushButton('Update')
        update.setFixedSize(200, 40)
        update.setStyleSheet('font-size: 13px;')
        self.enterPressed.connect(update,self.make(self.upd, [[lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab], [l1, l2, l3, l4, l5, l6, l7, l8, l9]]))
        self.connectButtonClicked(update, self.make(self.upd, [[lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9, lab], [l1, l2, l3, l4, l5, l6, l7, l8, l9]]))
    
        self.configureLabels([b1, b2, b3, b4, b5, b6, b7,  b8, b9])
        self.addToVerticalLayout([b1, b2, b3, b4, b5, b6, b7,  b8, b9], 0, 0, 2)
        self.addToVerticalLayout([l1, l2, l3, l4, l5, l6, l7, l8, l9], 0, 1, 2)
        self.addToVerticalLayout([lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9], 1, 1, 2)
        self.buttonsSize(
            [b1, b2, b3, b4, b5, b6, b7, b8, b9],
            150, 40
        )

        self.principalLayout.rightLayout.addWidget(update, 20, 0)
        self.principalLayout.rightLayout.addWidget(lab, 20, 1)
        l1.setFocus()
        lab1.setText('')
        lab2.setText('')
        lab3.setText('')
        lab4.setText('')
        lab5.setText('')
        lab6.setText('')
        lab7.setText('')
        lab8.setText('')
        lab9.setText('')

    def upd(self, args):
        
        nome = args[1][0].text()
        nome_f = args[1][1].text()
        lab = args[1][2].text()
        peso_l = args[1][3].text()
        val = args[1][4].text()
        uni = args[1][5].text()
        qtdt = args[1][6].text()
        qtdr = args[1][7].text()
        pet = args[1][8].text()
        
        if verifiedstring(nome, args[0][0]) and verifiedcient(nome_f, args[0][1]) and verifiedLab(lab, args[0][2]) and verifiedPeso(peso_l[0:2], args[0][3]) and verifiedData(val, args[0][4]) and verifiedNumber(uni, args[0][5]) and verifiedNumber(qtdt, args[0][6]) and verifiedNumber(qtdr, args[0][7]) and verifiedstring(pet, args[0][8]):
            try:
                
                up(SGM_DB, TABELA, args, self.datas)

            except IndexError:
                self.clearGrid()
                self.makeUpdateGrid()

            args[0][-1].setText('Registrado com sucesso!')
            QTimer.singleShot(3000, args[0][-1].hide)

            self.makeUpdateGrid()

    def foundOp(self):
        resume = self.principalLayout.leftLayout
        resume.la6.setStyleSheet('color: black;')
        self.clearGrid()
        path_ = self.principalLayout.rightLayout
        lf = self.principalLayout.leftLayout
        spaces_ = 10*' '
        self.principalLayout.leftLayout.la.setText('Função Buscar:')
        self.principalLayout.leftLayout.la.setStyleSheet('font-weight: bold;')
        self.principalLayout.leftLayout.la1.setText(f'{spaces_} Função que permite ao usuário')
        lf.la2.setText(f'{spaces_} buscar por um remédio ou pet')
        lf.la3.setStyleSheet('font-weight: normal')
        lf.la3.setText(f'{spaces_} no sistema, clicando no botão')
        lf.la4.setText(f'{spaces_} Consultar pet, passe o nome do')
        lf.la5.setText(f'{spaces_} animal que você procura para ver')
        lf.la6.setText(f'{spaces_} seus remédios. Para buscar por')
        lf.la7.setText(f'{spaces_} remédio clique em Buscar remédio')
        lf.la8.setText(f'{spaces_} e preencha os dados requeridos.')
        
        lab1 = QLabel('')
        lab2 = QLabel('')
        self.b1 = QPushButton('Consultar pet')
        b2 = QPushButton('Buscar Medicamento')
        lab4 = QLabel('')
        lab5 = QLabel('')
        lab6 = QLabel('')
        lab7 = QLabel('')
        lab8 = QLabel('')
        
        self.b1.setFixedSize(300, 50)
        b2.setFixedSize(300, 50)
        self.addToVerticalLayout([self.b1, b2, lab1, lab2, lab4, lab5, lab6], 1, 1, 1, True)
        self.addToVerticalLayout([lab7, lab8], 3, 2, 1)
        self.connectButtonClicked(self.b1, self.make(self.petFound, self.b1))
        self.connectButtonClicked(b2, self.makefoundGrid)
    
    def retorno(self, x):
        self.ob = x
        return
     
    def petFound(self, arg):
        lf = self.principalLayout.leftLayout
        nw = QWidget()
        ns = QScrollArea()
        ns.setWidgetResizable(True)
        ns.setWidget(nw)
        self.principalLayout.rightLayout.addWidget(nw, 5, 1)
        arg.hide()
        path_ = self.principalLayout.rightLayout
        exit_button = QLabel('Botão de fuga')
        exit_button = QLabel('')
        nome = QLabel('Nome do Pet:')
        line = OtherEdit(self, nw, path_, lf, exit_button)
        
        self.retorno(line)
        path_.addWidget(nome, 3, 1)
        path_.addWidget(line, 4, 1)
        path_.addWidget(exit_button)
        
    def makefoundGrid(self):
        self.makeUpdateGrid()
        self.clearGrid()
        path_ = self.principalLayout.rightLayout.addWidget

        l1 = QLabel('-')
        l2 = QLabel('-')
        l3 = QLabel('-')
        l4 = QLabel('-')
        l5 = QLabel('-')
        l6 = QLabel('-')
        l7 = QLabel('-')
        l8 = QLabel('-')
        l9 = QLabel('-')
        l10 = QLabel('-')

        path_(l1, 1, 2)
        path_(l2, 2, 2)
        path_(l3, 3, 2)
        path_(l4, 4, 2)
        path_(l5, 5, 2)
        path_(l6, 6, 2)
        path_(l7, 7, 2)
        path_(l8, 8, 2)
        path_(l9, 9, 2)
        path_(l10, 10, 2)

        id = QLabel('ID:')
        nome = QLabel('Nome:')
        nome_farmaceutico = QLabel('N. farmacêutico:')
        laboratorio = QLabel('Laboratório:')
        peso_liquido = QLabel('Peso L.:')
        validade = QLabel('Val.:')
        unidade = QLabel('Uni.:')
        qtd = QLabel('Quantidade Total.:')
        qtd_ = QLabel('Quantidade Rest.:')
        pet = QLabel('Pet:')

        lab = QLabel('')
        self.labelsList_.append(lab)
        b1 = QPushButton('Search')
        l = OtherEdits(lab, verifiedstring)
        self.editList3.append(l)
        nome_f = QLabel('Nome do medicamento:')

        path_(id, 1, 1)
        path_(nome, 2, 1)
        path_(nome_farmaceutico, 3, 1)
        path_(laboratorio, 4, 1)
        path_(peso_liquido, 5, 1)
        path_(validade, 6, 1)
        path_(unidade, 7, 1)
        path_(qtd, 8, 1)
        path_(qtd_, 9, 1)
        path_(pet, 10, 1)

        path_(nome_f, 12, 1)
        path_(l, 12, 2)
        l.setText('a')
        l.clear()
        path_(lab, 13, 2)
        path_(b1, 12, 3)
        self.enterPressed.connect(b1, self.make(self.inclui, [[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l],[lab, b1, nome_f]]))
        slot = self.make(self.inclui, [[l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l],[lab, b1, nome_f]])
        self.connectButtonClicked(b1, slot)
        l.setFocus()
    
    def submit_(self, args):

        nome = args[1][0].text()
        nome_f = args[1][1].text()
        lab = args[1][2].text()
        peso = args[1][3].text()
        val = args[1][4].text()
        uni = args[1][5].text()
        qtd = args[1][6].text()
        qtd_rest = args[1][7].text()
        pet = args[1][8].text()

        if args[0][0].state and args[0][1].state and args[0][2].state and args[0][3].state and args[0][4].state and args[0][5].state and args[0][6].state and args[0][7].state and args[0][8].state:
            for x in self.editList:
                x.clear()
            
            for x in self.labelsList_:
                x.setStyleSheet('color: red;')
            
            for x in self.labelsList_:
                x.setText('')

            RESULTADO = selectMed3(SGM_DB, TABELA_, pet.capitalize())
            if len(RESULTADO) < 1:
                
                self._showError('Não foi possível registrar', 'O nome do pet não foi encontrado no  sistema, registre-o primeiro!')
                return
            
            insert_med(SGM_DB, TABELA, (nome.capitalize(), nome_f.capitalize(), lab.capitalize(), f'{peso}mg' if peso != '-' else peso, val, uni, qtd, qtd_rest, pet.capitalize()))

            lab_ = QLabel('')
            self.principalLayout.rightLayout.addWidget(lab_, 20, 1)
            lab_.setText('Registrado com sucesso!')
            QTimer.singleShot(3000, lab_.hide)

            for x in args[0]:
                x.setText('a')
                x.clear()
            
            LISTA.clear()
            update_(SGM_DB, LISTA, TABELA)
        
    def upPets(self, args):
        oldname = args[0]
        resume = self.principalLayout.leftLayout
        resume.la6.setStyleSheet('color: black;')
        path_ = self.principalLayout.rightLayout.addWidget
        self.clearGrid()
        self.editList.clear()
        self.editList2.clear()
        self.labelsList_.clear()
        lf = self.principalLayout.leftLayout
        bold_ = 'font-weight: bold;'
        spaces_ = 10*' '

        resultados = contar(SGM_DB, TABELA_)

        self.principalLayout.leftLayout.la.setText('Registro de pets:')
        self.principalLayout.leftLayout.la1.setText(f'{spaces_}Há um total de {resultados[0][0]} pets registrados.' )
        lf.la3.setText('Função Adicionar pets:')
        lf.la3.setStyleSheet(bold_)
        lf.la4.setText(f'{spaces_} Fução que permite ao usuário adicionar')
        lf.la5.setText(f'{spaces_} novos pets ao sistema')
        lf.la6.setText(f'{spaces_} fornecendo os dados requeridos.')
        lf.la7.setText(f'{spaces_} É necessária para adição de medicamentos')
        lf.la8.setText(f'{spaces_} para novos pets.')

        lab14 = QLabel('')
        lab13 = QLabel('')
        lab12 = QLabel('')
        lab11 = QLabel('')        
        lab10 = QLabel('')
        lab9 = QLabel('')
        lab8 = QLabel('')
        lab7 = QLabel('')
        lab1 = QLabel('Novo nome:')
        lab1.setStyleSheet('font-size: 13px; font-weight: bold')
        lab2 = QLabel('')
        lab2.setStyleSheet('color: red;')
        lab3 = QLabel('Novo peso:')
        lab3.setStyleSheet('font-size: 13px; font-weight: bold')
        lab4 = QLabel('')
        lab4.setStyleSheet('color: red;')
        lab5 = QLabel('Cor:')
        lab5.setStyleSheet('font-size: 13px; font-weight: bold')
        lab6 = QLabel('')
        lab6.setStyleSheet('color: red;')
        self.labelsList_.append(lab2)
        self.labelsList_.append(lab4)
        self.labelsList_.append(lab6)
        line1 = OtherEdits(lab2, verifiedstring)
        line2 = OtherEdits(lab4, verifiedNumber)
        line3 = OtherEdits(lab6, verifiedstring)

        self.editList2.append(line1)
        self.editList2.append(line2)
        self.editList2.append(line3)

        send = QPushButton('Update pet')
        
        path_(lab14, 1, 1)
        lab14.setFixedSize(150, 150)
        path_(lab13, 1, 2)
        path_(lab12, 2, 2)
        path_(lab11, 3, 2)
        path_(lab10, 4, 2)
        path_(lab9, 5, 2)
        path_(lab8, 6, 2)
        path_(lab7, 7, 2)
        path_(lab1, 8, 2)
        path_(lab2, 9, 3)
        path_(lab3, 10, 2)
        path_(lab4, 11, 3)
        path_(lab5, 12, 2)
        path_(lab6, 13, 3)
        path_(line1, 8, 3)
        path_(line2, 10, 3)
        path_(line3, 12, 3)
        path_(send, 12, 4)
        
        line1.setText(f'{args[0]}')
        line2.setText(args[1])
        line3.setText(args[2])
        line1.setFocus()
        self.enterPressed.connect(send, self.make(self.sending, [[lab2, lab4, lab6],[line1, line2, line3, oldname]]))
        self.connectButtonClicked(send, self.make(self.sending, [[lab2, lab4, lab6],[line1, line2, line3, oldname]]))

    def sending(self, args):
        self.principalLayout.leftLayout.la.setText('Registro de Remédios')
        
        nome = args[1][0].text()
        peso = args[1][1].text().capitalize()
        cor = args[1][2].text().capitalize()
    
        if self.editList2[0].state and self.editList2[1].state and self.editList2[2].state:
            
            for x in self.labelsList_:
                x.setText('')
            
            for x in self.editList2:
                x.clear()

            upP(SGM_DB , TABELA_, (nome, peso, cor), args)

            args[0][0].setText('')
            args[0][1].setText('')
            args[0][2].setText('Atualizado com sucesso!')
            args[0][2].setStyleSheet('color: black;')
            self.makeUpdateGrid()

    def clearGrid(self):
    # Remove todos os widgets da grid
        for i in range(self.principalLayout.rightLayout.count()):
            widget = self.principalLayout.rightLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
        for x in self.principalLayout.leftLayout.labelList:
            x.setText("")

    def connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def configureLabels(self, args):
        if isinstance(args, QLabel):
            args.setStyleSheet('font-weight: bold; font-size: 13px')
            return
        
        for x in args:
            x.setStyleSheet('font-weight: bold; font-size: 13px')

    def buttonsSize(self, args, w, h):
        for x in args:
            x.setFixedSize(w, h)

    def addToLayout(self, x, args, y=None):
        y = 3 if y == None else y
        for z in args:
            self.principalLayout.rightLayout.addWidget(z, x, y,)
            y += 1
    
    def addToVerticalLayout(self, args, x, y, z, p = None):
        i = x
        if p is None:
            for l in args:
                self.principalLayout.rightLayout.addWidget(l, i, y)
                i+=z
            return
        
        for l in args:
            self.principalLayout.rightLayout.addWidget(l, i, y, 1, 1)
            i+=z
        

    def makeMsgBox(self):
        return QMessageBox()
    
    def makeDialog(self, text):
        msgbox = self.makeMsgBox()
        msgbox.setText(text)
        return msgbox
    
    def _showError(self, text, msg):
        msgbox = self.makeDialog(text)
        msgbox.setIcon(msgbox.Icon.Critical)
        msgbox.setStandardButtons(msgbox.StandardButton.Ok)# | msgbox.StandardButton.Cancel)
        msgbox.button(msgbox.StandardButton.Ok).setText('Ok')                
        msgbox.setInformativeText(msg)
        msgbox.setWindowTitle('Error')
        msgbox.exec()
    
    def _showInfo(self, text, msg):
        msgbox = self.makeDialog(text)
        msgbox.setIcon(msgbox.Icon.Information)
        msgbox.setStandardButtons(msgbox.StandardButton.Ok)# | msgbox.StandardButton.Cancel)
        msgbox.button(msgbox.StandardButton.Ok).setText('Ok')                
        msgbox.setInformativeText(msg)
        msgbox.setWindowTitle('Attention')
        msgbox.exec()