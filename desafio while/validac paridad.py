"""
Pedir al usuario un número que debe ser impar y positivo. Mientras el número no cumpla esa condición, volver a pedirlo. Cuando sea válido, mostrar el número ingresado.

"""

numero = input("ingrese un mumero impar y positivo") 

while numero < 0 or numero % 2 == 0:

    numero = int(input("ingrese un mumero impar y positivo"))
    print("Numero incorrecto")

print(f"Gracias, el numero {numero} es correcto")


