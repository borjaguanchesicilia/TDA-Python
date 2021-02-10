class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def setSiguiente(self, nodo):
        self.siguiente = nodo

    def getSiguiente(self):
        return self.siguiente

    def setDato(self, dato):
        self.dato = dato

    def getDato(self):
        return self.dato