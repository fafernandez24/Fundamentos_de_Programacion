#Programa que diga si un número es primo o no.

#Definicion de variables.

n1 = int
divisor = int
contador = int
continuar = str

#Declaracion de variables.

divisor = 1
contador = 0
continuar = "SI"


#Entrada de datos de numeros enteros

n1 =int(input("Ingrese un numero: "))

#Condiconal if/elif(si) para que el algoritmo interprete de forma especial los casos en el cual el usuario ingrese 2 o algun numero negativo.

if n1 == 2:
    print("2 es el unico numero par que es primo")
elif n1 <= 1:
    print("No es mayor a 1, por lo que no es primo." )

#En caso de que no se cumpla ninguno de los dos condicionales iniciales, el algoritmo seguira con normalidad a traves del condicional else(si no).

else:
    
#Este ciclo while genera que mientras el numero divisor(comienza en uno), al ser dividido con n1 (que seria el dividendo) no de como residuo 0, se le sumara un numero al divisor.
#Ejemplo: Si antes el divisor era 1, ahora pasa a ser 2, si aun no se logra que el residuo de 0, pasara a 3, hasta lograr que el residuo de 0.


    while divisor <= n1:

#Este condicional es el que informa al algoritmo si encuentra algun divisor, sumandole uno a la variable "contador"(su valor inicial es 0)

        if n1 % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1

#En caso de que el contador llegue a ser mayor a 3, automaticamente se considera al numero como NO primo y el programa termina

        if contador >3:
            break
        if divisor >= 101:
            print("Su numero SI ES primo")
            break

#En caso de que el numero sea primo, solo tendra dos divisores

    if contador == 2:
        print("El numero ", n1, " SI ES primo")

#En caso de que el numero tenga 3 o mas divisores, hace que este automaticamente deje de ser un numero primo

    if contador >= 3:
        print("El numero ", n1, " NO ES primo")
    