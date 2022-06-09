"""
escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

contraseña = "SENHA123"
ncontraseña = input("Cual es la contraseña? ")
ncontraseña = ncontraseña.upper()
if ncontraseña == contraseña:
    print("contraseña correcta!")
else:
    print("contraseña incorrecta!")