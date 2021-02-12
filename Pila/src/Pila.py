class Pila:
    
    def __init__(self):
        self.vect = []
        self.top = -1

    def vacia(self):
        if self.top < 0:
            print ("La pila está vacía.")
        else:
            print ("La pila NO está vacía.")
        return self.top

    def push(self, dato):
        self.top += 1
        self.vect.append(dato)

    def pop(self):
        assert self.top > 0, 'La pila está vacía.'
        self.top -= 1
        self.vect.pop()

    def queHayEnTop(self):
        assert self.top > 0, 'La pila está vacía.'
        print  ("\nEn el  top hay: " + str(self.vect.index(self.top)))

    def mostrar(self):
        tam = len(self.vect)
        self.vect.reverse()
        print ("\nLa pila es: ")
        for i in range(tam):
            print (self.vect[i])
        print ("\n")
        self.vect.reverse()