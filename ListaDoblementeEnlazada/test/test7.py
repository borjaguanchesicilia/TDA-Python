import NodoD as n
import ListaDoble as l

ListaDoble = l.ListaDoblementeEnlazada()

n1 = n.NodoD(1)

ListaDoble.insertarCola(n1)

n2 = n.NodoD(20)

ListaDoble.insertarCola(n2)

n3 = n.NodoD(300)

ListaDoble.insertarCabeza(n3)

n4 = n.NodoD(4000)

ListaDoble.insertarCabeza(n4)

ListaDoble.recorrerLista()

print ("Extraemos el nodo 3 (300)")
ListaDoble.extraccionN(n3)

ListaDoble.recorrerLista()