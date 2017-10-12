# Definir una funcion max() que tome como argumento 3 numero y devuelva el mayor de ellos

def maximo3 (num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            print (" el numero mayor de " + str(num1) + ", " + str(num2) + " y " + str(num3) + " es : " + str(num1))
        else:
            print (" el numero mayor de " + str(num1) + ", " + str(num2) + " y " + str(num3) + " es : " + str(num3))
    else:
        if num2 > num3:
            print (" el numero mayor de " + str(num1) + ", " + str(num2) + " y " + str(num3) + " es : " + str(num2))
        else:
            print (" el numero mayor de " + str(num1) + ", " + str(num2) + " y " + str(num3) + " es : " + str(num3))


valor1 = input("introduce el valor 1 : ")
valor2 = input("introduce el valor 2 : ")
valor3 = input("introduce el valor 3 : ")
maximo3(valor1,valor2,valor3)
