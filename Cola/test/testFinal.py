import Cola as c

miCola = c.Cola()

miCola.vacia()


for i in range(10):
    miCola.push(i)

miCola.vacia()

miCola.mostrar()

miCola.pop()
miCola.pop()
miCola.pop()
miCola.pop()

miCola.mostrar()

print("\nEl primero está en: " + str(miCola.primero))
print("\nEl último está en: " + str(miCola.ultimo))