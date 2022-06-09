"""
escribir un programa que muestre el eco de todo lo que el usuario introduzca
hasta que el usuario escriba "salir" que terminará.
"""

"""
eco = input("introduzca una palabra o texto: ")
salir = "salir"
while eco == salir:
        continue
print(eco)"""
"""
salir = "salir"
print("Hola, introduzca una palabra o texto, o escriba salir: ")
palabra = input("")
while palabra != salir:
    palabra = input(f"{palabra}")
    """

while True:
    frase = input("introduce algo: ")
    if frase == "salir":
        break
    print(frase)