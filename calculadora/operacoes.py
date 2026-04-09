
from math import *


def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    assert b != 0, "Proibido dividir por 0!"

def módulo(a):
    return sqrt(a**2)

def fatorial(a):
    if a == 1:
        return a
    elif a != 1:
        a *= fatorial(a-1)
        return a

def raizes_segundo_grau(a,b,c):    
    delta = b**2 - 4*a*c
    x1 = round((-b - sqrt(delta))/(2*a),2)
    x2 = round((-b + sqrt(delta))/(2*a),2)
    return [x1,x2]

