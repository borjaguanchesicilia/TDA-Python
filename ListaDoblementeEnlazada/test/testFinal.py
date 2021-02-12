import NodoD as n
import ListaDoble as l


ListaDobleCa = l.ListaDoblementeEnlazada()
ListaDobleCo = l.ListaDoblementeEnlazada()

n1 = n.NodoD(10)
ListaDobleCa.insertarCabeza(n1)

for i in range(5):
    aux = n.NodoD(i)
    ListaDobleCa.insertarCabeza(aux)

ListaDobleCa.recorrerLista()

ListaDobleCa.extraerCabeza()
print ("\nExtraemos el nodo n1, que va a coincidir con la cola de la lista.")
ListaDobleCa.extraccionN(n1)

ListaDobleCa.recorrerLista()


n2 = n.NodoD(10)
ListaDobleCo.insertarCola(n2)

for i in range(5):
    aux = n.NodoD(i)
    ListaDobleCo.insertarCola(aux)

ListaDobleCo.recorrerLista()

ListaDobleCo.extraerCola()
print ("\nExtraemos el nodo n2, que va a coincidir con la cabeza de la lista.")
ListaDobleCo.extraccionN(n2)

ListaDobleCo.recorrerLista()