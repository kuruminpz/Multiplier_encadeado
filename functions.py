from classes import *


def separador(string):
    list = []
    counter = 0
    if len(string) % 2 == 1:
        list.append(string[0])
        counter += 1
    list += [string[i:i + 2] for i in range(counter, len(string), 2)]
    return list


def listar(self, lst):
    lista_dupla = Lista_Dupla()
    for i in lst:
        lista_dupla.add_tail(i)
    return lista_dupla


def produto(self, ftr1, ftr2):
    # Converter a string recebida divida numa lista encadeada
    lista_fator1 = listar(ftr1)  # lista que armazena o fator1
    lista_fator2 = listar(ftr2)  # lista que armazena o fator2
    lista_final = Lista_Dupla()  # lista que armazena o resultado
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
        seg1 = int(final1.dado)  # Seg == segmento, referenciando parte do fator
        final2_result = final1_result
        while final2 != None:
            seg2 = int(final2.dado)
            result = seg1 * seg2
            if final2_result is not None:
                result += int(final2_result.dado)
                over = result // 100
                result -= over * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                final2_result.dado = str(result)
                if final2_result.prev is None:
                    if final2.prev is not None:
                        lista_final.add_head(str(over))
                    else:
                        if over != 0:
                            lista_final.add_head(str(over))
                else:
                    final2_result.prev.dado = str(over + int(final2_result.anterior.dado))
            elif lista_final.head is not None:
                result += int(lista_final.head.dado)
                over = result // 100
                result -= over * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                    lista_final.head.dado = str(result)
                if final2.anterior is not None:
                    lista_final.add_head(str(over))
                elif over != 0:
                    lista_final.add_head(str(over))
            else:
                over = result // 100
                result -= over * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                lista_final.add_head(str(result))
                lista_final.add_head(str(over))
            if final2_result is not None:
                final2_result = final2_result.prev
            final2 = final2.prev
        if final1_result is None:
            final1_result = lista_final.tail.prev
        final1 = final1.anterior
    while not lista_final.vazia():
        num_result += lista_final.pop_head()
    return num_result
