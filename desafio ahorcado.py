"""
El ahorcado
Objetivo:
Desarrollar un programa en Python que simule el clásico juego del ahorcado. Un jugador debe adivinar una palabra secreta que ha sido introducida previamente por otro jugador.
Descripción del juego:
Jugador 1 ingresa una palabra secreta.


Jugador 2 intenta adivinarla, letra por letra.


El programa muestra la palabra oculta usando guiones bajos (_) por cada letra aún no descubierta.


Cada intento incorrecto le resta una vida al jugador.


El número total de intentos permitidos es igual a la longitud de la palabra + 2 intentos adicionales.


El juego finaliza cuando:


El jugador adivina toda la palabra (¡Ganaste!)


Se queda sin intentos (¡Perdiste!)

------------

Requisitos del programa:

1. Selección de la palabra secreta
El programa debe recibir una palabra ingresada por el Jugador 1.


Debe verificar que todos los caracteres de la palabra sean letras mayúsculas o minúsculas (sin números ni símbolos).

2. Mostrar la palabra oculta
Inicialmente, se deben mostrar guiones bajos (_) por cada letra de la palabra.


Cuando el Jugador 2 adivine una letra correctamente, debe revelarse en todas las posiciones correspondientes.



3. Entrada del jugador
El jugador debe ingresar una letra a la vez.


El programa debe permitir el ingreso de letras ya adivinadas (repetidas), aunque no otorgue puntos por ellas.


4. Intentos limitados
El número total de intentos es igual a la longitud de la palabra secreta + 2.


Cada vez que el jugador ingrese una letra incorrecta, se descontará un intento.


5. Verificar victoria o derrota
Si el jugador adivina todas las letras: mostrar el mensaje "¡Ganaste!"


Si se queda sin intentos antes de completar la palabra: mostrar "¡Perdiste!" y revelar la palabra secreta completa.


6. Control de entradas
El programa debe validar que el jugador solo ingrese una letra a la vez.


No se deben aceptar entradas vacías, múltiples letras, ni caracteres especiales.


Ejemplo:
palabra secreta: Amigo
Bienvenido al juego del Ahorcado
La palabra secreta tiene 5 letras.
Cantidad de intentos: 7

_ _ _ _ _

Ingresa una letra: a
La palabra secreta es: A _ _ _ _
Te quedan 7 intentos.
 
Ingresa una letra: e
La palabra secreta es: A _ _ _ _
Te quedan 6 intentos.
 
Ingresa una letra: r
La palabra secreta es: A _ _ _ _
Te quedan 5 intentos.

Ingresa una letra: o
La palabra secreta es: A _ _ _ o
Te quedan 4 intentos.




"""

"""

LOGICA DEL PROGRAMA:



"""

palabra = input("Ingrese la palabra secreta: ")

#LOGICA DE VALIDACION DE PALABRA SIN NUMEROS Y SIMBOLOS:

"""

contador = 0

while contador < len(palabra):

    if (ord(palabra[i]) >= 65 and ord(palabra[i]) <= 90) or (ord(palabra[i]) >= 97 and ord(palabra[i]) <= 122):

            palabra = input("Ingrese la palabra secreta BIEN: ")

    contador += 1
    
"""



# VALIDACION DE QUE NO TENGA NUMEROS NI SIMBOLOS

intentos = len(palabra) + 2 # un intento por cada letra y 2 más

print(f"Tenes {intentos} intentos")

respuesta = "_" * len(palabra) # Creamos la palabra con guiones bajos


# HASTA AHORA TENEMOS: INGRESO DE PALABRA + INTENTOS + VISUAL RESPUESTA

# NEXT STEP: VALIDAR LETRA X LETRA

#WHILE MAYOR: MIENTRAS QUE HAYA UN " " EN LA PALABRA, PEDIMOS LETRA


# WHILE MAYOR: VALIDAMOS QUE TENGA INTENTOS Y QUE NO HAYA "_" DENTRO DE LA NUEVA RESPUESTA 

# WHILE MENOR: RECORREMOS LA PALABRA

while intentos > 0 and "_" in respuesta: # quedan intentos y hay algun "_" dentor de respuesta

    nueva_respuesta = ""

    letra = input("ingrese una letra: ")

    i = 0

    esletra = False


    while i < len(palabra):


        if letra == palabra[i]:

            # ACÁ VA EL CODIGO QUE REEMPLAZA LETRA EN RESPUESTA
            # LOGICA: LETRA? SI -> OBTENEMOS ÍNDICE -> REESCRIBIMOS VAR RESPUESTA

            nueva_respuesta += letra

            esletra = True

        else: #si la letra no esta en la palabra restamos una vida

            nueva_respuesta += respuesta[i]

        i += 1
    
    if esletra == False:

        intentos -= 1

    respuesta = nueva_respuesta

    print(respuesta)

if intentos > 1:

    print(f"Ganaste! Felicidades. Te sobraron {intentos} intentos")

else:

    print("Perdiste :(")

print(respuesta)

"""
u = 0


while u < len(palabra):


    if palabra[u] == "_":

        adivino = False

    else:

        adivino = True

    while adivino == False:

        letra = input("ingrese una letra: ")

        i = 0

        # WHILE MENOR: RECORREMOS LA PALABRA

        while i < len(palabra):

            esletra = False

            if letra == palabra[i]:

                # ACÁ VA EL CODIGO QUE REEMPLAZA LETRA EN RESPUESTA
                # LOGICA: LETRA? SI -> OBTENEMOS ÍNDICE -> REESCRIBIMOS VAR RESPUESTA

                nueva_respuesta += letra

                print(respuesta)

                esletra = True

            else: #si la letra no esta en la palabra restamos una vida

                nueva_respuesta += respuesta[i]

            if esletra == False:

                intentos -= 1

            i += 1
    
    u += 1
"""

# print(f"la letra ingresada es {letra[i]} y la primer letra de la palabra es {palabra[i]}") 