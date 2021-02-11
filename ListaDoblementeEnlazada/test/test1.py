import NodoD as n

n1 = n.NodoD(1)

print ("El dato del nodo 1 es: " + str(n1.dato))
print ("El siguiente nodo del nodo 1 es: " + str(n1.siguiente))

n2 = n.NodoD(20)
n1.setSiguiente(n2)
n2.setAnterior(n1)
print ("El dato del nodo 2 es: " + str(n2.dato))
print (n1.siguiente)
print (n1.anterior)

n3 = n.NodoD(300)
n2.setSiguiente(n3)
n3.setAnterior(n2)
print ("El dato del nodo 3 es: " + str(n3.dato))
print (n2.siguiente)
print (n2.anterior)
print (n3.anterior)