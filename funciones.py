import itertools
from itertools import product

def prefijos(entrada_de_la_cadena):
    resultado=["ε"]
    for i in range(1, len(entrada_de_la_cadena) + 1):
        resultado.append(entrada_de_la_cadena[:i])
    return resultado

def sufijos(entrada_de_la_cadena):
    resultado=["ε"]
    for i in range(len(entrada_de_la_cadena), -1, -1):
        resultado.append(entrada_de_la_cadena[i:])
    return resultado
##
def subcadenas(entrada_de_la_cadena):
    resultado=["ε"]
    for i in range(len(entrada_de_la_cadena)):
        for j in range (i+1, len(entrada_de_la_cadena) + 1):
            resultado.append(entrada_de_la_cadena[i:j])
    return resultado

def kleene(alfabeto, max_longitud):
    resultado = []
    for k in range(0, max_longitud + 1):
        for combinacion in product(alfabeto, repeat=k):
            cadena = "".join(combinacion)
            resultado.append(cadena)
    return resultado

def positiva(alfabeto, max_longitud):
    resultado = []
    for i in range(1, max_longitud + 1):  #empezamos en1
        for combinacion in product(alfabeto, repeat=i):
            cadena = "".join(combinacion)
            resultado.append(cadena)
    return resultado