# definir una funcion sum y multiplicacion

class lista():

    def __init__(self):
        self.valores = []
        self.rsuma = 0
        self.rmult = 1

    def suma(self):
        for a in self.valores:
            self.rsuma += int(a)
        print (self.rsuma)

    def mult(self):
        for a in self.valores:
            self.rmult *= int(a)
        print (self.rmult)

    def pedir_valores(self):
        i = input("cuantos valores deseas introducir ? ")
        while i > 0:
            self.valores.append(raw_input("Introduce los valores : "))
            i = i-1
        print (self.valores)


bonche = lista()
bonche.pedir_valores()
bonche.suma()
bonche.mult()