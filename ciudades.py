class nodo:  # LISTA 1 INFO DE CIUDADES
    def __init__(self,id, name, row, column, filas, siguiente=None):
        self.id=id
        self.name = name
        self.row = row
        self.column = column
        self.filas = filas
        self.siguiente = siguiente


class lista_ciudades:
    def __init__(self):
        self.root = None  # Crea la lista con un nodo null

    def agregar(self,id,name, row, column, filas):
        if self.root is None:  # si el primer nodo es null (vacio)
            self.root = nodo(id=id,name=name, row=row, column=column, filas=filas)
            return
        aux = self.root
        while aux.siguiente:  # busca un nodo que esté vacío
            aux = aux.siguiente
        aux.siguiente = nodo(id=id,name=name, row=row, column=column, filas=filas)

    def imprimir(self):
        node = self.root
        while node != None:
            print(node.id,')    ','CIUDAD:', node.name,'filas:',node.row, 'columnas',node.column)
            self.siguiente = node.siguiente
            node = self.siguiente

    def buscar(self, x):
        node = self.root
        while node != None:
            if node.name == x:
                x=node.filas.buscar()
                return x

            self.siguiente = node.siguiente
            node = self.siguiente

    def getrow(self, x):
        node = self.root

        while node != None:
            if node.name == x:
                return node.row


            self.siguiente = node.siguiente
            node = self.siguiente

    def getcolumn(self, x):
        node = self.root

        while node != None:
            if node.name == x:
                return node.column


            self.siguiente = node.siguiente
            node = self.siguiente

    def setcolor(self,nombre,x,y,color):
        node = self.root

        while node != None:
            if node.name == nombre:
                 node.filas.setcolor(x,y,color)

            self.siguiente = node.siguiente
            node = self.siguiente