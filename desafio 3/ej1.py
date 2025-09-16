import random

amigos = random.randint(4,10) #definimos cantidad de amigos

print(f"Vendrán {amigos} amigos a la fiesta")

i = 0

while i < amigos:

    opcion = random.randint(1,6) #generamos una opcion aleatoria

    comida = ""

    if opcion == 1:

        comida = "prepizza"

    elif opcion == 2:

        comida = "salsa de tomate"
        
    elif opcion == 3:

        comida = "muzzarella"

    elif opcion == 4:

        comida = "coca"

    elif opcion == 5:

        comida = "ron"

    else:

        comida = "whisky"


    print(comida)

    i += 1

