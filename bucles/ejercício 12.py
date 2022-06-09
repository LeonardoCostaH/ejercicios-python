"""
escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

"""frase = input("escriba una frase: ")
letra = input("ahora una letra: ")
contador = 0
for i in range(len(frase)):
    if letra == frase[i]:
        contador+=1
print(contador)"""

frase = input("introduce una frase: ")
letra = input("introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador+=1
print(contador)