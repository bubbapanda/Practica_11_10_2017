# definir una funcion quetome un caracter y devuelva true en vocal

class caracter():

    def __init__(self):
        self.letra = ""
        self.vocal = False
        self.cuenta = 0

    def validar_vocal(self):
        self.letra = raw_input("introduce 1 caracter ")
        for i in self.letra:
            self.cuenta = self.cuenta + 1
        if self.cuenta > 1:
            print ("escribiste mas de 1 caracter ")
        if self.letra in ("aeiou"):
            self.vocal = True
        print (self.vocal)

lista = caracter()
lista.validar_vocal()