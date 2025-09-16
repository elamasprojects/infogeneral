
frase = input("ingrese una frase: ")



# palabra arranca en False

palabra = False

palabra_count = 0

i = 0

# iniciamos ciclo while para recorrer la frase caracter por caracter con un indice

while i < len(frase): #mientras el i sea menor a la longitud de la frase, se va a ejecutar el ciclo

    if frase[i] == " ": #si el caracter en la posicion i es un espacio, se imprime que es un caracter vacio
        print("Caracter vacio")
        palabra = False #palabra se vuelve False
    else:
        print("Caracter no vacio")
        if palabra == False: #si palabra es False, se vuelve True
            palabra = True
            palabra_count += 1 #si palabra es True, se incrementa el contador de palabras

        else:
            print("ya se contabilizó una palabra") #si palabra es True, se imprime que ya se contabilizó una palabra

    i += 1
    
print(f"La cantidad de palabras en la frase es: {palabra_count}")





## ASI LO HARIA CON FOR (SOLO A PARTIR DEL SEGUNDO PARCIAL)

""" for i in nombre:

    if i == " ":
        print("Caracter vacio")
    else:
        print("Caracter no vacio")
        palabra = True

    if palabra == True 

    if palabra == True:
        palabra_count += 1

print(f"La cantidad de palabras en la frase es: {palabra_count}")


print("fin del programa") """