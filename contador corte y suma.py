"""
Contador con corte y suma:

Pedir al usuario que ingrese números positivos.

El ciclo termina cuando se introduce un número mayor a 100.

Mostrar:

La suma total de los números ingresados (sin incluir el >100).
La cantidad de números válidos.

"""

numero = int(input("Ingrese un numero positivo"))

contador = 0

suma = 0

#Si el numero es negativo o menor a 100 entra al while

while numero < 0 or numero <= 100:

    if numero > 0: # filtro numeros que solo entraron por ser menos a 100 y no negativos

        contador += 1 # agrego 1 al contador por cada numero menos a 100, valido, ingresado
        suma += numero # sumatoria de numeros menores a 100

    #si el numero era negativo, solo pedimos el numero de vuelta, sino, lo contabilizamos y lo sumamos

    numero = int(input("Ingrese un numero positivo"))

print(f"La suma total es {suma}, la cantidad de numeros valida es {contador} y el ultimo numero ingresado es {numero}")