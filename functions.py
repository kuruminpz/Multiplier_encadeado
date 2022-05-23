from classes import *


def separador(string):
    list = []
    counter = 0
    if len(string) % 2 == 1:
        list.append(string[0])
        counter += 1
    list += [string[i:i + 2] for i in range(counter, len(string), 2)]
    return list


def listar(lst):
    lista_dupla = Lista_Dupla()
    for i in lst:
        lista_dupla.add_tail(i)
    return lista_dupla


def produto(ftr1, ftr2):
    list_factor1 = listar(ftr1)
    list_factor2 = listar(ftr2)
    list_final = Lista_Dupla()
    final1 = list_factor1.tail
    final2 = list_factor2.tail
    final1_result = None
    final2_result = None
    over = 0
    result = 0
    num_result = ""

    while final1 is not None:
        final2 = list_factor2.tail
        seg1 = int(final1.dado)
        final2_result = final1_result
        while final2 is not None:
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
                        list_final.add_head(str(over))
                    else:
                        if over != 0:
                            list_final.add_head(str(over))
                else:
                    final2_result.prev.dado = str(over + int(final2_result.prev.dado))
            elif list_final.head is not None:
                result += int(list_final.head.dado)
                over = result // 100
                result -= over * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                    list_final.head.dado = str(result)
                if final2.prev is not None:
                    list_final.add_head(str(over))
                elif over != 0:
                    list_final.add_head(str(over))
            else:
                over = result // 100
                result -= over * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                list_final.add_head(str(result))
                list_final.add_head(str(over))

            if final2_result is not None:
                final2_result = final2_result.prev
            final2 = final2.prev

        if final1_result is None:
            final1_result = list_final.tail.prev
        else:
            final1_result = final1_result.prev
        final1 = final1.prev

    while not list_final.vazia():
        num_result += list_final.pop_head()
    return num_result
