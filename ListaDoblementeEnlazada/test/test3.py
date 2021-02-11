import NodoD as n
import ListaDoble as l

ListaDoble = l.ListaDoblementeEnlazada()

n1 = n.NodoD(1)
print (n1.dato)

ListaDoble.insertarCabeza(n1)

ListaDoble.queHayEnCabeza()

ListaDoble.queHayEnCola()


n2 = n.NodoD(20)
print (n2.dato)

ListaDoble.insertarCola(n2)

ListaDoble.queHayEnCabeza()

ListaDoble.queHayEnCola()