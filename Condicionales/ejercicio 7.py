"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
renta                       tipo impositivo
menos de 10000                  5%
entre 10000 y 20000             15%
entre 20000 y 35000             20%
entre 35000 y 60000             30%
más de 60000                    45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el
tipo impositivo que le corresponde
"""

renta_anual = input("Cual es tu renta anual? ")
if not renta_anual.isdigit():
    print("valor errado")
else:
    renta_anual = int(renta_anual)
    if renta_anual <= 10000:
        print("5% de impuesto ")
    elif renta_anual <= 20000:
        print("15% de impuesto")
    elif renta_anual <= 35000:
        print("20% de impuesto")
    elif renta_anual <= 60000:
        print("30% de impuesto")
    else:
        print("45% de impuesto")