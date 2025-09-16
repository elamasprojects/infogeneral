""""
Pedir al usuario un número entre 50 y 100. Mientras esté fuera de ese rango, volver a pedirlo. Cuando el valor sea válido, imprimir "Número aceptado".

"""

numero = int(input("Ingresa un numero entre 50 y 100"))

while numero < 50 or numero > 100:

    print("numero incorrecto")
    numero = int(input("Ingresa un numero entre 50 y 100"))

print("numero aceptado")