# definir una funcion histograma

class lista():

    def __init__(self):
        self.valores = []
        self.histograma = {}


    def histo(self):
        for a in self.valores:
            print ("")
            b=int(a)
            for c in range (0,b):
                print (" *",end =" ")


    def pedir_valores(self):
        i = input("cuantos valores deseas introducir ? ")
        while int(i) > 0:
            self.valores.append(input("Introduce los valores : "))
            i = int(i)-1
        print (self.valores)


bonche = lista()
bonche.pedir_valores()
bonche.histo()