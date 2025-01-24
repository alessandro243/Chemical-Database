import sqlite3
from db_utils import create_med, insert_med, create_pet, insert_pet
import shutil
SGM_DB = 'C:\\Users\\Thalita\\Desktop\\Alessandro\\Projeto SGM\\SGM.sqlite3'
TABELA = 'Medicamentos'
TABELA_ = 'Pet'
LISTA = []
if __name__ == '__main__':
    
    con = sqlite3.connect(SGM_DB)
    cursor = con.cursor()

    #pet_nome = input('Nome do pet: ')
    #pet_peso = input('Peso do pet: ')
    #pet_cor = input('Cor do pet: ')

    create_pet(cursor, TABELA_)
    #insert_pet(cursor, TABELA_, (pet_nome, pet_peso, pet_cor))
    con.commit()

    #in_nome1 = input('NOME_FANTASIA: ')
    #in_nome2 = input('NOME_FARMACÊUTICO: ')
    #in_lab = input('LABORATÓRIO: ')
    #in_peso_liquido = int(input('PESO_LÍQUIDO: '))
    #in_validade = input('VALIDADE: ')
    #in_unidade = int(input('UNIDADE: '))
    #in_quant_total = int(input('QUANTIDADE_TOTAL: '))
    #in_quant_restante = float(input('QUANTIDADE_RESTANTE: '))
    #in_pet = input('NOME DO PET: ')

    create_med(cursor, TABELA)
    #insert_med(cursor, TABELA, (
        #in_nome1,
        #in_nome2,
        #in_lab,
        #in_peso_liquido,
        #in_validade,
        #in_unidade,
        #in_quant_total,
        #in_quant_restante,
        #in_pet
    #))
   
    con.commit()

    cursor.execute(f'SELECT * FROM {TABELA}')

    for row in cursor.fetchall():
        if row not in LISTA:
            LISTA.append(row)

    cursor.close()
    con.close()