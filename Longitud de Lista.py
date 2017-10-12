# definir una funcion que calcule la longitud de una lista o cadena dada

class longitud_cadena():

    def __init__(self):
        self.cadena = ""
        self.cuenta = 0

    def contar_longitud(self):
        self.cadena = raw_input("introduce la cadena ")
        for i in self.cadena:
            self.cuenta = self.cuenta + 1
        print ("La longitud de la cadena es: " + str(self.cuenta))

lista = longitud_cadena()
lista.contar_longitud()