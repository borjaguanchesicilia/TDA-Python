class ListaEnlazada:
    
    def __init__(self):
        self.cabeza = None

    def insertarCabeza(self, nodo):
        nodo.siguiente = self.cabeza
        self.cabeza = nodo

    def insertarN(self, anteriorNodo, nuevoNodo):
        nuevoNodo.siguiente = anteriorNodo.siguiente
        anteriorNodo.siguiente = nuevoNodo

    def queHayEnCabeza(self):
        print ("\nEn la cabeza hay: " + str(self.cabeza.dato))

    def extraerCabeza(self):
        assert self.cabeza != None, 'No hay ningún nodo en la lista.'
        aux = self.cabeza
        self.cabeza = self.cabeza.siguiente
        aux.siguiente = None

    def extraerN(self, anteriorNodo):
        assert anteriorNodo != None, 'No hay ningún nodo en la lista.'
        aux = anteriorNodo.siguiente
        anteriorNodo.siguiente = aux.siguiente

    def recorrerLista(self):
        aux = self.cabeza
        print ("\nLa lista es: \n")
        while(aux != None):
            if aux.siguiente != None:
                print (str(aux.dato) + " --> ",end="")
            else:
                print (str(aux.dato),end="")
            aux = aux.siguiente
        print ("\n")

    def buscarNodo(self, valor):
        aux = self.cabeza
        valorEncontrado = 0
        while ((aux != None) and (valorEncontrado == 0)):
            if aux.dato == valor:
                valorEncontrado = 1
            else:
                aux = aux.siguiente

        if valorEncontrado == 1:
            print("\nEl valor fue encontrado.")
        else:
            print("\nEl valor NO fue encontrado.")
        