#Criar uma calculadora utilizando conceitos vistos previamente para executar
#as operações a seguir:
#Soma, subtração, divisão, multiplicação
#fatorial, elevação, raiz, porcentagem, logaritmos
#TEM QUE CONTER CONTASNTES: PI, Euler

import math

PI = math.pi
EULER = math.e

def soma(x, y):
    return x + y
     
def subtracao(x, y):
    return x - y
    
def divisao(x, y):
    return x / y
    
def multiplicacao(x, y):
    return x * y

def fatorial(x):
    aux = 1
    while x > 0:
        aux = aux*x
        x=x-1
    return aux
    
def elevacao(x, y):
    if y == 1:
        return x
    else:
        return x * elevacao(x, y-1)
    
def raiz(x, y):
    expoente = 1/y
    return x ** expoente

def porcentagem(x, y):
    return (x/100)*y
    
def logaritmos(x):
    return math.log10(x)

print("soma")
print(soma(5, 8))
print("subtracao")
print(subtracao(6, 2)) 
print("divisao")
print(divisao(7, 2))
print("multiplicacao")
print(multiplicacao(8, 2)) 
print("fatorial")
print(fatorial(12))
print("elevacao")
print(elevacao(3,4)) 
print("raiz")
print(raiz(27, 3))
print("porcentagem")
print(porcentagem(25, 200)) 
print("logaritmos")
print(logaritmos(3))
print("pi")
print(PI)
print("euler")
print(EULER)
