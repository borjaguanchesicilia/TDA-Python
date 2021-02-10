import ListaEnlazada
import Nodo

listaSimple = ListaEnlazada()

n1 = Nodo("a")
listaSimple.cabeza = n1

n2 = Nodo("b")
n3 = Nodo("c")
n1.siguiente = n2
n2.siguiente = n3
print (listaSimple.mostrar())