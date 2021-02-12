import Pila as p

print ("\nProbamos el método push y vacía.")

miPila = p.Pila()

miPila.vacia()

for i in range(5):
    miPila.push(i)

miPila.mostrar()

miPila.vacia()