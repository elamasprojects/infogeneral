"""
1. Solicitar dos numeros enteros positivos. 
2 Validar:

    1) El segundo debe ser mayor o igual que el segundo
    2) Positivos
    3) Numeros

2. Mostrar mensaje de error si no se cumplen y reingresar
3. Defininr intervalo usando ambos numeros como extremos
4. Buscar numero primo mas grande del intervalo
5. Buscar numero primo mas chico del intervalo
6. Si no hay ninguno, mostrarlo


"""

inicio = int(input("Ingresa el primer numero: ")) #pedimos primer numero

while inicio < 0: #mientras sea negativo
    
    inicio = int(input("Ingresa el primer numero correctamente: ")) #pedimos primer numero

fin = int(input("Ingresa el segundo número: "))

while fin < inicio or fin < 0:

    print("Error, ingresa otro numero") #mostramos el error

    fin = input("Ingresa el segundo número correctamente: ") #pedimos otro numero


print(f"El invervalo va desde {inicio} a {fin}")

# CONDICIONES PARA SER PRIMO: 
# 1) DIVISIBLE POR SI MISMO
# 2) DIVISIBLE POR 1 

primo_max = 0
primo_min = 99

while inicio < fin: #recorremos todo el invervalo

    esPrimo = True

    divisor = 2

    while divisor < inicio: #mientras el dividor es menor que el numero, se sigue dividiendo
        
        if inicio % divisor == 0:

            esPrimo = False

            print(f"este numero no es primo: {inicio}")

        divisor += 1

    if esPrimo:

        print(f"Este numero es primo: {inicio}")

        if inicio > primo_max: #validamos si el primo es mayor al primo maximo actual

                primo_max = inicio

        if inicio < primo_min:

                primo_min = inicio
    
    inicio += 1

if primo_max != 0:
     
    print(f"El primo más grande es: {primo_max}")

if primo_min != 99:
     
    print(f"El primo más chico es: {primo_min}")















# ESTE CODIGO BASICAMENTE HACE QUE SE DIVIDA EL NUMERO POR TODOS LOS NUMEROS ENTRE 2 Y ESE NUMERO Y SI ALGUNO DA RESTO 0, ENTONCES NO ES PRIMO

"""python
    es_primo = True  # Suponemos que el número es primo
    divisor = 2
    while divisor < numero_actual:
        if numero_actual % divisor == 0:  # Si es divisible, no es primo
            es_primo = False
        divisor += 1
    if es_primo and numero_actual > 1:
        print(f"{numero_actual} es primo.")
    numero_actual += 1
"""