#Dada una cadena contar cuanta vocales tiene. Andrés Salan

cadena = "IES Antonio Sequeros"
contador = 0

for caracter in cadena.lower():
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        contador = contador + 1

print("El número de vocales de", cadena, "es", contador)


