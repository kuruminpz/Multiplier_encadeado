""""
Arquivo gerado para a criação de classes
e definições pertinentes ao algoritmo
"""


class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None
        self.prev = None


class Lista_Dupla:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0



    def vazia(self):
        if self.inicio is None:
            return True
        else:
            return False

    def adicionar_inicio(self, valor):
        no = No(valor)
        if self.vazia():
            self.inicio = self.fim = no
        else:
            no.proximo = self.inicio
            self.inicio.anterior = no
            no.anterior = None
            self.inicio = no
        self.tamanho += 1

    def adicionar_fim(self, valor):
        no = No(valor)
        if self.vazia():
            self.inicio = self.fim = no
        else:
            self.fim.proximo = no
            no.anterior = self.fim
            no.proximo = None
            self.fim = no
        self.tamanho += 1





    def calcular(self,list1,list2):
        # todo implementar o calculo ja com as listas em formas numericas
        pass


