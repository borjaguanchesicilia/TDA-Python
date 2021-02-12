class Cola:

    def __init__(self):
        self.vect = []
        self.frente = 0
        self.final = -1

    def vacia(self):
        if self.final < self.frente:
            print ("\nLa cola está vacía.")
        else:
            print ("\nLa cola NO está vacía.")

    def tamCola(self):
        print ("\nEl tamaño de la cola es: " + str((self.final - self.frente) + 1))

    def push(self, dato):    
        self.final  += 1
        self.vect.append(dato)
    
    def mostrar(self):
        print ("\nLa cola es:\n")
        tam = len(self.vect)
        for i in range(tam):
            print (self.vect[i], end=' ')
        print ("\n")