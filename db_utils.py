import sqlite3
from variables import SGM_DB
from win_utils import verifiedcient, verifiedstring, verifiedNumber, verifiedData

def makeList(bank, tabela):
    con = sqlite3.connect(SGM_DB)
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {tabela}')
    resutado = cursor.fetchall()
    cursor.close()
    con.close()
    return resutado

def create_pet(bank, tabela):
    con = sqlite3.connect(bank)
    cursor = con.cursor()
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {tabela} '
        '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'nome TEXT NOT NULL, '
        'peso REAL NOT NULL, '
        'cor TEXT NOT NULL'
        ')'
        )
    cursor.close()
    con.close()

def contar(bank, tabela):
    con = sqlite3.connect(bank)
    cursor = con.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {tabela}")
    resultados = cursor.fetchall()
    cursor.close()
    con.close()
    return resultados

def insert_pet(bank, tabela, datas: tuple):

    con = sqlite3.connect(bank)
    cursor = con.cursor()
    str_= f'INSERT INTO {tabela} (nome, peso, cor) VALUES (?, ?, ?)'

    cursor.execute(str_, datas)
    con.commit()
    cursor.close()
    con.close()


def create_med(bank, tabela):
    con = sqlite3.connect(bank)
    cursor = con.cursor()
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {tabela}'
        '('
        'ID INTEGER PRIMARY KEY AUTOINCREMENT, '
        'NOME_FANTASIA VARCHAR(30), '
        'NOME_FARMACÊUTICO VARCHAR(30), '
        'LABORATÓRIO VARCHAR(30), '
        'PESO_LÍQUIDO VARCHAR(30), '
        'VALIDADE VARCHAR(10), '
        'UNIDADE INTEGER, '
        'QUANTIDADE_TOTAL INTEGER, '
        'QUANTIDADE_RESTANTE REAL, '
        'Pet_nome VARCHAR(30) NOT NULL, FOREIGN KEY (pet_nome) REFERENCES Pet(nome)'
        ')'
        )
    cursor.close()
    con.close()

def insert_med(bank, tabela, datas: tuple):

    con = sqlite3.connect(SGM_DB)
    cursor = con.cursor()
    str_= f'INSERT INTO {tabela} (NOME_FANTASIA, NOME_FARMACÊUTICO, LABORATÓRIO, PESO_LÍQUIDO, VALIDADE, UNIDADE, QUANTIDADE_TOTAL, QUANTIDADE_RESTANTE, Pet_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(str_, datas)
    con.commit()
    cursor.close()
    con.close()

def update_(database, lista, tabela):
    con = sqlite3.connect(database)
    cursor = con.cursor()
    cursor.execute(f'SELECT * FROM {tabela}')

    for row in cursor.fetchall():
        
        if row not in lista:
            lista.append(row)

    cursor.close()
    con.close()

def selectMed(bank, tabela, nome):
    con = sqlite3.connect(bank)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE NOME_FANTASIA = '{nome}'")
    resutado = cursor.fetchall()
    cursor.close()
    con.close()
    return resutado

def selectall(bank, tabela):
    con = sqlite3.connect(bank)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {tabela}")
    resultados = cursor.fetchall()
    cursor.close()
    con.close()
    return resultados

def selectMed2(bank, tabela, nome):
    con = sqlite3.connect(SGM_DB)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE Pet_nome = '{nome}'")
    RESULTADO = cursor.fetchall()
    cursor.close()
    con.close()
    return RESULTADO

def selectMed3(bank, tabela, nome):
    con = sqlite3.connect(bank)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE nome = '{nome}'")
    resultado = cursor.fetchall()
    cursor.close()
    con.close()
    return resultado

def selectPet(bank, tabela):
    con = sqlite3.connect(SGM_DB)
    cursor = con.cursor()
    cursor.execute(f"SELECT NOME FROM {tabela}")
    resultado = cursor.fetchall()
    cursor.close()
    con.close()
    return resultado

def up(bank, tabela, args,  data2):

    nome = args[1][0].text()
    nome_f = args[1][1].text()
    lab = args[1][2].text()
    peso_l = args[1][3].text()
    val = args[1][4].text()
    uni = args[1][5].text()
    qtdt = args[1][6].text()
    qtdr = args[1][7].text()
    pet = args[1][8].text()
    old_name = data2[0][1]

    if verifiedstring(nome, args[0][0]) and verifiedcient(nome_f, args[0][1]) and verifiedcient(lab, args[0][2]) and verifiedNumber(peso_l, args[0][3]) and verifiedData(val, args[0][4]) and verifiedNumber(uni, args[0][5]) and verifiedNumber(qtdt, args[0][6]) and verifiedNumber(qtdr, args[0][7]) and verifiedstring(pet, args[0][8]):
        con = sqlite3.connect(SGM_DB)
        cursor = con.cursor()
        cursor.execute(f'UPDATE {tabela} SET '
                   'NOME_FANTASIA = ?, '
                   'NOME_FARMACÊUTICO = ?, '
                   'LABORATÓRIO = ?, '
                   'PESO_LÍQUIDO = ?, '
                   'VALIDADE = ?, '
                   'UNIDADE = ?, '
                   'QUANTIDADE_TOTAL = ?, '
                   'QUANTIDADE_RESTANTE = ?, '
                   'Pet_nome = ? '
                   'WHERE NOME_FANTASIA = ? ', (nome.capitalize(), nome_f.capitalize(), lab.capitalize(), peso_l, val, uni, qtdt, qtdr, pet.capitalize(), old_name)
                   )
        cursor.execute(f'SELECT * FROM {tabela} WHERE NOME_FANTASIA = ?', (nome,))
        row_after = cursor.fetchone()
        con.commit()
        cursor.close()
        con.close()

def up2(bank, tabela, args,  data2):
    
    nome = args[1][0].text()
    nome_f = args[1][1].text()
    lab = args[1][2].text()
    peso_l = args[1][3].text()
    val = args[1][4].text()
    uni = args[1][5].text()
    qtdt = args[1][6].text()
    qtdr = args[1][7].text()
    pet = args[1][8].text()
    old_name = data2[1]

    if verifiedstring(nome, args[0][0]) and verifiedcient(nome_f, args[0][1]) and verifiedstring(lab, args[0][2]) and verifiedNumber(peso_l, args[0][3]) and verifiedData(val, args[0][4]) and verifiedNumber(uni, args[0][5]) and verifiedNumber(qtdt, args[0][6]) and verifiedNumber(qtdr, args[0][7]) and verifiedstring(pet, args[0][8]):
        con = sqlite3.connect(SGM_DB)
        cursor = con.cursor()
        cursor.execute(f'UPDATE {tabela} SET '
                   'NOME_FANTASIA = ?, '
                   'NOME_FARMACÊUTICO = ?, '
                   'LABORATÓRIO = ?, '
                   'PESO_LÍQUIDO = ?, '
                   'VALIDADE = ?, '
                   'UNIDADE = ?, '
                   'QUANTIDADE_TOTAL = ?, '
                   'QUANTIDADE_RESTANTE = ?, '
                   'Pet_nome = ? '
                   'WHERE NOME_FANTASIA = ? ', (nome.capitalize(), nome_f.capitalize(), lab.capitalize(), peso_l, val, uni, qtdt, qtdr, pet.capitalize(), old_name)
                   )
        cursor.execute(f'SELECT * FROM {tabela} WHERE NOME_FANTASIA = ?', (nome,))
        row_after = cursor.fetchone()
        con.commit()
        cursor.close()
        con.close()