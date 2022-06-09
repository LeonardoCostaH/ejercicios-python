"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""
actual_contraseña = ("senha123")
contraseña = input("informe la contraseña: ")
while contraseña != actual_contraseña:
    contraseña = input("informe la contraseña: ")
print("contraseña correcta!")