import NodoD as n
import ListaDoble as l

print ("\n\nProbamos el método extraer por cola.")

ListaDoble = l.ListaDoblementeEnlazada()

n1 = n.NodoD(1)

ListaDoble.insertarCola(n1)
ListaDoble.queHayEnCola()
ListaDoble.queHayEnCabeza()

n2 = n.NodoD(20)

ListaDoble.insertarCola(n2)
ListaDoble.queHayEnCola()
ListaDoble.queHayEnCabeza()


ListaDoble.recorrerLista()

n3 = n.NodoD(300)

ListaDoble.insertarCabeza(n3)
ListaDoble.queHayEnCola()
ListaDoble.queHayEnCabeza()

n4 = n.NodoD(4000)

ListaDoble.insertarCabeza(n4)
ListaDoble.queHayEnCola()
ListaDoble.queHayEnCabeza()

ListaDoble.recorrerLista()


ListaDoble.extraerCola()

ListaDoble.recorrerLista()