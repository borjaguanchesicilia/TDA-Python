import sys

class ListaEnlazada:

    def __init__(self):
        self.cabeza = None

    def insertarCabeza(self, nodo):
        nodo.setSiguiente(self.cabeza)
        self.cabeza = nodo

    def insertarN(self, anteriorNodo, nuevoNodo):
        nuevoNodo.setSiguiente(anteriorNodo.getSiguiente())
        anteriorNodo.setSiguiente(nuevoNodo)

    def queHayEnCabeza(self):
        return self.cabeza.getDato

    def extraerCabeza(self):
        aux = self.cabeza
        self.cabeza = self.cabeza.getSiguiente()
        aux.setSiguiente(None)

    def extraerN(self, anteriorNodo):
        if anteriorNodo == None:
            sys.exit()
        else:
            aux = anteriorNodo.getSiguiente()
            if anteriorNodo == None:
                sys.exit()
            else:
                anteriorNodo.setSiguiente(aux.getSiguiente())

    def recorrerLista(self):
        aux = self.cabeza
        print ("\nLa lista es: \n")
        while(aux != None):
            if aux.getSiguiente() != None:
                print (str(aux.getDato()) + " --> ",end="")
            else:
                print (str(aux.getDato()),end="")
            aux = aux.getSiguiente()
        print ("\n")