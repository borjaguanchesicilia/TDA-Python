class Cola:
    
    def __init__(self):
        self.vect = []
        self.primero = 0
        self.ultimo = -1
        self.auxPop = 0

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
        assert self.ultimo > self.primero, 'La cola está vacía'
        self.primero  += 1
        self.vect.pop(self.auxPop)
        self.vect.insert(self.auxPop, ' ')
        self.auxPop += 1
    
    def mostrar(self):
        print ("\nLa cola es:\n")
        tam = len(self.vect)
        for i in range(tam):
            print (self.vect[i], end=' ')
        print ("\n")