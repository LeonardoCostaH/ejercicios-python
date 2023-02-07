"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""


def impuesto(total_sin_iva, iva=21):
    iva = iva / 100 + 1
    return total_sin_iva * iva
total = impuesto(100)
print(f"El valor de la factura con iva es {total} ")

