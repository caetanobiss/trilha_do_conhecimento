#calcular um número elevado a outro numero utilizando uma função recursiva
#ENTRADA: 3, 3
#SAIDA: 27

def calcular_elevacao(raiz, expoente):
    if expoente == 1:
        return raiz
    else:
        return raiz * calcular_elevacao(raiz, expoente-1)

raiz = float(input("Informe a raiz do valor"))
expoente = float(input("Informe o expoente do valor"))
print(calcular_elevacao(raiz,expoente))
