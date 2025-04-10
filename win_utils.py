def hollowVari(word, label):
    if len(word) < 1:
        label.setText('Você não digitou nada')
        return False
    return True

#strin fuctions
def verifiedcient(word, label):
    label.setStyleSheet('color: red;')
    veri_3 = hollowVari(word, label)

    if not veri_3:
        return False
    veri_4 = spaceInit(word, label)
    veri_1 = verifyWord(word, label)
    veri_2 = noNumbnoDig(word, label)
    if veri_1 and veri_2 and veri_3 and veri_4:
        label.setText('')
        return True
    return False

def noNumbnoDig(word, label):
    for x in word:
        if not x.isdigit() and not x.isalpha() and not x == ' ':
            label.setText('Não digite símbolos')
            return False
        
    return True

def spaceInit(word, label):
    if word[0] == ' ':
        label.setText('O nome não deve começar com espaço')
        return False
    return True

def verifiedstring(word, label):
    label.setStyleSheet('color: red;')
    veri_3 = hollowVari(word, label)

    if not veri_3:
        return False
    
    veri_1 = verifyWord(word, label)
    veri_2 = numberWord(word, label)
    if veri_1 and veri_2 and veri_3:
        label.setText('')
        return True
    return False


def verifyWord(word, label):
    first_ = word[0]
    if word == first_ * len(word):
        label.setText('Dado inválido')
        return False
    return True

def numberWord(word, label):
    for x in word:
        if x.isdigit() or not x.isalpha() and not x == ' ':
            label.setText('Digite apenas letras')
            return False
    
    return True

#number functions

def verifiedNumber(number, label):
    label.setStyleSheet('color: red;')
    veri_3 = fewDots(number, label)
    veri_2 = hollowVari(number, label)

    if not veri_2:        
        return False
    
    veri_1 = alphaNumbers(number, label)

    if veri_1.is_integer():
        int(veri_1)

    if veri_1 and veri_3:
        return True
    
    return False

def alphaNumbers(number, label):
    for x in number:
        y = x == '.'
        if not x.isdigit() and not y:
            label.setText('Digite apenas números')
            return False
    
    return True

def fewDots(number, label):
    if number.count('.') > 1:
        label.setText('Número inválido')
        return False
    return True

#data functions

def verifiedData(data, label):
    label.setStyleSheet('color: red;')
    
    vari_3 = checkBar(data, label)
    vari_2 = hollowVari(data, label)
    if not vari_2:
        return False

    vari_5 = largeData(data, label)

    if not vari_5:
        return False

    vari_4 = positionBar(data, label)
    vari_1 = verifyNumbers(data, label)
    vari_6 = plusthan12(data, label)
    
    if vari_1 and vari_2 and vari_3 and vari_4 and vari_5 and vari_6:
    
        return True
    return False

def verifyNumbers(data, label):
    if not data == '-':
    
        for x in data:
            if x.isalpha() or x == '-':
                label.setText('Não deve conter letras ou hífens')
                return False
    
    return True

def checkBar(data, label):
    if data.count('/') > 1 and data != '-':
        label.setText('Formato inválido, siga a máscara: MM/YYYY')
        return False
    return True

def positionBar(data, label):
    if not data == '-':
        if data[2] != '/':
            label.setText('Formato inválido, siga a máscara: MM/YYYY')
            return False
    return True

def largeData(data, label):
    if (len(data) < 7 or len(data) > 7) and data != '-':
        label.setText('Formato inválido, siga a máscara: MM/YYYY')
        return False
    return True

def plusthan12(data, label):
    mes = data[0:2]
    if not data == '-':
        if int(mes) > 12 and data != '-':
            label.setText('Mês inválido')
            return False
    return True

def verifiedPeso(valor, label):
    label.setStyleSheet('color: red;')

    veri_1 = hollowVari(valor, label)

    if not veri_1:
        return False
    
    veri_2 = haveSpaceOrDot(valor, label)
    veri_3 = verifyNumbers(valor, label)
    
    if veri_1 and veri_2 and veri_3:
        return True
    
def defintive(valor, label):

    if valor[-2] == 'm' and valor[-1] == 'g' and valor [0:-2].isdigit():
        return True
    
def haveSpaceOrDot(valor, label):
    if valor.isdigit():
        if int(valor) > 0:
            return True

    if not valor == '-':
        for x in valor:
            if x == ' ' or x == '.' or '-':
                label.setText('Não deve conter espaços, pontos ou números justons a hífens')
                return False
        
    return True

def definitiveLab(valor):
    if valor == '-':
        return True

def verifiedLab(valor, label):
    label.setStyleSheet('color: red;')
    veri_3 = hollowVari(valor, label)

    if not veri_3:
        return False
    
    vari_5 = definitiveLab(valor)

    if vari_5:
        return True
    
    veri_4 = spaceInit(valor, label)
    veri_1 = verifyWord(valor, label)
    veri_2 = noNumbnoDig(valor, label)

    if veri_1 and veri_2 and veri_3 and veri_4:
        label.setText('')
        return True
    return False
    
