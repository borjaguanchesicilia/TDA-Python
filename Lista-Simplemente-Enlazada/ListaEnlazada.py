class ListaEnlazada:

    def __init__(self):

        self.cabeza = None

    def mostrar(self):

        nodo = self.cabeza
        nodos = []
        while nodo is not None:
            nodos.append(nodo.dato)
            nodo = nodo.siguiente
        nodos.append("None")
        return(" --> ".join(nodos))