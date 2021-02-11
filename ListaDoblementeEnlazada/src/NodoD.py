class NodoD:
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def setSiguiente(self, nodo):
        self.siguiente = nodo

    def setAnterior(self, nodo):
        self.anterior = nodo

    def setDato(self, dato):
        self.dato = dato