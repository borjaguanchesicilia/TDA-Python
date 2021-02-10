import ListaEnlazada as l
import Nodo as n

print ("\n\nProbamos el método insertar por cabeza.")

listaSimple = l.ListaEnlazada()

n1 = n.Nodo(1)
listaSimple.insertarCabeza(n1)
listaSimple.recorrerLista()
n2 = n.Nodo(20)
listaSimple.insertarCabeza(n2)
listaSimple.recorrerLista()
n3 = n.Nodo(300)
listaSimple.insertarCabeza(n3)
listaSimple.recorrerLista()