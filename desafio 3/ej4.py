texto = input("Ingrese un string:")

while len(texto) > 100 or len(texto) < 3:
   
   texto = input("Ingrese un string:")

i = 0

while i < len(texto):

    again = False

    if ord(texto[i]) < 65 or (ord(texto[i]) > 90 and ord(texto[i]) < 97) or ord(texto[i]) > 123:

      texto = input("Ingrese otro string")
      
      while len(texto) > 100 or len(texto) < 3:
   
        texto = input("Ingrese un string:")

      again = True
    
    i += 1

    if again:
       
       i = 0

















"""
Acá básicamente hacemos que si y sigue siendo menor a longitud, 
o sea que se recorra todo el string en casi que no se termine de recorrer el while se va a ejecutar. 
También se va a ejecutar si la longitud del texto es mayor a 100 y también se va a ejecutar si la longitud del string es menor a 3. 
O sea que capaz que ya terminó de iterar todo el string pero la longitud es mayor a 100 entonces lo sigue ejecutando. 

"""