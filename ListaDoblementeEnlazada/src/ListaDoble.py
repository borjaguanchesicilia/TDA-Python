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
            self.cabeza.anterior = nodo
            self.cabeza = nodo
        self.tam += 1

    def insertarCola(self, nodo):
        if self.tam == 0:
            self.cabeza = self.cola = nodo
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo    
        self.tam += 1

    def queHayEnCabeza(self):
        print ("\nEn la cabeza hay: " + str(self.cabeza.dato))

    def queHayEnCola(self):
        print ("\nEn la cola hay: " + str(self.cola.dato))

    def extraerCabeza(self):
        assert self.tam != 0, 'La lista está vacía'
        aux = self.cabeza
        self.cabeza = self.cabeza.siguiente
        if self.cabeza != None:
            self.cabeza.anterior = None
        else:
            self.cola = None

        self.tam -=1
        aux.siguiente = None

    def extraerCola(self):
        assert self.tam != 0, 'La lista está vacía'
        aux = self.cola
        self.cola = self.cola.anterior
        if self.cola != None:
            self.cola.siguiente = None
        else:
            self.cabeza = None

        self.tam -=1
        aux.anterior = None

    def extraccionN(self, nodo):
        assert nodo != None
        if nodo.anterior != None:
            aux = nodo.siguiente
            nodoAnterior = nodo.anterior
            nodoAnterior.siguiente = aux
        else:
            self.cabeza = nodo.siguiente

        if nodo.siguiente != None:
            aux = nodo.anterior
            nodoSiguiente = nodo.siguiente
            nodoSiguiente.anterior = aux

        else:
            self.cola = nodo.anterior

        del nodo
        self.tam -= 1

    def recorrerLista(self):
        aux = self.cabeza
        print ("\nLa lista es: \n")
        while(aux != None):
            if (aux.siguiente != None):
                print (str(aux.dato) + " <--> ",end="")
            else:   
                print (str(aux.dato),end="")
            aux = aux.siguiente
        print ("\n")