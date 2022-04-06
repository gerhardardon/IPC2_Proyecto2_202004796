class node:  # LISTA 2 CONTIENE CIUDADES POR FILA
    def __init__(self, y, content, siguiente=None):
        self.y = y
        self.content = content
        self.siguiente = siguiente


class lista_filas:
    def __init__(self):
        self.root = None

    def agregar(self, y, content):
        if self.root is None:
            self.root = node(y=y, content=content)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(y=y, content=content)

    def imprimir(self):
        node = self.root
        while node != None:
            print('Codigo: ', node.y, node.content)
            node = node.siguiente

    def buscar(self):
        node = self.root
        x=""
        while node != None:
            x=x+node.content.getcolor()
            node = node.siguiente
        return x

    def setcolor(self,x, y,color):
        node = self.root

        while node != None:
            if int(node.y) == int(y):
                node.content.setcolor(x,color)

            self.siguiente = node.siguiente
            node = self.siguiente


