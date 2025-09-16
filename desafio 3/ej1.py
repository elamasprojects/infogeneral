import random

amigos = random.randint(4,10) #definimos cantidad de amigos

print(f"Vendrán {amigos} amigos a la fiesta")

i = 0

# LOGICA DEL WHILE: CREAMOS POR CADA PERSONA UN NUMERO RANDOM, Y CADA NUMERO CORRESPONDE A UNA COMIDA PARTICULAR.
# DE ESA FORMA ASIGNAMOS COMIDAS Y LAS MOSTRAMOS

# inicializamos variabels para saber si se traen estos ingredientes o no

prepizza = False
salsa = False
muzzarella = False
coca = False
ron = False
whisky = False

while i < amigos:

    opcion = random.randint(1,6) #generamos una opcion aleatoria

    comida = ""

    if opcion == 1:

        comida = "prepizza"

        prepizza = True

    elif opcion == 2:

        comida = "salsa de tomate"

        salsa = True
        
        
    elif opcion == 3:

        comida = "muzzarella"

        muzzarella = True

    elif opcion == 4:

        comida = "coca"

        coca = True


    elif opcion == 5:

        comida = "ron"

        ron = True


    else:

        comida = "whisky"

        whisky = True



    print(f"Amigo trae {comida}")

    i += 1

pizza = False
roncola = False
whiscola = False

print ("Menu")
print ("====")


print("Bebidas:")

if coca:

    print ("Coca-Cola")

if whisky:

    print ("Whisky")

if ron:

    print ("Ron")

if coca and ron:

    roncola = True
    
    print ("Roncola")


if whisky and coca:

    whiscola = True

    print("Whiscola")

if prepizza and salsa and muzzarella:

    pizza = True

    print("Comida:")

    print("Pizza")
else:
    print("No hay comida")
