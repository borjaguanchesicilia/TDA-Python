import ListaEnlazada as l
import Nodo as n


listaSimple = l.ListaEnlazada()

for i in range(5):
    aux = n.Nodo(i)
    listaSimple.insertarCabeza(aux)

listaSimple.recorrerLista()

listaSimple.queHayEnCabeza()

listaSimple.extraerCabeza()
listaSimple.recorrerLista()

print("\nEl valor a buscar es el 20...")
listaSimple.buscarNodo(20)

print("\nEl valor a buscar es el 2...")
listaSimple.buscarNodo(2)

n1 = n.Nodo(10)
listaSimple.insertarCabeza(n1)
listaSimple.recorrerLista()
n2 = n.Nodo(20)
listaSimple.insertarCabeza(n2)
listaSimple.recorrerLista()

n3 = n.Nodo(300)
listaSimple.insertarN(n1, n3)
listaSimple.recorrerLista()

listaSimple.extraerN(n1)
listaSimple.recorrerLista()