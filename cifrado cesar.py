""" Desplaza cada letra de una palabra una cantidad fija de posiciones en el alfabeto (solo minsculas)

Ejemplo: hola con desplazamiento 3

Respuesta esperada: krod
"""
"""

desplazamiento = 3

palabra = input("ingrese una palabra: ")

i = 0

letra = palabra[i]

while i < len(palabra):

    letra = 




print(palabra)


"""

# palabra y desplazamiento
palabra = input("ingrese una palabra: ")
desplazamiento = 3

i = 0
resultado = ""

while i < len(palabra):

    letra = palabra[i] # letra es la letra en la posicion i de la palabra

    pos = ord(letra) - ord('a') # pos es la posicion de la letra en el alfabeto

    nueva_pos = pos + desplazamiento # nueva_pos es la nueva posicion de la letra

    if nueva_pos > 25: # si la nueva posicion es mayor a 25, se resta 26
        nueva_pos = nueva_pos - 26  # si la nueva posicion es mayor a 25, se resta 26

    if nueva_pos < 0: # si la nueva posicion es menor a 0, se suma 26
        nueva_pos = nueva_pos + 26  # si la nueva posicion es menor a 0, se suma 26

    nueva_letra = chr(nueva_pos + ord('a')) # nueva_letra es la letra en la nueva posicion

    resultado = resultado + nueva_letra # resultado es la palabra cifrada

    i += 1 # i es la posicion de la letra en la palabra

print(resultado)

