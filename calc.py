from classes import *
from functions import *

print("\t\t\tCalculo duplamente encadeado de \n\tfatores grandes demais para um espaço pequeno.")

fator1 = separador(input("Escreva uma string numérica: "))
fator2 = separador(input("Escreva uma string numérica: "))

resultado = produto(fator1, fator2)

print(f"O produto desses fatores é: {resultado}")



