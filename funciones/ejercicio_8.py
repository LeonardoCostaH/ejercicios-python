"""Escribir una función que reciba una muestra de números en una lista y devuelva
un diccionario con su media, varianza y desviación típica."""

def dic_datos(*args):
    media = sum(args) / args.__len__()
    varianza = sum([(x - media)**2 for x in args]) / len(args)
    desviacion = round(varianza ** 0.5,2)
    diccionario = {}
    diccionario["Media"] = media
    diccionario["Varianza"] = varianza
    diccionario["Desviación Típica"] = desviacion
    return diccionario
print(dic_datos(1500,1200,1700,1300,1800))
