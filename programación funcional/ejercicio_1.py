"""Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un
precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes
de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para
aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta."""

def aplicar_descuento(porc,precio):
    porcentaje = porc / 100
    descuento = 1 - porcentaje
    return precio * descuento


def aplicar_iva(iva,precio):
    porcentaje = iva / 100
    descuento_final = 1 + porcentaje
    return precio * descuento_final

def dic_precios():
    dic = {}
    