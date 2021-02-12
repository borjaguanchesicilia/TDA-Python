import Pila as p

print ("\nProbamos el método pop.")

miPila = p.Pila()

miPila.vacia()

for i in range(5):
    miPila.push(i)

miPila.mostrar()

miPila.pop()

miPila.mostrar()

miPila.vacia()