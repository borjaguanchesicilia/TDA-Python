class Cola:
    
    def __init__(self):
        self.vect = []
        self.primero = 0
        self.ultimo = -1

    def vacia(self):
        if self.ultimo < self.primero:
            print ("\nLa cola está vacía.")
        else:
            print ("\nLa cola NO está vacía.")

    def tamCola(self):
        print ("\nEl tamaño de la cola es: " + str((self.ultimo - self.primero) + 1))

    def push(self, dato):    
        self.ultimo  += 1
        self.vect.append(dato)

    def pop(self):    
        self.primero  += 1
        self.vect.pop(0)
        self.vect.insert(0, ' ')
    
    def mostrar(self):
        print ("\nLa cola es:\n")
        tam = len(self.vect)
        for i in range(tam):
            print (self.vect[i], end=' ')
        print ("\n")