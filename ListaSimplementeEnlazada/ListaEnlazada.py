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
        print ("\nEn la cabeza hay: " + str(self.cabeza.getDato()))

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

    def buscarNodo(self, valor):
        aux = self.cabeza
        valorEncontrado = 0
        while ((aux != None) and (valorEncontrado == 0)):
            if aux.getDato() == valor:
                valorEncontrado = 1
            else:
                aux = aux.getSiguiente()

        if valorEncontrado == 1:
            print("\nEl valor fue encontrado.")
        else:
            print("\nEl valor NO fue encontrado.")
        