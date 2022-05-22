from classes import *


def separador(string):
    list = []
    counter = 0
    if len(string) % 2 == 1:
        list.append(string[0])
        counter += 1
    list += [string[i:i + 2] for i in range(counter, len(string), 2)]
    return string.converter(list)


def produto(self, ftr1, ftr2):
    # Converter a string recebida divida numa lista encadeada
    lista_fator1 = listar(ftr1)
    lista_fator2 = listar(ftr2)


def listar(self, lst):
    lista_dupla = Lista_Dupla()
    for i in lst:
        lista_dupla.add_tail(i)
    return lista_dupla
