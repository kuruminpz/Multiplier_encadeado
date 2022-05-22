""""
Arquivo gerado para a criação de classes
e definições pertinentes ao algoritmo
"""


class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = None # ponteiro pro próximo
        self.prev = None # ponteiro pro anterior


class Lista_Dupla:
    def __init__(self):
        self.head = None # inicio
        self.tail = None # final
        self.size = 0


    def vazia(self):
        if self.head is None:
            return True
        else:
            return False

    def add_head(self, valor):
        no = Node(valor)
        if self.vazia():
            self.head = self.tail = no
        else:
            no.next = self.head
            self.head.prev = no
            no.prev = None
            self.head = no
        self.size += 1

    def add_tail(self, valor):
        no = Node(valor)
        if self.vazia():
            self.head = self.tail = no
        else:
            self.tail.next = no
            no.prev = self.tail
            no.next = None
            self.tail = no
        self.size += 1

