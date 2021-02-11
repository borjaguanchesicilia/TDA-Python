class ListaDoblementeEnlazada:
    
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tam = 0

    def insertarCabeza(self, nodo):
        if self.tam == 0:
            self.cabeza = self.cola = nodo
        else:
            nodo.siguiente = self.cabeza
            aux = nodo.anterior
            self.cabeza = aux
            self.cabeza = nodo
        self.tam += 1

    def queHayEnCabeza(self):
        print ("\nEn la cabeza hay: " + str(self.cabeza.dato))

    def queHayEnCola(self):
        print ("\nEn la cola hay: " + str(self.cola.dato))