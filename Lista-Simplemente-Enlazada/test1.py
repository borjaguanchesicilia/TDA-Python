import ListaEnlazada as le
import Nodo as nd

listaSimple = le.ListaEnlazada()

n1 = nd.Nodo("a")
listaSimple.cabeza = n1

n2 = nd.Nodo("b")
n3 = nd.Nodo("c")
n1.siguiente = n2
n2.siguiente = n3
print (listaSimple.mostrar())