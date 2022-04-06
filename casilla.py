class node:  # SIRVE PARA GUARDAR UN COLOR POR NODO
    def __init__(self,x, color, siguiente=None):
        self.x=x
        self.color = color
        self.siguiente = siguiente


class lista_casilla:
    def __init__(self):
        self.root = None

    def agregar(self, x, color):
        if self.root is None:
            self.root = node(x=x,color=color)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(x=x,color=color)

    def imprimir(self):
        node = self.root
        while node != None:
            print('Color: ', node.x, node.color)
            node = node.siguiente


    def getcolor(self):
        node = self.root
        x=""
        while node != None:
            x = x+ node.color
            node = node.siguiente
        return x



    def setcolor(self, x, color): #x es el id de casilla y x2 el nuevo color
        node = self.root

        while node != None:
            if int(node.x) == int(x):
                node.color = color

            self.siguiente = node.siguiente
            node = self.siguiente