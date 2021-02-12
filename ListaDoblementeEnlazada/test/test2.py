import NodoD as n
import ListaDoble as l

print ("\n\nProbamos el método insertar por cabeza, y los qué hay en cabezay en cola.")

ListaDoble = l.ListaDoblementeEnlazada()

n1 = n.NodoD(1)
print (n1.dato)

ListaDoble.insertarCabeza(n1)

ListaDoble.queHayEnCabeza()

ListaDoble.queHayEnCola()