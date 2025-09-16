"""
2. Encontrar la palabra más larga de la frase
Solicita una frase y muestra cual es la palabra más larga de la frase.
Ejemplo: El murcielago es un animal mamifero
Respuesta Esperada: murcielago

"""

"""

LOGICA DEL EJERCICIO:

1. IDENTIFICAR PALABRAS
2. CONTAR LONGITUD
3. ALMACENAR PALABRA COMO PAL_LARGA
4. VERIFICAR SI LEN PALABRA ES > LEN(PAL_LARGA)
5. SI ES, REEMPLAZAR, SINO NO

"""

frase = input("Ingrese una frase: ")

palabra = False

longitud = 0

pal = ""

palabra_larga = ""

i = 0

while i < len(frase):

    if frase[i] == " ": # espacio -> set palabra to false

        print("CARACTER VACIO")

        palabra = False

        print (f"la longitud de la ultima palabra {pal} es de {longitud}")

        if len(pal) > len(palabra_larga): #si la len de palabra actual > que la de palabra larga, la reescribe

            palabra_larga = pal

        longitud = 0 # reseteo la longitud al encontrar un espacio

        pal = "" #borramos la palabra actual para sumar de nuevo cuando haya otra

    else:
        print("Caracter no vacio")

        #ejecuto tareas si no es un espacio

        if not palabra: # Antes habia un espacio?

            palabra = True # no espacio -> set palabra to True

            longitud = 1 #comienzo a contar la longitud

            pal += frase[i]

            print(pal)
        
        else:

            print("esta letra se suma a una palabra")

            longitud += 1 #sumo uno a longitud por cada vez que

            pal += frase[i]

            print (pal)

            if i == (len(frase) - 1):

                if len(pal) > len(palabra_larga): #si la len de palabra actual > que la de palabra larga, la reescribe

                    palabra_larga = pal


    i += 1

print(f"la palabra mas larga es {palabra_larga}")