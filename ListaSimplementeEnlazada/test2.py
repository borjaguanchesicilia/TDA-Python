import ListaEnlazada as l
import Nodo as n

listaSimple = l.ListaEnlazada()

n1 = n.Nodo(1)
listaSimple.insertarCabeza(n1)
n2 = n.Nodo(20)
listaSimple.insertarCabeza(n2)
n3 = n.Nodo(300)
listaSimple.insertarCabeza(n3)

listaSimple.recorrerLista()