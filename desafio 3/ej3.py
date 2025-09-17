"""

Ejercicio 3


Desarrollar un programa en Python que permita al usuario ingresar múltiples cadenas de texto, procesarlas según ciertas condiciones y realizar análisis específicos sobre ellas.
Instrucciones:
Ingreso de cadenas:


1. El programa debe solicitar al usuario que introduzca cadenas de texto de forma repetitiva. La entrada de datos finalizará cuando el usuario introduzca una cadena vacía.


2. Validación de cadenas: Solo se considerarán válidas las cadenas que contengan exclusivamente letras (mayúsculas o minúsculas). 
Si una cadena contiene números, símbolos u otros caracteres no alfabéticos, se considerará inválida y será ignorada en los procesos posteriores.


3. Procesamiento de cadenas válidas:

Por cada cadena válida ingresada, el programa debe generar una nueva cadena construida de la manera como se muestra en los siguientes ejemplos:

                          Cadena original: "Code" 
                          Cadena resultante: "CCoCodCode"
                          Cadena original: "abc"
                          Cadena resultante: "aababc"
                          Cadena original: "ab"
                          Cadena resultante: "aab"
                          Cadena original: "a"                  
                          Cadena resultante: "a"

4. Análisis adicional:

Mostrar la cantidad total de cadenas inválidas ingresadas. 
Calcular y mostrar el porcentaje que representan las cadenas válidas respecto al total de cadenas ingresadas (válidas + inválidas).
Identificar y mostrar cuál de las cadenas válidas contiene la mayor cantidad de vocales.


"""


cadena = input("Ingresar una cadena de texto")


contador_val = 0

contador_inv = 0

while cadena != "":

    valida = True

    cadena = input("Ingresar una cadena de texto")

    i = 0

    # VERIFICAMOS SI ES VALIDA

    while i < len(cadena): #recorre cada caracter de la cadena

        if ord(cadena[i]) < 65 or (ord(cadena[i]) > 90 and ord(cadena[i]) < 97) or ord(cadena[i]) > 123: # ¿No es letra?

            valida = False

        i += 1

    # TERMINAMOS DE RECORRER TODA LA CADENA. EN ESTE PUNTO, SI ES VALIDA, deberiamos tener aún valida = True

    # PROCEDEMOS A CONTABILIZAR 

    if valida:

        contador_val += 1

    else:

        contador_inv += 1


#mostramos cantidad de cadenas validas e invalidas:

print(f"Hay {contador_val} cadenas validas y {contador_inv} cadenas invalidas")

#mostramos porcentaje: