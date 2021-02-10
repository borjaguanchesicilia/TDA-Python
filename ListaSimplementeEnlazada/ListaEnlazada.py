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