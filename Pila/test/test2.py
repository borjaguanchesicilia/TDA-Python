import Pila as p

print ("\nProbamos el método pop.")

miPila = p.Pila()

miPila.vacia()

miPila.push(1)
miPila.push(2)
miPila.push(3)
miPila.push(4)

miPila.mostrar()

miPila.pop()

miPila.mostrar()

miPila.vacia()