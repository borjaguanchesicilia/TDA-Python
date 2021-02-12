import Nodo as n

n1 = n.Nodo(15)

print ("El dato del nodo 1 es: " + str(n1.dato))
print ("El siguiente nodo del nodo 1 es: " + str(n1.siguiente))

n2 = n.Nodo(16)
n1.siguiente = n2
print ("El dato del nodo 2 es: " + str(n2.dato))
print (n1.siguiente)
