import Pila as p

print ("\nProbamos el método que hay en el top.")

miPila = p.Pila()

miPila.vacia()

for i in range(5):
    miPila.push(i)

miPila.mostrar()

miPila.queHayEnTop()