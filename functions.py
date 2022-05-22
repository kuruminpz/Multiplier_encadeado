from classes import *

def separador(string):
    list = []
    counter = 0
    if len(string) % 2 == 1:
        list.append(string[0])
        counter += 1
    list += [string[i:i + 2] for i in range(counter, len(string), 2)]
    return string.converter(list)

def produto(self,fator1,fator2):
    #TODO implement
    pass
