import sys
sys.setrecursionlimit(15000)

def iniciaCaixa():
    '''
    Solicita o número de cédulas de cada tipo disponível no caixa
    '''
    caixa = {}
    for cedula in cedulas:
        ncedulas = input (f"# de cédulas de R${cedula:3d} no caixa: ")
        caixa[cedula] = int(ncedulas)
    return caixa


def valorEmCedulas (valor, limites):
    '''
    Converte um valor nas cedulas que o representam.
    Eventualmente limita ao caixa e um limite passado
    para cada cedula.
    '''
    qtdeCedulas = {}
    for cedula in cedulas:
            ncedulas = min (valor // cedula, limites[cedula])
            qtdeCedulas[cedula] = ncedulas
            valor -= cedula * ncedulas
    if valor == 0:
        return qtdeCedulas
    else:
        return None

def getLimites (valor):
    limites = {}
    for cedula in cedulas:
        limites[cedula] = min(valor // cedula, caixa[cedula])
    return limites

def getTroco (valorTroco):
    limites = getLimites(valorTroco)
    print ("Limites:", limites)
    tryLimites = {}
    for ced100 in range(limites[100], -1, -1):
        tryLimites[100] = ced100
        for ced50 in range(limites[50], -1, -1):
            tryLimites[50] = ced50
            for ced20 in range(limites[20], -1, -1):
                tryLimites[20] = ced20
                for ced10 in range(limites[10], -1, -1):
                    tryLimites[10] = ced10
                    for ced5 in range(limites[5], -1, -1):
                        tryLimites[5] = ced5
                        for ced2 in range(limites[2], -1, -1):
                            tryLimites[2] = ced2
                            for ced1 in range(limites[1], -1, -1):
                                tryLimites[1] = ced1
                                print (valorTroco, tryLimites)
                                troco = valorEmCedulas(valorTroco, tryLimites)
                                if troco != None:
                                    return troco
    return None

def showQtdeCedulas (header, valor):
    '''
    Mostra a quantidade de cédulas de um valor.
    '''
    print (header, " - Cédulas:\n", '-'*40, sep='')
    for cedula in troco:
        if valor[cedula] > 0:
            print (f"# de cédulas de R$ {cedula:3d}: {valor[cedula]:2}")
    print ('-'*40)


cedulas = [100, 50, 20, 10, 5, 2, 1]
print (40*'-',"\nIniciando caixa\n",30*'-',sep='')
#caixa = iniciaCaixa()
caixa = {100:10, 50:10, 20:10, 10:0, 5:0, 2:0, 1:0}
print (40*'-',"\nCaixa aberto\n",40*'-',sep='')

while True:
    valorConta = 10 # int(input ("Valor da conta (R$): "))
    valorPgto = 270 #int(input ("Valor pago (R$): "))
    valorTroco = valorPgto - valorConta
    if valorTroco >= 0:
        print ("Troco:", valorTroco)
        print (40*'-')
        troco = getTroco (valorTroco)
        if troco != None:
            showQtdeCedulas ("Troco", troco)
            showQtdeCedulas ("Situaçãoo do caixa", caixa)
        else:
            print ("O caixa não tem cédulas disponíveis para o troco!!!")
    else:
        print ("O pagamento não cobre o valor da conta!!!")
    break