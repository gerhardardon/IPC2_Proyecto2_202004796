class node:  # SIRVE PARA GUARDAR UN COLOR POR NODO
    def __init__(self,id, nombre, tipo, capacidad=None, siguiente=None):
        self.id=id
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.siguiente = siguiente


class lista_drones:
    def __init__(self):
        self.root = None

    def agregar(self,id, nombre, tipo, capacidad=None):
        if self.root is None:
            self.root = node(id=id,nombre=nombre, tipo=tipo, capacidad=capacidad)
            return
        aux = self.root
        while aux.siguiente:
            aux = aux.siguiente
        aux.siguiente = node(id=id,nombre=nombre, tipo=tipo, capacidad=capacidad)

    def imprimir(self):
        node = self.root
        while node != None:
            if node.tipo == "ChapinFighter":
                print(node.id,")","    Nombre:", node.nombre, "tipo:",node.tipo, "capacidad:",node.capacidad)
            else:
                print(node.id,")","    Nombre:", node.nombre, "tipo:",node.tipo)
            node = node.siguiente

    def gettipo(self, x):
        node = self.root

        while node != None:
            if node.nombre == x:
                return node.tipo


            self.siguiente = node.siguiente
            node = self.siguiente
