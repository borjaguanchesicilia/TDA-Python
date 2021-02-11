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
            self.cola.anterior = nodo
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
        aux = self.cabeza
        self.cabeza = self.cabeza.siguiente
        if self.cabeza != None:
            self.cabeza.anterior = None
        else:
            self.cola = None

        self.tam -=1
        aux.siguiente = None

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