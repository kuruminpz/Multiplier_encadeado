from classes import *


def separador(string):
    list = []
    counter = 0
    if len(string) % 2 == 1:
        list.append(string[0])
        counter += 1
    list += [string[i:i + 2] for i in range(counter, len(string), 2)]
    return string.converter(list)


def listar(self, lst):
    lista_dupla = Lista_Dupla()
    for i in lst:
        lista_dupla.add_tail(i)
    return lista_dupla


def produto(self, ftr1, ftr2):
    # Converter a string recebida divida numa lista encadeada
    lista_fator1 = listar(ftr1)
    lista_fator2 = listar(ftr2)

    final1 = lista_fator1.tail
    final2 = lista_fator2.tail
    final1_result = None
    final2_result = None

    over = 0
    result = 0
    num1 = 0
    num2 = 0
    num_result = ""

    while final1 != None:
        final2 = lista_fator2.tail
        seg1 = int(final1.dado) # Seg == segmento, referenciando parte do fator
        final2_result = final1_result
        while final2 != None:
            seg2 = int(final2.dado)
            result = seg1 * seg2

