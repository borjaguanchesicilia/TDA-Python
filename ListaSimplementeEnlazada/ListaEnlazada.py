class ListaEnlazada:

    def __init__(self):

        self.cabeza = None

    def insertarCabeza(self, nodo):
        nodo.setSiguiente(self.cabeza)
        self.cabeza = nodo

    def queHayEnCabeza(self):
        return self.cabeza.getDato

    def recorrerLista(self):
        aux = self.cabeza
        while(aux != None):
            print ("El dato  es: " + str(aux.getDato()) + "\n\n")
            aux = aux.getSiguiente()