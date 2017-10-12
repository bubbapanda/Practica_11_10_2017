# Definir una funcion max() que tome como argumento 2 numero y devuelva el mayor de ellos

def maximo (num1,num2):
    if num1 > num2:
        print (" el numero mayor de " + str(num1) + " y " + str(num2) + " es : " + str(num1))
    else:
        print (" el numero mayor de " + str(num1) + " y " + str(num2) + " es : " + str(num2))


valor1 = input("introduce el valor 1 : ")
valor2 = input("introduce el valor 2 : ")
maximo(valor1,valor2)

