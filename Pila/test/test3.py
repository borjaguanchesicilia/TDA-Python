import Pila as p

miPila = p.Pila()

miPila.vacia()

for i in range(5):
    miPila.push(i)

miPila.mostrar()

miPila.queHayEnTop()