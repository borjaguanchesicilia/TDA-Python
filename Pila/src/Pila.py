class Pila:
    
    def __init__(self):
        self.vect = []
        self.top = -1

    def vacia(self):
        if self.top < 0:
            print ("La pila está vacía.")
        else:
            print ("La pila NO está vacía.")

    def push(self, dato):
        self.top += 1
        self.vect.append(dato)

    def pop(self):
        self.top -= 1
        self.vect.pop()

    def mostrar(self):
        tam = len(self.vect)
        self.vect.reverse()
        print ("La pila es: ")
        for i in range(tam):
            print (self.vect[i])
        print ("\n\n")
        self.vect.reverse()