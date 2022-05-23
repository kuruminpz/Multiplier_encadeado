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

    def del_head(self):
        if self.vazia():
            raise TypeError("Lista está vazia!")
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def del_tail(self):
        if self.vazia():
            raise TypeError("Lista está vazia!")
        elif self.size == 1:
            self.del_head()
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def pop_head(self):
        valor = self.head.dado
        self.del_head()
        return valor

    def pop_tail(self):
        valor = self.tail.dado
        self.del_tail()
        return valor