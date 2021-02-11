import NodoD as n
import ListaDoble as l

ListaDoble = l.ListaDoblementeEnlazada()

n1 = n.NodoD(1)
print (n1.dato)

ListaDoble.insertarCabeza(n1)

ListaDoble.queHayEnCabeza()

ListaDoble.queHayEnCola()