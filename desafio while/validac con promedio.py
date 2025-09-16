"""
Validación compleja con promedio:
Pedir al usuario que ingrese exactamente 5 números positivos.
Si el usuario ingresa un valor negativo, debe volver a intentarlo hasta cumplir.
Al finalizar, mostrar el promedio de los 5 números válidos.

"""

numero = int(input("Ingrese un numero positivo: "))

suma = 0

contador = 0

if numero > 0:
    contador += 1
    suma += numero # sumatoria de los numeros validos
    print("Numero valido") # mostramos que el numero es valido

while contador < 5:

    #volvemos a pedir el numero
    numero = int(input("Ingrese un numero positivo: "))

    # sumamos al contador solo si el numero es positivo

    if numero > 0:
        contador += 1
        suma += numero # sumatoria de los numeros validos
        print("Numero valido") # mostramos que el numero es valido

promedio = suma / 5 # calculamos el promedio sumando todos y dividiendolos por la cantidad de numeros

print(f"El promedio de los numeros es {promedio}")


    

    

