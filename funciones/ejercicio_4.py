"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""

def impuesto(factura,iva=21):
    iva = (iva / 100) + 1
    print(f"El valor de la factura con iva es {factura * iva} ")
    return
impuesto(100)