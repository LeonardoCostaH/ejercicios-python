"""Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se
guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario
con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor
True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente
menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar
clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

1- Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2- Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3- Preguntar por el NIF del cliente y mostrar sus datos.
4- Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5- Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6- Terminar el programa."""

clientes = {}
datos = ["NIF","nombre", "dirección", "teléfono", "correo", "preferente"]
while True:
    menu = input(f"qué quieres hacer? (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, \n"
                 f"(4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función \n"
                 f"de la opción elegida el programa tendrá que hacer lo siguiente: ")
    if menu == "1":
        datos_clientes = {}
        for d in datos:
            if d == "preferente":
                while True:
                    dato = input(f"Sos un cliente preferente? responda con (s) para sí y (n) para no. ")
                    if dato == "s" or dato == "n":
                        break
                if dato == "s":
                    dato = True
                elif dato == "n":
                    dato = False
                datos_clientes[d] = dato
            else:
                dato = input(f"Cual es tu {d}? ")
                if d == "NIF":
                    valor_nif = dato
                else:
                    datos_clientes[d] = dato
        clientes[valor_nif] = datos_clientes
        print(clientes)
    elif menu == "2":
        cual_eliminar = input(f"escriba el NIF del cliente que quieres eliminar: ")
        del clientes[cual_eliminar]
        print(clientes)
    elif menu == "3":
        cual_mostrar = input(f"escriba el NIF para mostrar todos los datos de ese cliente: ")
        print(clientes[cual_mostrar])
    elif menu == "4":
        print(clientes)
    elif menu == "5":
        for k, v in clientes.items():
            clientes_preferentes = {}
            for e, w in v.items():
                if e == "preferente":
                    if w:
                        clientes_preferentes[k] = v
        print(clientes_preferentes)
    elif menu == "6":
        print("atendimiento terminado!")
        break


